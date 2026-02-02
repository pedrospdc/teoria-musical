# Scripts de Conversão e Tradução

## Scripts Disponíveis

### convert_to_markdown.py
Converte arquivos HTML para Markdown limpo.

**Uso:**
```bash
# Converter todos os arquivos
venv/bin/python scripts/convert_to_markdown.py all

# Converter arquivo específico
venv/bin/python scripts/convert_to_markdown.py HalfStepsAndWholeSteps.html
```

**O que faz:**
- Remove navegação, menus, scripts
- Extrai apenas o conteúdo principal
- Preserva LaTeX, imagens, links
- Cria índice automático

### translate_markdown.py
Helper para preparar arquivos para tradução (não usado no workflow atual).

## Workflow Completo

1. **HTML → Markdown:**
   ```bash
   venv/bin/python scripts/convert_to_markdown.py all
   ```

2. **Tradução:**
   - Feita via agente Claude (automática)
   - Preserva formatação e elementos técnicos
   - Aplica terminologia musical brasileira

3. **Resultado:**
   - `markdown/` - Inglês limpo
   - `pt-br/` - Português brasileiro traduzido
