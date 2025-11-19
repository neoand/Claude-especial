# 🎨 Padrões de Projeto - Biblioteca de Soluções

> **Propósito:** Registrar padrões de código, arquitetura e soluções reutilizáveis.

---

## 📋 Índice de Padrões

| ID | Nome | Categoria | Uso |
|----|------|-----------|-----|
| P001 | [UI Autopopulação onchange](#p001-ui-autopopulation-onchange) | UI/UX | Formulários responsivos |

---

## P001: UI Autopopulação onchange

**Categoria:** UI/UX
**Quando Usar:** Para preencher automaticamente campos baseados em seleção do usuário em tempo real
**Evitar Quando:** Cálculos complexos que precisam persistir em lote

### Problema
Usuários precisam preencher manualmente campos que podem ser derivados de outras seleções, causando:
- Trabalho redundante
- Erros de digitação
- Experiência pobre do usuário

### Solução
Usar `@api.onchange` para autopopulação responsiva de campos relacionados

```python
@api.onchange('related_field')
def _onchange_related_field(self):
    """Auto-populate field when related field is selected"""
    if self.related_field:
        # Prioridade: campo1 > campo2 > vazio
        if self.related_field.field1:
            self.target_field = self.related_field.field1
        elif self.related_field.field2:
            self.target_field = self.related_field.field2
        else:
            self.target_field = False
    else:
        self.target_field = False
```

### Benefícios
- ✅ Resposta imediata na UI
- ✅ Melhor experiência do usuário
- ✅ Reduz erros de digitação
- ✅ Não gera queries desnecessárias ao carregar
- ✅ Lógica simples e clara

### Trade-offs
- ⚠️ Mudanças não são salvas automaticamente
- ⚠️ Usuário pode modificar manualmente após autopopulação
- ⚠️ Não funciona em batch operations

### Exemplos de Uso
- Formulários de cadastro (autopopular endereço do cliente)
- Pedidos de venda (autopopular preço/unitário)
- SMS/Mensagens (autopopular telefone do contato)
- Ordens de serviço (autopopular dados do equipamento)

---

## Template de Novo Padrão

```markdown
## PXXX: [Nome do Padrão]

**Categoria:** [Tipo]
**Quando Usar:** [Cenário]
**Evitar Quando:** [Situações]

### Problema
[O que resolve?]

### Solução
[Como resolver?]

\`\`\`language
// Código exemplo
\`\`\`

### Benefícios
- ✅ [Benefício]

### Trade-offs
- ⚠️ [Trade-off]

### Exemplos de Uso
- [Onde usar]
```

---

**Última atualização:** [Data]
