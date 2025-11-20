#!/usr/bin/env python3
"""
Generic Database MCP Server - Template para Claude Code

Interface genérica para consultas SQL com segurança e validação.
Suporta PostgreSQL e MySQL com extensibilidade para outros bancos.

Métodos disponíveis:
- db.list_tables: Lista todas tabelas do banco
- db.describe_table: Descreve estrutura de uma tabela
- db.query: Executa SELECT query segura
- db.get_record: Busca registro específico
- db.get_schema: Retorna schema completo do banco
"""

import sys
import json
import os
from pathlib import Path
from typing import Dict, List, Any, Optional
import logging

# Importar drivers de banco (opcional)
try:
    import psycopg2
    PSYCOPG2_AVAILABLE = True
except ImportError:
    PSYCOPG2_AVAILABLE = False

try:
    import mysql.connector
    MYSQL_AVAILABLE = True
except ImportError:
    MYSQL_AVAILABLE = False

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GenericDatabaseMCP:
    """MCP Server genérico para consultas de banco de dados"""

    def __init__(self):
        self.project_root = Path(__file__).parent.parent.parent.parent
        self.load_config()
        self.connection = None
        self.db_type = self.db_config.get('type', 'postgresql')

    def load_config(self):
        """Carrega configuração do banco de dados"""
        self.db_config = {
            'type': os.getenv('DB_TYPE', 'postgresql'),  # postgresql, mysql, sqlite
            'host': os.getenv('DB_HOST', 'localhost'),
            'port': int(os.getenv('DB_PORT', '5432')),
            'database': os.getenv('DB_NAME', 'your_database'),
            'user': os.getenv('DB_USER', 'your_user'),
            'password': os.getenv('DB_PASSWORD', 'your_password'),
            'sqlite_path': os.getenv('DB_SQLITE_PATH', 'database.db')
        }

    def get_connection(self):
        """Estabelece conexão com o banco de dados"""
        if self.connection:
            return self.connection

        try:
            if self.db_type == 'postgresql':
                if not PSYCOPG2_AVAILABLE:
                    raise ImportError("psycopg2-binary não instalado")
                self.connection = psycopg2.connect(
                    host=self.db_config['host'],
                    port=self.db_config['port'],
                    database=self.db_config['database'],
                    user=self.db_config['user'],
                    password=self.db_config['password']
                )

            elif self.db_type == 'mysql':
                if not MYSQL_AVAILABLE:
                    raise ImportError("mysql-connector-python não instalado")
                self.connection = mysql.connector.connect(
                    host=self.db_config['host'],
                    port=self.db_config['port'],
                    database=self.db_config['database'],
                    user=self.db_config['user'],
                    password=self.db_config['password']
                )

            elif self.db_type == 'sqlite':
                import sqlite3
                self.connection = sqlite3.connect(self.db_config['sqlite_path'])
                self.connection.row_factory = sqlite3.Row

            else:
                raise ValueError(f"Tipo de banco não suportado: {self.db_type}")

            logger.info(f"Conectado ao banco {self.db_type}: {self.db_config['database']}")
            return self.connection

        except Exception as e:
            logger.error(f"Erro de conexão: {e}")
            raise

    def handle_list_tables(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Lista todas tabelas do banco"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()

            if self.db_type == 'postgresql':
                query = """
                SELECT table_name, table_type
                FROM information_schema.tables
                WHERE table_schema NOT IN ('information_schema', 'pg_catalog')
                ORDER BY table_name
                """
            elif self.db_type == 'mysql':
                query = """
                SELECT table_name, table_type
                FROM information_schema.tables
                WHERE table_schema = DATABASE()
                ORDER BY table_name
                """
            elif self.db_type == 'sqlite':
                query = """
                SELECT name as table_name, 'table' as table_type
                FROM sqlite_master
                WHERE type='table' AND name NOT LIKE 'sqlite_%'
                ORDER BY name
                """
            else:
                raise ValueError(f"Consulta não implementada para {self.db_type}")

            cursor.execute(query)
            results = cursor.fetchall()

            tables = []
            for row in results:
                tables.append({
                    'name': row[0],
                    'type': row[1] if len(row) > 1 else 'table'
                })

            return {
                'success': True,
                'database': self.db_config['database'],
                'db_type': self.db_type,
                'table_count': len(tables),
                'tables': tables
            }

        except Exception as e:
            logger.error(f"Erro em list_tables: {e}")
            return {'success': False, 'error': str(e)}

    def handle_describe_table(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Descreve estrutura de uma tabela específica"""
        table_name = params.get('table')
        if not table_name:
            return {'success': False, 'error': 'Parâmetro "table" é obrigatório'}

        try:
            conn = self.get_connection()
            cursor = conn.cursor()

            if self.db_type == 'postgresql':
                query = """
                SELECT
                    column_name,
                    data_type,
                    is_nullable,
                    column_default,
                    character_maximum_length,
                    numeric_precision,
                    numeric_scale
                FROM information_schema.columns
                WHERE table_name = %s
                ORDER BY ordinal_position
                """
                cursor.execute(query, (table_name,))

            elif self.db_type == 'mysql':
                query = """
                SELECT
                    column_name,
                    data_type,
                    is_nullable,
                    column_default,
                    character_maximum_length,
                    numeric_precision,
                    numeric_scale
                FROM information_schema.columns
                WHERE table_name = %s AND table_schema = DATABASE()
                ORDER BY ordinal_position
                """
                cursor.execute(query, (table_name,))

            elif self.db_type == 'sqlite':
                cursor.execute(f"PRAGMA table_info({table_name})")
                results = cursor.fetchall()
                columns = []
                for row in results:
                    columns.append({
                        'column_name': row[1],
                        'data_type': row[2],
                        'is_nullable': 'YES' if row[3] == 0 else 'NO',
                        'column_default': row[4],
                        'character_maximum_length': None,
                        'numeric_precision': None,
                        'numeric_scale': None
                    })

                return {
                    'success': True,
                    'table': table_name,
                    'column_count': len(columns),
                    'columns': columns
                }

            results = cursor.fetchall()
            columns = []
            for row in results:
                columns.append({
                    'column_name': row[0],
                    'data_type': row[1],
                    'is_nullable': row[2],
                    'column_default': row[3],
                    'character_maximum_length': row[4],
                    'numeric_precision': row[5],
                    'numeric_scale': row[6]
                })

            return {
                'success': True,
                'table': table_name,
                'column_count': len(columns),
                'columns': columns
            }

        except Exception as e:
            logger.error(f"Erro em describe_table: {e}")
            return {'success': False, 'error': str(e)}

    def handle_query(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Executa SELECT query segura"""
        query = params.get('query', '').strip()
        limit = min(params.get('limit', 100), 1000)

        if not query:
            return {'success': False, 'error': 'Parâmetro "query" é obrigatório'}

        # Apenas permitir SELECT queries
        if not query.upper().startswith('SELECT'):
            return {'success': False, 'error': 'Apenas queries SELECT são permitidas'}

        # Verificar keywords perigosas
        dangerous_keywords = ['DELETE', 'UPDATE', 'INSERT', 'DROP', 'ALTER', 'TRUNCATE']
        for keyword in dangerous_keywords:
            if keyword in query.upper():
                return {'success': False, 'error': f'Keyword "{keyword}" não permitido'}

        # Adicionar LIMIT se não tiver
        if 'LIMIT' not in query.upper() and self.db_type in ['postgresql', 'mysql']:
            query += f" LIMIT {limit}"

        try:
            conn = self.get_connection()
            cursor = conn.cursor()

            cursor.execute(query)
            results = cursor.fetchall()

            # Obter nomes das colunas
            if self.db_type == 'sqlite':
                columns = [desc[0] for desc in cursor.description]
            else:
                columns = [desc[0] for desc in cursor.description]

            # Converter para lista de dicionários
            rows = []
            for row in results:
                if self.db_type == 'sqlite':
                    rows.append(dict(zip(columns, row)))
                else:
                    rows.append(dict(zip(columns, row)))

            return {
                'success': True,
                'query': query,
                'columns': columns,
                'row_count': len(rows),
                'rows': rows
            }

        except Exception as e:
            logger.error(f"Erro em query: {e}")
            return {'success': False, 'error': str(e)}

    def handle_get_record(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Busca registro específico por ID e tabela"""
        table_name = params.get('table')
        record_id = params.get('id')
        id_column = params.get('id_column', 'id')

        if not table_name or not record_id:
            return {'success': False, 'error': 'Parâmetros "table" e "id" são obrigatórios'}

        try:
            conn = self.get_connection()
            cursor = conn.cursor()

            if self.db_type == 'postgresql' or self.db_type == 'mysql':
                query = f'SELECT * FROM {table_name} WHERE {id_column} = %s LIMIT 1'
                cursor.execute(query, (record_id,))
            else:  # SQLite
                query = f'SELECT * FROM {table_name} WHERE {id_column} = ? LIMIT 1'
                cursor.execute(query, (record_id,))

            result = cursor.fetchone()

            if not result:
                return {
                    'success': False,
                    'error': f'Registro {record_id} não encontrado em {table_name}'
                }

            # Obter nomes das colunas
            if self.db_type == 'sqlite':
                columns = [desc[0] for desc in cursor.description]
            else:
                columns = [desc[0] for desc in cursor.description]

            # Converter para dicionário
            record = dict(zip(columns, result))

            return {
                'success': True,
                'table': table_name,
                'id': record_id,
                'record': record
            }

        except Exception as e:
            logger.error(f"Erro em get_record: {e}")
            return {'success': False, 'error': str(e)}

    def handle_get_schema(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Retorna schema completo do banco"""
        try:
            tables_result = self.handle_list_tables({})
            if not tables_result['success']:
                return tables_result

            schema = {
                'database': self.db_config['database'],
                'db_type': self.db_type,
                'tables': {},
                'total_tables': tables_result['table_count']
            }

            # Descrever cada tabela
            for table_info in tables_result['tables']:
                table_name = table_info['name']
                desc_result = self.handle_describe_table({'table': table_name})

                if desc_result['success']:
                    schema['tables'][table_name] = {
                        'type': table_info['type'],
                        'columns': desc_result['columns'],
                        'column_count': desc_result['column_count']
                    }
                else:
                    schema['tables'][table_name] = {
                        'error': desc_result['error']
                    }

            return {
                'success': True,
                'schema': schema
            }

        except Exception as e:
            logger.error(f"Erro em get_schema: {e}")
            return {'success': False, 'error': str(e)}

    def handle_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Processa requisição MCP"""
        method = request.get('method', '')
        params = request.get('params', {})

        logger.info(f"Processando método: {method}")

        # Route para método apropriado
        if method == 'db.list_tables':
            return self.handle_list_tables(params)
        elif method == 'db.describe_table':
            return self.handle_describe_table(params)
        elif method == 'db.query':
            return self.handle_query(params)
        elif method == 'db.get_record':
            return self.handle_get_record(params)
        elif method == 'db.get_schema':
            return self.handle_get_schema(params)
        else:
            return {
                'success': False,
                'error': f'Método desconhecido: {method}',
                'available_methods': [
                    'db.list_tables',
                    'db.describe_table',
                    'db.query',
                    'db.get_record',
                    'db.get_schema'
                ]
            }

    def run(self):
        """Inicia o MCP server loop"""
        logger.info("Iniciando Generic Database MCP Server...")
        logger.info(f"Configuração: {self.db_type} - {self.db_config['database']}")

        try:
            for line in sys.stdin:
                if not line.strip():
                    continue

                try:
                    request = json.loads(line.strip())
                    response = self.handle_request(request)

                    # Adicionar timestamp se sucesso
                    if response.get('success', False):
                        response['timestamp'] = str(Path(__file__).stat().st_mtime)

                    print(json.dumps(response), flush=True)
                    sys.stdout.flush()

                except json.JSONDecodeError as e:
                    error_response = {
                        'success': False,
                        'error': f'JSON decode error: {str(e)}'
                    }
                    print(json.dumps(error_response), flush=True)
                    sys.stdout.flush()

        except KeyboardInterrupt:
            logger.info("Encerrando Generic Database MCP Server...")
        except Exception as e:
            logger.error(f"Erro no MCP server: {e}")
        finally:
            if self.connection:
                self.connection.close()

if __name__ == "__main__":
    server = GenericDatabaseMCP()
    server.run()