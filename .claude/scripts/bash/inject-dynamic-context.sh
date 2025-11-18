#!/bin/bash
# Script: inject-dynamic-context.sh
# Description: Injeta contexto dinâmico em CADA interação com Claude
# Usage: Executado automaticamente pelo UserPromptSubmit hook
# Author: Claude
# Created: 2025-11-17
# ADR: ADR-008 (Sistema Avançado de Gestão de Contexto)

set -e  # Exit on error

# ================================
# Configuration
# ================================

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"

# ================================
# Gather Dynamic Context
# ================================

# Git branch atual
BRANCH=$(git branch --show-current 2>/dev/null || echo "unknown")

# Último commit
LAST_COMMIT=$(git log -1 --oneline 2>/dev/null || echo "none")

# Arquivos modificados
CHANGES_COUNT=$(git status --short 2>/dev/null | wc -l | tr -d ' ')

# Staged vs unstaged
STAGED=$(git diff --cached --name-only 2>/dev/null | wc -l | tr -d ' ')
UNSTAGED=$(git diff --name-only 2>/dev/null | wc -l | tr -d ' ')
UNTRACKED=$(git ls-files --others --exclude-standard 2>/dev/null | wc -l | tr -d ' ')

# Projeto atual
PROJECT_NAME=$(basename "$PROJECT_ROOT")

# Última sincronização com template
LAST_SYNC=$(grep -m 1 "Última sincronização:" "$PROJECT_ROOT/.claude/memory/learnings/sync-log.md" 2>/dev/null | cut -d: -f2- || echo "desconhecida")

# ================================
# Output Context (vai para additionalContext do Claude)
# ================================

cat << EOF

---
📍 **Contexto Atual (Auto-injetado)**

**Git:**
- Branch: \`$BRANCH\`
- Último commit: $LAST_COMMIT
- Mudanças: $CHANGES_COUNT arquivos ($STAGED staged, $UNSTAGED unstaged, $UNTRACKED untracked)

**Projeto:**
- Nome: $PROJECT_NAME
- Path: $PROJECT_ROOT
- Template: Claude-especial (LLM-First)

**Sincronização:**
- Última sync:$LAST_SYNC

**Performance:**
- Paralelizar sempre! (ADR-007 se existir)

**Lembretes:**
- ADR-003: Melhorias genéricas → sincronizar com template
- ADR-007: Tool calls paralelos em UMA mensagem (se existir)
- ADR-008: Hooks garantem contexto persistente (se existir)

---

EOF
