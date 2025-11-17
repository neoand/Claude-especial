# 🐍 Python Scripts

Scripts Python reutilizáveis do projeto.

## Convenções

### Nomenclatura
```
verbo_substantivo.py

✅ backup_database.py
✅ process_data.py
✅ send_email.py
❌ backup.py (muito genérico)
❌ script1.py (não descritivo)
```

### Header Obrigatório

```python
#!/usr/bin/env python3
"""
Script: nome.py
Description: Descrição do que faz
Usage: python nome.py [args]
Author: Claude
Created: YYYY-MM-DD
"""

import sys
import argparse
```

### Argparse

```python
def main():
    parser = argparse.ArgumentParser(description='Descrição do script')
    parser.add_argument('input', help='Input file')
    parser.add_argument('-o', '--output', help='Output file', default='output.txt')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')

    args = parser.parse_args()

    # Lógica aqui

if __name__ == '__main__':
    main()
```

## Exemplos

### process_data.py

```python
#!/usr/bin/env python3
"""
Script: process_data.py
Description: Process CSV data and generate report
Usage: python process_data.py input.csv --output report.txt
Author: Claude
Created: 2025-11-17
"""

import sys
import argparse
import csv

def process_csv(input_file, output_file):
    """Process CSV and write report"""
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    # Process data
    total = len(data)

    # Write report
    with open(output_file, 'w') as f:
        f.write(f"Total records: {total}\n")

    print(f"✅ Report written to {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Process CSV data')
    parser.add_argument('input', help='Input CSV file')
    parser.add_argument('-o', '--output', default='report.txt', help='Output file')

    args = parser.parse_args()

    process_csv(args.input, args.output)

if __name__ == '__main__':
    main()
```

## Boas Práticas

1. **Use type hints** - Melhora legibilidade
2. **Docstrings** - Sempre documente funções
3. **Argparse** - Para argumentos de linha de comando
4. **Error handling** - Try/except quando apropriado
5. **Logging** - Use logging ao invés de print
6. **Virtual env** - Documente dependências

## Dependências

Se o script precisa de bibliotecas externas:

```python
# requirements.txt
requests==2.28.0
pandas==1.5.0
```

Instalar:
```bash
pip install -r requirements.txt
```

## Como Claude Usa

Claude descobre scripts Python da mesma forma que bash:

1. Você: "Processe os dados do CSV"
2. Claude → skill `tool-inventory`
3. Verifica: `.claude/scripts/python/process*.py`
4. Encontra e executa!

## Adicionar Novo Script

```bash
# 1. Criar script
nano .claude/scripts/python/meu_script.py

# 2. Adicionar header e docstring

# 3. Tornar executável
chmod +x .claude/scripts/python/meu_script.py

# 4. Testar
python .claude/scripts/python/meu_script.py --help

# 5. Claude descobrirá automaticamente!
```
