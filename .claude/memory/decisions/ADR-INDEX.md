# 📐 Architecture Decision Records (ADRs) - Índice

> **Propósito:** Documentar TODAS as decisões arquiteturais e técnicas importantes do projeto.

---

## O Que São ADRs?

**Architecture Decision Records** documentam decisões técnicas importantes:
- **Contexto:** Por que precisamos decidir?
- **Decisão:** O que escolhemos?
- **Alternativas:** O que consideramos?
- **Consequências:** Impactos da decisão

**Benefícios:**
- 🧠 Memória institucional
- 🤔 Raciocínio documentado
- 🔄 Facilita onboarding
- ✅ Evita refazer decisões

---

## 📋 ADRs Registrados

| # | Data | Título | Status | Tags |
|---|------|--------|--------|------|
| 001 | 2025-11-17 | [Sistema de Memória Claude](#adr-001) | ✅ Aceito | #infra #claude |
| 002 | 2025-11-17 | [Arquitetura LLM-First Tools](#adr-002) | ✅ Aceito | #infra #claude #automation |
| 003 | 2025-11-17 | [Evolução Contínua do Template](#adr-003) | ✅ Aceito | #template #workflow |

---

## ADR-001: Sistema de Memória Claude

**Data:** 2025-11-17
**Status:** ✅ Aceito
**Decisores:** Anderson + Claude

### Contexto
Claude Code perdia contexto entre sessões, causando:
- Reexplicação constante de decisões
- Repetição de erros já resolvidos
- Perda de conhecimento acumulado
- Frustração e perda de tempo

### Decisão
Implementar sistema hierárquico de memória usando CLAUDE.md oficial:

```
CLAUDE.md (raiz)
.claude/memory/
  ├── context/      - Contexto permanente
  ├── decisions/    - ADRs
  ├── errors/       - Erros resolvidos
  ├── patterns/     - Padrões descobertos
  ├── commands/     - Histórico de comandos
  └── learnings/   - Aprendizados
```

### Alternativas Consideradas

1. **claude-mem (MCP + ChromaDB)**
   - ✅ Busca semântica
   - ✅ Escalável
   - ❌ Complexidade alta
   - ❌ Dependência externa
   - ❌ Setup não trivial

2. **Memory MCP (SQLite)**
   - ✅ Persistente
   - ✅ Estruturado
   - ❌ Requer MCP server
   - ❌ Configuração adicional

3. **CLAUDE.md nativo** ← **ESCOLHIDO**
   - ✅ Oficial Anthropic
   - ✅ Zero config
   - ✅ Simples e eficaz
   - ✅ Markdown legível
   - ✅ Git-friendly
   - ⚠️ Manual para atualizar

### Consequências

**Positivas:**
- ✅ Contexto persiste entre sessões
- ✅ Conhecimento acumulativo
- ✅ Erros documentados = não repetidos
- ✅ Onboarding mais rápido
- ✅ Decisões rastreáveis
- ✅ Zero overhead de setup

**Negativas:**
- ⚠️ Arquivos precisam ser mantidos
- ⚠️ Pode crescer muito (mitigation: modularizar)
- ⚠️ Busca é textual, não semântica

**Neutral:**
- 📝 Disciplina para documentar

### Implementação
- CLAUDE.md na raiz com @imports
- Estrutura em .claude/memory/
- Templates para ADRs e erros
- Docs em português/inglês conforme preferência

---

## ADR-002: Arquitetura LLM-First Tools (Híbrida Skills + MCPs)

**Data:** 2025-11-17
**Status:** ✅ Aceito e Evoluído
**Decisores:** Anderson + Claude

### Contexto

Claude estava criando scripts duplicados a cada sessão porque:
- Sem memória de ferramentas disponíveis
- Sem inventário de scripts existentes
- HD ficando cheio de scripts iguais
- Usuário precisava manualmente dizer "use o script X"
- Cada sessão = novos scripts para mesmas tarefas

**Problema crítico:** Falta de sistema de descoberta automática de ferramentas.

### Decisão

Implementar arquitetura LLM-First em 4 camadas:

**Camada 1: Skills (Auto-descoberta)**
- Local: `.claude/skills/`
- Claude descobre e usa automaticamente
- Baseado em descrições (model-driven)
- Skill essencial:
  - `tool-inventory/` - Lista ferramentas disponíveis

**Camada 2: Scripts Centralizados**
- Local: `.claude/scripts/`
- Organização por tipo: `bash/`, `python/`, `npm/`
- Nomenclatura padronizada: `verbo-substantivo.ext`
- Header obrigatório com documentação

**Camada 3: MCPs Oficiais (IMPLEMENTADO!)** ✨
- MCPs do Anthropic para integrações externas
- Tools nativos que Claude descobre automaticamente
- Mantidos pela comunidade oficial
- MCPs recomendados:
  - `github` - GitHub API (repos, PRs, issues, commits)
  - `filesystem` - Operações de arquivo avançadas
  - `git` - Operações git (log, diff, status, commit)

**Camada 4: Slash Commands (Existente)**
- Para operações que usuário quer controle direto
- Pode chamar Skills, MCPs ou scripts internamente

### Alternativas Consideradas

1. **Apenas Slash Commands**
   - ✅ Controle explícito
   - ❌ Usuário precisa lembrar de chamar
   - ❌ Não é LLM-first
   - ❌ Não resolve duplicação

2. **Apenas MCP Server**
   - ✅ Tools nativos para Claude
   - ❌ Requer configuração complexa
   - ❌ Overhead desnecessário para casos simples
   - ❌ Mais uma camada de abstração

3. **Skills + Scripts Centralizados** ← **ESCOLHIDO**
   - ✅ Descoberta automática
   - ✅ Zero duplicação
   - ✅ Simples de manter
   - ✅ Escalável
   - ✅ Git-friendly
   - ✅ LLM-first na essência

4. **Plugin System**
   - ✅ Distribuível
   - ❌ Complexidade muito alta
   - ❌ Overkill para uso interno
   - ❌ Harder to customize

### Consequências

**Positivas:**
- ✅ **Zero duplicação** - Claude verifica inventário antes de criar
- ✅ **Descoberta automática** - Skills auto-invocados + MCPs nativos
- ✅ **Memória persistente** - Scripts sobrevivem sessões
- ✅ **Centralização** - Um lugar para todos scripts
- ✅ **Escalável** - Fácil adicionar novos tools e MCPs
- ✅ **Manutenção** - Nomenclatura e docs padronizados
- ✅ **LLM-first** - Claude usa sem usuário pedir
- ✅ **HD limpo** - Sem acumulação de arquivos
- ✅ **Integrações nativas** - GitHub, Git, Filesystem via MCPs oficiais
- ✅ **Performance superior** - MCPs mais rápidos que bash scripts
- ✅ **Mantidos pela comunidade** - Atualizações automáticas via npm

**Negativas:**
- ⚠️ Skills precisam de descrições claras
- ⚠️ Scripts precisam de headers documentados
- ⚠️ Disciplina para seguir convenções

**Neutras:**
- 📝 MCP server opcional (95% dos casos não precisa)
- 📝 Skills complementam, não substituem slash commands

### Implementação

**Estrutura criada:**
```
.claude/
├── skills/
│   └── tool-inventory/SKILL.md
├── scripts/
│   ├── bash/
│   ├── python/
│   └── npm/
├── LLM_FIRST_TOOLS.md (documentação completa)
└── (raiz)
    └── .mcp.json (MCPs configurados)
```

**MCPs Instalados (.mcp.json):**
```json
{
  "mcpServers": {
    "github": "@modelcontextprotocol/server-github",
    "filesystem": "@modelcontextprotocol/server-filesystem",
    "git": "@modelcontextprotocol/server-git"
  }
}
```

**Checklist para novos scripts:**
- [ ] Verificar inventário primeiro
- [ ] Se existe, reutilizar
- [ ] Se não, criar em `.claude/scripts/[tipo]/`
- [ ] Header completo
- [ ] chmod +x
- [ ] Testar manualmente
- [ ] Documentar se resolver problema novo

### Padrões Estabelecidos

**Nomenclatura:**
```
verbo-substantivo.extensão
✅ server-restart.sh
✅ db-backup.sh
❌ restart.sh (genérico)
❌ script1.sh (não descritivo)
```

**Header obrigatório:**
```bash
#!/bin/bash
# Script: nome.sh
# Description: O que faz
# Usage: ./nome.sh [params]
# Author: Claude
# Created: YYYY-MM-DD
```

**Parameters:**
- Valores padrão: `VAR=${1:-default}`
- Validação de inputs
- Help message

### Quando Reavaliar

**Configurar MCP server se:**
- Volume de scripts > 20
- Necessidade de tools verdadeiramente nativos
- Integração com outras ferramentas MCP

**Criar novo Skill se:**
- Padrão de uso repetitivo identificado
- 3+ scripts relacionados a mesma área
- Oportunidade de automação clara

**Migrar para Plugin se:**
- Ferramentas úteis para comunidade
- Distribuição necessária
- Time > 5 pessoas

### Integração com Memória

Scripts documentados em:
- `.claude/memory/commands/COMMAND-HISTORY.md` - Se usar sudo
- `.claude/memory/errors/ERRORS-SOLVED.md` - Se resolver problema
- `.claude/memory/learnings/` - Descobertas importantes

### Métricas de Sucesso

**Antes:**
- 🔴 Scripts duplicados: ~10-20 por semana
- 🔴 HD uso: Crescimento descontrolado
- 🔴 Reuso: 0%
- 🔴 Claude awareness: Nenhuma

**Depois:**
- 🟢 Scripts duplicados: 0
- 🟢 HD uso: Controlado e organizado
- 🟢 Reuso: 100%
- 🟢 Claude awareness: Total

### Referência

Documentação completa: `.claude/LLM_FIRST_TOOLS.md`

---

## 📝 Template para Nova ADR

Copie quando fazer nova decisão arquitetural:

```markdown
## ADR-XXX: Título da Decisão

**Data:** YYYY-MM-DD
**Status:** 🔄 Proposto / ✅ Aceito / ❌ Rejeitado / 🗑️ Obsoleto

### Contexto
Por que precisamos decidir?

### Decisão
O que escolhemos?

### Alternativas Consideradas
1. Opção A
   - Prós
   - Contras
2. Opção B
   - Prós
   - Contras

### Consequências
**Positivas:**
- Item

**Negativas:**
- Item

**Neutras:**
- Item

### Implementação
Como será implementado?

### Quando Reavaliar
Em que condições revisitar esta decisão?
```

---

## ADR-003: Evolução Contínua do Template

**Data:** 2025-11-17
**Status:** ✅ Aceito e CRÍTICO
**Decisores:** Anderson + Claude

### Contexto

Este é um template destinado a ser reutilizado em múltiplos projetos futuros.

**Problema:** Como garantir que o template evolua com as descobertas dos projetos que o utilizam?

**Risco:** Template ficar desatualizado, perdendo valor ao longo do tempo.

### Decisão

**Projetos que usam este template devem sincronizar melhorias genéricas de volta para o template.**

**Workflow de Sincronização:**

Quando um projeto descobrir/criar algo genérico e reutilizável:
1. Aplicar no projeto específico
2. Identificar se é genérico o suficiente
3. Se SIM: Copiar de volta para este template
4. Commitar e push
5. Documentar em sync-log.md

**Critérios para Sincronizar:**

**✅ SINCRONIZAR:**
- Skills genéricos (úteis para qualquer projeto)
- Scripts bash/python reutilizáveis
- Melhorias em protocolos (AUTO-LEARNING, THINKING-MODE)
- ADRs de arquitetura geral
- Patterns de código universal
- Melhorias em LLM_FIRST_TOOLS.md
- Novos MCPs úteis
- Descobertas sobre Git workflow

**❌ NÃO SINCRONIZAR:**
- Código específico de domínio/negócio
- Scripts de servidores específicos
- ADRs de decisões de negócio
- Contexto de projeto específico
- Erros específicos de tecnologia/framework

### Consequências

**Positivas:**
- ✅ Template evolui continuamente
- ✅ Conhecimento acumulativo entre projetos
- ✅ Novos projetos herdam todas as melhorias
- ✅ Economia de tempo exponencial
- ✅ Cada projeto melhora o template (efeito composto)

**Negativas:**
- ⚠️ Requer disciplina para sincronizar
- ⚠️ Risco de sincronizar código específico por engano

### Implementação

**Checklist para Claude ao criar algo:**

```
[ ] É genérico ou específico do projeto?
[ ] Útil para qualquer projeto ou só este?
[ ] Se GENÉRICO:
    [ ] Copiar para template Claude-especial
    [ ] Remover partes específicas
    [ ] Testar se faz sentido genérico
    [ ] Commitar no template
    [ ] Documentar em sync-log.md
[ ] Se ESPECÍFICO:
    [ ] Apenas commitar no projeto
```

**Tracking:** Ver `.claude/memory/learnings/sync-log.md`

### Exemplos

**✅ Deve Sincronizar:**
- Novo skill para backup automático
- Melhoria no AUTO-LEARNING-PROTOCOL
- Script bash genérico para health checks
- Pattern de retry em APIs
- ADR sobre estratégia de testes

**❌ Não Deve Sincronizar:**
- Módulo específico de e-commerce
- Script de deploy para servidor X
- Integração com API específica de negócio
- ADR sobre escolha de fornecedor

### Referência

- **sync-log.md:** Histórico de sincronizações
- **GitHub:** Template sempre atualizado

---

## 📊 Estatísticas

**Total de ADRs:** 3
**Aceitos:** 3
**Propostos:** 0
**Rejeitados:** 0
**Obsoletos:** 0

---

**Última atualização:** 2025-11-17
**Próxima revisão:** Sempre que nova decisão arquitetural for tomada
