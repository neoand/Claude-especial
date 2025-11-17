#!/bin/bash
# Script: setup.sh
# Description: Setup inicial para projetos com Claude-especial template
# Usage: ./setup.sh
# Author: Claude + Anderson
# Created: 2025-11-17

set -e  # Exit on error

echo "🤖 Claude-especial - Setup Inicial"
echo "=================================="
echo ""

# Obter o diretório do projeto
PROJECT_DIR="$(pwd)"
PROJECT_NAME="$(basename "$PROJECT_DIR")"

echo "📂 Projeto: $PROJECT_NAME"
echo "📍 Localização: $PROJECT_DIR"
echo ""

# Passo 1: Renomear templates
echo "1️⃣  Renomeando templates..."

if [ -f ".claude/memory/context/projeto.md.template" ]; then
    mv .claude/memory/context/projeto.md.template .claude/memory/context/projeto.md
    echo "   ✅ projeto.md criado"
fi

if [ -f ".claude/memory/errors/ERRORS-SOLVED.md.template" ]; then
    mv .claude/memory/errors/ERRORS-SOLVED.md.template .claude/memory/errors/ERRORS-SOLVED.md
    echo "   ✅ ERRORS-SOLVED.md criado"
fi

if [ -f ".claude/memory/patterns/PATTERNS.md.template" ]; then
    mv .claude/memory/patterns/PATTERNS.md.template .claude/memory/patterns/PATTERNS.md
    echo "   ✅ PATTERNS.md criado"
fi

if [ -f ".claude/memory/commands/COMMAND-HISTORY.md.template" ]; then
    mv .claude/memory/commands/COMMAND-HISTORY.md.template .claude/memory/commands/COMMAND-HISTORY.md
    echo "   ✅ COMMAND-HISTORY.md criado"
fi

echo ""

# Passo 2: Substituir placeholders em .mcp.json
echo "2️⃣  Configurando MCPs..."

if [ -f ".mcp.json" ]; then
    # Substituir {{PROJECT_PATH}} pelo path real
    sed -i.bak "s|{{PROJECT_PATH}}|$PROJECT_DIR|g" .mcp.json
    rm .mcp.json.bak 2>/dev/null || true
    echo "   ✅ .mcp.json configurado com path: $PROJECT_DIR"
fi

echo ""

# Passo 3: Atualizar CLAUDE.md com nome do projeto
echo "3️⃣  Personalizando CLAUDE.md..."

if [ -f "CLAUDE.md" ]; then
    sed -i.bak "s|\[NOME DO SEU PROJETO\]|$PROJECT_NAME|g" CLAUDE.md
    sed -i.bak "s|\[Preencha com nome do projeto\]|$PROJECT_NAME|g" CLAUDE.md
    rm CLAUDE.md.bak 2>/dev/null || true
    echo "   ✅ CLAUDE.md atualizado com: $PROJECT_NAME"
fi

echo ""

# Passo 4: Configurar Git
echo "4️⃣  Configurando Git (anti-rebase)..."

if [ ! -d ".git" ]; then
    git init
    echo "   ✅ Git inicializado"
fi

# Configurações anti-rebase
git config pull.rebase false
git config merge.ff false
git config push.default simple
git config core.autocrlf input

# Performance
git config core.preloadindex true
git config core.fscache true
git config gc.auto 256
git config pack.threads 0

echo "   ✅ Git configurado (merge-only, no rebase)"
echo ""

# Passo 5: Dar permissão aos scripts
echo "5️⃣  Configurando permissões de scripts..."

find .claude/scripts/bash -type f -name "*.sh" -exec chmod +x {} \; 2>/dev/null || true
find .claude/scripts/python -type f -name "*.py" -exec chmod +x {} \; 2>/dev/null || true

echo "   ✅ Permissões configuradas"
echo ""

# Passo 6: Verificar Node.js/npm (para MCPs)
echo "6️⃣  Verificando dependências..."

if command -v node &> /dev/null; then
    NODE_VERSION=$(node --version)
    echo "   ✅ Node.js: $NODE_VERSION"
else
    echo "   ⚠️  Node.js não encontrado (necessário para MCPs)"
    echo "      Instale: https://nodejs.org/"
fi

if command -v npm &> /dev/null; then
    NPM_VERSION=$(npm --version)
    echo "   ✅ npm: $NPM_VERSION"
else
    echo "   ⚠️  npm não encontrado"
fi

echo ""

# Passo 7: Instruções finais
echo "=================================="
echo "✨ Setup Completo!"
echo "=================================="
echo ""
echo "📋 Próximos Passos:"
echo ""
echo "1. Edite .claude/memory/context/projeto.md com informações do seu projeto"
echo "2. Personalize CLAUDE.md conforme necessário"
echo "3. Adicione seu repositório remoto:"
echo "   git remote add origin https://github.com/seu-usuario/seu-repo.git"
echo ""
echo "4. Faça o primeiro commit:"
echo "   git add ."
echo "   git commit -m \"chore: initial commit with Claude-especial template\""
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "5. Comece a usar Claude Code!"
echo "   - Claude descobrirá automaticamente skills e MCPs"
echo "   - Scripts criados em .claude/scripts/ serão reutilizados"
echo "   - Memória persistirá entre sessões"
echo ""
echo "📚 Documentação:"
echo "   - README.md - Visão geral do template"
echo "   - .claude/LLM_FIRST_TOOLS.md - Sistema completo"
echo "   - .claude/memory/decisions/ADR-INDEX.md - Decisões base"
echo ""
echo "🚀 Você está pronto para começar!"
echo ""
