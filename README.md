# 🤖 Claude-especial - Template LLM-First

> **Template Universal para Projetos com Claude Code**
> Crie projetos com inteligência artificial integrada desde o dia 1!

[![ADRs](https://img.shields.io/badge/ADRs-5-blue)](.claude/memory/decisions/ADR-INDEX.md)
[![Hooks](https://img.shields.io/badge/Hooks-3-green)](.claude/hooks.yaml)
[![Performance](https://img.shields.io/badge/Performance-20x-orange)](https://claude.ai/max)
[![Windows](https://img.shields.io/badge/Windows-WSL2-blue)](#-setup-windows-wsl2)

---

## 🎯 O Que É?

Template/boilerplate para iniciar **qualquer projeto** com filosofia **LLM-First**, onde Claude atua como:
- 🧠 **Senior Engineer** com memória permanente
- 🔧 **Ferramenteiro** que descobre e reutiliza scripts automaticamente
- 📚 **Documentador** que aprende e registra tudo
- 🚀 **Automador** que integra GitHub, Git, e muito mais
- 🔄 **Auto-educador** que NUNCA perde contexto (hooks inteligentes!)

**Zero duplicação. Máxima automação. Conhecimento acumulativo. Contexto perpétuo.**

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
- ✅ **Hooks inteligentes** - Zero perda de contexto (ADR-008) 🔥
- ✅ **Performance 5-10x mais rápida** - Paralelização agressiva (ADR-007) ⚡
- ✅ Skills auto-descobertos
- ✅ MCPs integrados (GitHub, Git, Filesystem)
- ✅ Git configurado anti-rebase
- ✅ Scripts centralizados
- ✅ Protocolos de aprendizado automático

### 4. Windows? Use WSL2! 🪟

**Claude Code requer ambiente Linux.** Windows users: [Ver setup WSL2](#-setup-windows-wsl2)

---

## 🏗️ O Que Vem Incluso

### 📂 Estrutura Completa

```
Claude-especial/
├── .claude/
│   ├── hooks.yaml                 # 🔥 NOVO! Hooks inteligentes
│   ├── skills/                    # Skills auto-descobertos
│   │   └── tool-inventory/        # Verifica scripts antes de criar novos
│   ├── scripts/                   # Scripts centralizados
│   │   ├── bash/
│   │   │   ├── pre-compact-save-context.sh    # 🔥 NOVO! Salva contexto
│   │   │   └── inject-dynamic-context.sh      # 🔥 NOVO! Injeta contexto
│   │   ├── python/
│   │   └── npm/
│   ├── memory/                    # Memória permanente
│   │   ├── context/               # Contexto do projeto
│   │   ├── context-snapshots/     # 🔥 NOVO! Backups automáticos
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

## 🪟 Setup Windows (WSL2)

### Por que WSL2?

Claude Code + hooks + scripts bash = **ambiente Linux obrigatório**.

Windows não possui:
- Bash nativo
- Permissões Unix
- Hooks funcionais
- Performance otimizada para MCPs

**Solução:** WSL2 = Linux completo rodando no Windows!

### Instalação WSL2 (Quick)

```powershell
# PowerShell como Administrador
wsl --install

# Reiniciar Windows
# Abrir "Ubuntu" no menu Iniciar
# Configurar usuário/senha
```

### Instalação WSL2 (Manual)

1. **Habilitar WSL** (PowerShell como Admin):
```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

2. **Reiniciar Windows**

3. **Definir WSL2**:
```powershell
wsl --set-default-version 2
```

4. **Instalar Ubuntu** (Microsoft Store):
   - Buscar "Ubuntu 22.04 LTS"
   - Instalar
   - Configurar usuário/senha

### Setup Ambiente Linux (WSL2)

```bash
# 1. Atualizar
sudo apt update && sudo apt upgrade -y

# 2. Git
sudo apt install git -y

# 3. Node.js 20 (via nvm)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.bashrc
nvm install 20
nvm use 20

# 4. Claude Code CLI
npm install -g @anthropic/claude-code

# 5. Clonar template
cd ~
git clone https://github.com/neoand/Claude-especial.git meu-projeto
cd meu-projeto
rm -rf .git

# 6. Setup
./setup.sh

# 7. Configurar Git
git init
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"

# 8. Iniciar Claude
claude
```

### Dicas WSL2

**Arquivos Windows → WSL2:**
```bash
# Windows C:\ = /mnt/c/ no WSL
cd /mnt/c/Users/SeuUsuario/Documents

# Copiar para WSL (mais rápido):
cp -r /mnt/c/Users/SeuUsuario/projeto ~/
```

**VS Code + WSL2:**
1. Instalar extensão "Remote - WSL"
2. `F1` → "WSL: Connect to WSL"
3. Abrir pasta no WSL

**Performance:**
- Trabalhar em `~/` (Linux) = **rápido**
- Trabalhar em `/mnt/c/` (Windows) = lento

### Troubleshooting Windows

**`bash: command not found`**
→ Você está no PowerShell. Abrir "Ubuntu" no menu Iniciar.

**Hooks não funcionam**
→ `chmod +x .claude/scripts/bash/*.sh`

**MCPs não encontrados**
→ `npm list -g | grep modelcontextprotocol`

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

## 🌟 Novidades (2025-11-17)

### ADR-008: Sistema Avançado de Contexto (REVOLUCIONÁRIO!)

**3 Hooks Inteligentes implementados:**

1. **PreCompact Hook** - Salva contexto ANTES de auto-compact
   - ADRs recentes
   - Commits
   - TODOs ativos
   - Status do projeto

2. **SessionStart Hook** - Re-educação automática APÓS compact
   - Lê snapshot salvo
   - Restaura contexto crítico
   - Continue de onde parou!

3. **UserPromptSubmit Hook** - Contexto dinâmico SEMPRE
   - Branch git atual
   - Arquivos modificados
   - Último commit
   - Lembretes importantes

**Resultado:** ZERO perda de contexto entre sessões!

### ADR-007: Performance 5-10x Mais Rápida

- ⚡ Tool calls paralelos
- 🔀 Bash paralelo (`&` e `wait`)
- 🌳 Git worktrees para multi-tasking
- 🤖 Headless mode para automação

**Resultado:** Operações 5-10x mais rápidas!

### Descobertas Além das Expectativas

- ✅ **Checkpointing** - Todo prompt cria checkpoint (`/rewind`)
- ✅ **Plugin System** - Criar plugins distribuíveis
- ✅ **Plan Mode** - Análise read-only segura
- ✅ **Headless + JSON** - Claude como API
- ✅ **Custom MCPs** - Criar seus próprios MCPs

---

## 🎯 Próximos Passos

Depois de configurar:

1. **Personalize** `.claude/memory/context/projeto.md` com seu projeto
2. **Adicione** scripts específicos do seu domínio
3. **Crie** skills personalizados conforme necessário
4. **Documente** decisões importantes em ADRs
5. **Use** Claude normalmente - ele faz o resto!
6. **Aproveite** hooks automáticos - contexto perpétuo garantido!

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
