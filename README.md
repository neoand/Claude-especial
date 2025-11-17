# 🤖 Claude-especial - Template LLM-First

> **Template Universal para Projetos com Claude Code**
> Crie projetos com inteligência artificial integrada desde o dia 1!

---

## 🎯 O Que É?

Template/boilerplate para iniciar **qualquer projeto** com filosofia **LLM-First**, onde Claude atua como:
- 🧠 **Senior Engineer** com memória permanente
- 🔧 **Ferramenteiro** que descobre e reutiliza scripts automaticamente
- 📚 **Documentador** que aprende e registra tudo
- 🚀 **Automador** que integra GitHub, Git, e muito mais

**Zero duplicação. Máxima automação. Conhecimento acumulativo.**

---

## ⚡ Quick Start

### 1. Clone este template para seu novo projeto

```bash
git clone https://github.com/neoand/Claude-especial.git meu-novo-projeto
cd meu-novo-projeto
rm -rf .git  # Remove git do template
```

### 2. Execute o setup

```bash
./setup.sh
```

### 3. Pronto! 🎉

Você agora tem:
- ✅ Sistema de memória permanente
- ✅ Skills auto-descobertos
- ✅ MCPs integrados (GitHub, Git, Filesystem)
- ✅ Git configurado anti-rebase
- ✅ Scripts centralizados
- ✅ Protocolos de aprendizado automático

---

## 🏗️ O Que Vem Incluso

### 📂 Estrutura Completa

```
Claude-especial/
├── .claude/
│   ├── skills/                    # Skills auto-descobertos
│   │   └── tool-inventory/        # Verifica scripts antes de criar novos
│   ├── scripts/                   # Scripts centralizados
│   │   ├── bash/
│   │   ├── python/
│   │   └── npm/
│   ├── memory/                    # Memória permanente
│   │   ├── context/               # Contexto do projeto
│   │   ├── decisions/             # ADRs (Architecture Decision Records)
│   │   ├── errors/                # Erros resolvidos
│   │   ├── patterns/              # Padrões descobertos
│   │   ├── commands/              # Histórico de comandos sudo
│   │   └── learnings/             # Aprendizados gerais
│   ├── LLM_FIRST_TOOLS.md         # Documentação completa do sistema
│   ├── AUTO-LEARNING-PROTOCOL.md  # Protocolo de aprendizado
│   └── THINKING-MODE-PROTOCOL.md  # Quando ativar thinking mode
├── .mcp.json                      # MCPs pré-configurados
├── .gitignore                     # Universal gitignore
├── CLAUDE.md                      # Brain principal (auto-loaded)
├── setup.sh                       # Script de inicialização
└── README.md                      # Este arquivo
```

### 🧠 Sistema de Memória

- **CLAUDE.md**: Auto-loaded em todas sessões
- **ADRs**: Decisões arquiteturais documentadas
- **Error Tracking**: Erros nunca se repetem
- **Pattern Library**: Padrões descobertos e reutilizados
- **Command History**: Comandos sudo documentados

### 🛠️ Skills Inclusos

#### `tool-inventory`
Auto-verifica scripts existentes antes de criar novos.
**Zero duplicação garantida!**

### 🔌 MCPs Pré-Configurados

- **GitHub** - Repos, PRs, Issues, Commits
- **Git** - Status, Diff, Log, Commit, Branch
- **Filesystem** - Navegação avançada de arquivos

### 📖 Protocolos

#### Auto-Learning Protocol
Claude aprende automaticamente:
- ✅ Erros resolvidos → Documentados
- ✅ Comandos sudo → Salvos
- ✅ Padrões descobertos → Registrados
- ✅ Decisões técnicas → ADRs criados

#### Thinking Mode Protocol
Claude ativa thinking mode automaticamente quando:
- 🧠 Aprendendo algo novo
- 🧠 Salvando na memória
- 🧠 Tomando decisão arquitetural

---

## 🎨 Casos de Uso

### Para Qualquer Projeto

Este template funciona para:

- ✅ **Web Apps** (React, Vue, Angular)
- ✅ **Backend** (Node.js, Python, Go, Rust)
- ✅ **Mobile** (React Native, Flutter)
- ✅ **Data Science** (Jupyter, Python)
- ✅ **DevOps** (Terraform, Kubernetes)
- ✅ **CLI Tools** (Bash, Python)
- ✅ **Odoo** (ERP customizations)
- ✅ **Qualquer linguagem/framework!**

**Filosofia:** Scripts e skills são genéricos. Você adiciona os específicos do seu projeto.

---

## 📚 Como Usar

### Adicionar Novo Script

1. Claude verifica inventário automaticamente
2. Se não existir, cria em `.claude/scripts/[tipo]/`
3. Próxima vez: reutiliza!

**Você não faz nada. Claude gerencia.**

### Adicionar Novo Skill

```bash
# Criar pasta
mkdir .claude/skills/meu-skill

# Criar SKILL.md com frontmatter
cat > .claude/skills/meu-skill/SKILL.md << 'EOF'
---
name: meu-skill
description: Descrição clara do que faz e quando usar
---

# Instruções detalhadas para Claude
EOF
```

### Adicionar Novo MCP

```bash
claude mcp add --transport stdio --scope project <name> -- npx -y @modelcontextprotocol/server-<name>
```

### Documentar Decisão Arquitetural

Claude faz automaticamente, mas você pode também:
1. Editar `.claude/memory/decisions/ADR-INDEX.md`
2. Copiar template de ADR
3. Preencher contexto, decisão, alternativas, consequências

---

## 🔧 Configuração Git Anti-Rebase

Git já vem configurado para workflow simples:

```bash
pull.rebase = false      # NUNCA rebase
merge.ff = false         # SEMPRE merge commit
push.default = simple    # Push apenas branch atual
```

**Sem rebase. Sem travamento. Sem dor de cabeça.**

---

## 🚀 Workflows Automáticos

### Exemplo 1: Desenvolvimento Normal

```
Você: "Adicione autenticação JWT"

Claude:
1. Skill tool-inventory → Verifica scripts auth
2. Cria implementação
3. MCP Git → Verifica mudanças
4. MCP Git → Cria commit
5. MCP GitHub → Cria PR (se solicitado)
✅ Pronto!
```

### Exemplo 2: Deploy

```
Você: "Faça deploy para produção"

Claude:
1. Skill tool-inventory → Encontra script deploy
2. Executa deploy
3. MCP Git → Commit das mudanças
4. MCP GitHub → Atualiza issue/PR
5. Skill health-check → Verifica servidor
✅ Deploy completo!
```

---

## 📖 Documentação Completa

Depois de clonar, leia:

1. **CLAUDE.md** - Brain principal
2. **.claude/LLM_FIRST_TOOLS.md** - Sistema completo
3. **.claude/memory/decisions/ADR-INDEX.md** - Decisões base

---

## 🎓 Filosofia

### Princípios

1. **LLM-First** - Claude descobre e usa, você não gerencia
2. **Zero Duplicação** - Inventário sempre verificado
3. **Memória Permanente** - Conhecimento sobrevive sessões
4. **Aprendizado Automático** - Erros viram documentação
5. **Git Simples** - Merge > Rebase (sempre)

### Anti-Padrões Evitados

- ❌ Scripts duplicados espalhados
- ❌ Perda de contexto entre sessões
- ❌ Repetição de erros resolvidos
- ❌ Git rebase travando projeto
- ❌ Usuário tendo que lembrar ferramentas

---

## 🔍 Troubleshooting

### Claude não encontra scripts

```bash
# Verificar structure
ls -la .claude/skills/
ls -la .claude/scripts/

# Verificar SKILL.md tem frontmatter correto
cat .claude/skills/tool-inventory/SKILL.md
```

### MCPs não funcionam

```bash
# Listar MCPs instalados
claude mcp list

# Ver configuração
cat .mcp.json

# Reinstalar
claude mcp remove <name>
claude mcp add --transport stdio --scope project <name> -- npx -y @modelcontextprotocol/server-<name>
```

### Git está fazendo rebase

```bash
# Verificar configs
git config pull.rebase    # Deve ser: false
git config merge.ff       # Deve ser: false

# Reconfigurar
./setup.sh
```

---

## 🤝 Contribuindo

Este é um template privado para projetos pessoais, mas se tiver melhorias:

1. Fork (se tornar público)
2. Crie branch: `git checkout -b feature/melhoria`
3. Commit: `git commit -m "feat: descrição"`
4. Push: `git push origin feature/melhoria`
5. Abra PR

---

## 📊 Comparação

### Antes (Projeto Normal)

```
❌ Claude esquece contexto
❌ Scripts duplicados
❌ Erros repetidos
❌ Git complexo
❌ Integração manual
```

### Depois (Com Claude-especial)

```
✅ Memória permanente
✅ Zero duplicação
✅ Erros documentados
✅ Git simples
✅ Automação nativa
```

---

## 🎯 Próximos Passos

Depois de configurar:

1. **Personalize** `.claude/memory/context/projeto.md` com seu projeto
2. **Adicione** scripts específicos do seu domínio
3. **Crie** skills personalizados conforme necessário
4. **Documente** decisões importantes em ADRs
5. **Use** Claude normalmente - ele faz o resto!

---

## 📞 Suporte

- **Documentação**: Ver `.claude/LLM_FIRST_TOOLS.md`
- **ADRs**: Ver `.claude/memory/decisions/ADR-INDEX.md`
- **Issues**: (Abra issue se houver problema)

---

## 📜 Licença

Privado - Uso pessoal

---

## ✨ Créditos

**Desenvolvido por:** Anderson + Claude
**Data:** 2025-11-17
**Versão:** 1.0

**Baseado em:**
- [Claude Code](https://claude.com/claude-code) - Anthropic
- [Architecture Decision Records](https://adr.github.io/)
- [Model Context Protocol](https://modelcontextprotocol.io/)

---

**🚀 Comece agora e tenha IA trabalhando para você desde o commit 1!**
