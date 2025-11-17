# 🧠 Memória do Projeto - [NOME DO SEU PROJETO]

> **IMPORTANTE**: Este arquivo é carregado AUTOMATICAMENTE em TODAS as sessões do Claude Code.
> Contém contexto permanente, decisões, padrões e conhecimento acumulado.

---

## 🎯 Contexto do Projeto

**Nome:** [Preencha com nome do projeto]
**Tipo:** [Web App / Backend / Mobile / CLI / etc]
**Ambiente:** [Development / Testing / Production]
**Linguagem:** [Python / JavaScript / TypeScript / Go / etc]
**Framework:** [React / Django / Express / etc]

**Descrição:**
[Descreva brevemente o que o projeto faz]

**Módulos Principais:**
- [Módulo 1] - [Descrição]
- [Módulo 2] - [Descrição]

**Database:** [PostgreSQL / MySQL / MongoDB / etc]

---

## 📋 Importações de Contexto

@.claude/memory/context/projeto.md
@.claude/memory/decisions/ADR-INDEX.md
@.claude/memory/errors/ERRORS-SOLVED.md
@.claude/memory/patterns/PATTERNS.md
@.claude/memory/commands/COMMAND-HISTORY.md
@.claude/memory/learnings/git-workflow.md
@.claude/memory/AUTO-LEARNING-PROTOCOL.md
@.claude/memory/THINKING-MODE-PROTOCOL.md

---

## 🧠 PROTOCOLO DE AUTO-APRENDIZADO (CRÍTICO!)

### Regras Fundamentais

**❌ NUNCA:**
- Assumir ou deduzir sem verificar
- Repetir comando que falhou sem modificação
- Executar sem checar histórico primeiro
- Esquecer de documentar erro resolvido
- Criar script novo sem verificar inventário (`.claude/scripts/`)

**✅ SEMPRE:**
1. **ANTES de executar comando:** Verificar `COMMAND-HISTORY.md`
2. **Se comando falhar:** Documentar IMEDIATAMENTE em `ERRORS-SOLVED.md`
3. **Se usar sudo:** Salvar regra em `COMMAND-HISTORY.md`
4. **Se pesquisar:** Salvar resultado em `learnings/`
5. **Se incerto:** Pesquisar docs oficiais, NUNCA assumir
6. **QUANDO APRENDER ALGO:** Ativar thinking mode, raciocinar profundamente, salvar "na rocha"
7. **ANTES de criar script:** Verificar `.claude/scripts/` via skill `tool-inventory`, reutilizar se existir

### Checklist de Execução

Antes de QUALQUER ação:

```
[ ] Li ERRORS-SOLVED.md?
[ ] Li COMMAND-HISTORY.md?
[ ] Verifiquei se script/tool existe?
[ ] Comando é seguro?
[ ] Tenho certeza ou preciso pesquisar?
```

Depois de resolver problema:

```
[ ] Erro documentado em ERRORS-SOLVED.md?
[ ] Comando sudo salvo em COMMAND-HISTORY.md?
[ ] Pattern salvo em PATTERNS.md?
[ ] Decisão arquitetural → ADR criado?
```

---

## 🤖 LLM-First Tools System

### Sistema Híbrido (Skills + MCPs)

**Skills Ativos:**
- `tool-inventory` - Verifica scripts antes de criar novos (AUTO-INVOCADO)

**MCPs Instalados:**
- `github` - GitHub API (repos, PRs, issues)
- `git` - Git operations (status, diff, commit)
- `filesystem` - Advanced file operations

**Scripts Centralizados:**
- Localização: `.claude/scripts/{bash,python,npm}/`
- Nomenclatura: `verbo-substantivo.extensão`
- Header obrigatório: Sim
- Documentação completa: `.claude/LLM_FIRST_TOOLS.md`

**Regra de Ouro:**
> **SEMPRE** verificar inventário via skill `tool-inventory` ANTES de criar novo script!

---

## 📚 Contexto Específico do Projeto

### Stack Tecnológico

**Backend:**
- [Framework e versão]
- [Bibliotecas principais]

**Frontend:**
- [Framework e versão]
- [Bibliotecas principais]

**Infraestrutura:**
- [Servidor / Cloud provider]
- [CI/CD]
- [Monitoring]

### Ambientes

**Development:**
- [URL/IP]
- [Acesso]

**Testing/Staging:**
- [URL/IP]
- [Acesso]

**Production:**
- [URL/IP]
- [Acesso]

### Serviços Externos

- [API 1] - [Propósito]
- [API 2] - [Propósito]

---

## 🚨 Problemas Conhecidos e Soluções

### [Nome do Problema 1]

**Sintoma:**
[Descrever]

**Solução:**
[Comando ou passo a passo]

**Referência:** `.claude/memory/errors/ERRORS-SOLVED.md#erro-xxx`

---

## 🎯 Padrões e Convenções

### Código

- **Estilo:** [PEP8 / Airbnb / Google / etc]
- **Linting:** [ESLint / Pylint / etc]
- **Formatação:** [Prettier / Black / etc]

### Git

- **Commits:** [Conventional Commits](https://www.conventionalcommits.org/)
- **Branches:** `feature/`, `fix/`, `refactor/`
- **Workflow:** Merge (NUNCA rebase)

### Documentação

- **Inline:** JSDoc / Docstrings
- **API:** OpenAPI / Swagger
- **Arquitetura:** ADRs em `.claude/memory/decisions/`

---

## 🔐 Segurança e Credenciais

### NUNCA commitar:

- ❌ `.env`, `.env.*`
- ❌ `credentials.json`, `secrets.json`
- ❌ `*.pem`, `*.key`, `*.p12`
- ❌ API keys, tokens, senhas

### Verificar `.gitignore` sempre!

**Localização:** Raiz do projeto
**Template:** Já incluso no Claude-especial

---

## 📊 Métricas e Monitoramento

### Performance

- [Métrica 1]: [Objetivo]
- [Métrica 2]: [Objetivo]

### Qualidade

- **Cobertura de testes:** [Objetivo %]
- **Code quality:** [Tool e score]
- **Vulnerabilidades:** [Tool e score]

---

## 🔗 Links Importantes

- **Repositório:** [GitHub URL]
- **Documentação:** [URL]
- **CI/CD:** [URL]
- **Monitoring:** [URL]
- **Wiki:** [URL]

---

## 📝 Notas de Sessão

### Última sessão: [Data]

**Trabalhado:**
- [Item 1]
- [Item 2]

**Próximos passos:**
- [ ] [Task 1]
- [ ] [Task 2]

**Bloqueios:**
- [Se houver]

---

## 🎓 Aprendizados Recentes

Ver: `.claude/memory/learnings/`

**Últimos 5:**
1. [Aprendizado 1] - [Data]
2. [Aprendizado 2] - [Data]
3. [Aprendizado 3] - [Data]
4. [Aprendizado 4] - [Data]
5. [Aprendizado 5] - [Data]

---

## ⚡ Quick Commands

```bash
# [Comando útil 1]
[comando]

# [Comando útil 2]
[comando]

# Ver scripts disponíveis
ls -la .claude/scripts/bash/

# Ver MCPs instalados
claude mcp list
```

---

**Última atualização:** [Data]
**Próxima revisão:** [Quando revisar]
