#!/bin/bash
# Quick script to update ADR-INDEX stats
sed -i.bak 's/Total de ADRs:** 3/Total de ADRs:** 4/' .claude/memory/decisions/ADR-INDEX.md
sed -i.bak 's/Aceitos:** 3/Aceitos:** 4/' .claude/memory/decisions/ADR-INDEX.md
sed -i.bak '/| 003 | 2025-11-17 |/a\
| 004 | 2025-11-17 | [Otimizações Performance e Paralelização](ADR-007-PERFORMANCE.md) | ✅ Aceito | #performance #speed #parallel |' .claude/memory/decisions/ADR-INDEX.md
rm .claude/memory/decisions/ADR-INDEX.md.bak
