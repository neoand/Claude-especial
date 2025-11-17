# 📜 Bash Scripts

Scripts bash reutilizáveis do projeto.

## Convenções

### Nomenclatura
```
verbo-substantivo.sh

✅ server-restart.sh
✅ db-backup.sh
✅ logs-tail.sh
❌ restart.sh (muito genérico)
❌ script1.sh (não descritivo)
```

### Header Obrigatório

```bash
#!/bin/bash
# Script: nome.sh
# Description: Descrição do que faz
# Usage: ./nome.sh [parametros]
# Author: Claude
# Created: YYYY-MM-DD

set -e  # Exit on error
```

### Parâmetros

```bash
# Valores padrão
PARAM=${1:-default}

# Validação
if [ -z "$PARAM" ]; then
    echo "Erro: Parâmetro obrigatório"
    exit 1
fi
```

### Help Message

```bash
# Função de help
show_help() {
    echo "Usage: $0 [options]"
    echo ""
    echo "Options:"
    echo "  -h, --help     Show this help"
    echo "  -v, --version  Show version"
    exit 0
}

# Parse argumentos
while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            show_help
            ;;
        *)
            echo "Unknown option: $1"
            show_help
            ;;
    esac
    shift
done
```

## Exemplos

### server-restart.sh

```bash
#!/bin/bash
# Script: server-restart.sh
# Description: Restart application server
# Usage: ./server-restart.sh [dev|prod]
# Author: Claude
# Created: 2025-11-17

set -e

ENV=${1:-dev}

echo "🔄 Restarting server ($ENV)..."

if [ "$ENV" = "dev" ]; then
    sudo systemctl restart myapp-dev
elif [ "$ENV" = "prod" ]; then
    sudo systemctl restart myapp-prod
else
    echo "❌ Invalid environment: $ENV"
    exit 1
fi

echo "✅ Server restarted!"
```

## Boas Práticas

1. **Sempre use `set -e`** - Script para em caso de erro
2. **Valide inputs** - Evite erros silenciosos
3. **Mensagens claras** - Use emojis para status
4. **Help message** - Sempre inclua
5. **Testável** - Pode ser executado manualmente
6. **Idempotente** - Pode rodar múltiplas vezes sem problema

## Como Claude Usa

Claude **automaticamente descobre** scripts via skill `tool-inventory`:

1. Você: "Reinicie o servidor"
2. Claude ativa skill `tool-inventory`
3. Verifica: `ls .claude/scripts/bash/server-*.sh`
4. Encontra: `server-restart.sh`
5. Executa sem criar duplicata!

## Adicionar Novo Script

```bash
# 1. Criar script
nano .claude/scripts/bash/meu-script.sh

# 2. Adicionar header completo

# 3. Tornar executável
chmod +x .claude/scripts/bash/meu-script.sh

# 4. Testar
./claude/scripts/bash/meu-script.sh

# 5. Claude descobrirá automaticamente!
```
