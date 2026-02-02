# Teoria Musical para a Sala de Aula do Seculo XXI

Traducao para portugues brasileiro do livro "Music Theory for the 21st-Century Classroom" de Robert Hutchinson.

## Sobre o Projeto

Este repositorio contem a traducao completa do site de teoria musical originalmente disponivel em ingles em [musictheory.pugetsound.edu](https://musictheory.pugetsound.edu/mt21c/MusicTheory.html).

O objetivo e tornar este excelente material didatico acessivel para estudantes e professores de musica brasileiros, utilizando a terminologia musical padrao em portugues brasileiro.

## Estrutura do Repositorio

```
teoria-musical/
├── pt-br/                      # Markdown traduzido para portugues brasileiro ✓
├── markdown/                   # Markdown em ingles (extraido do HTML)
├── original/                   # HTML original em ingles (referencia)
├── scripts/                    # Scripts de conversao e traducao
│   ├── convert_to_markdown.py  # HTML → Markdown (remove navegação)
│   ├── translate_markdown.py   # Preparação para tradução
│   └── [deprecated scripts]    # Scripts antigos (crawler, translator)
├── venv/                       # Virtual environment Python
└── FILE_MAPPING.md             # Mapeamento arquivo → título PT-BR
```

## Conteudo

O material cobre os seguintes topicos:

### Fundamentos (Capitulos 1-4)
- Conceitos Basicos: Altura, Notacao, Registros de Oitava, Acidentes, Notas Enarmonicas
- Escalas Maiores e Armaduras de Clave
- Escalas Menores e Armaduras de Clave
- Fundamentos de Ritmo: Formula de Compasso, Figuras de Duracao, Metrica, Quialteras

### Harmonia Basica (Capitulos 5-9)
- Intervalos
- Triades
- Numeros Romanos e Cadencias
- Acordes de Setima
- Progressao Harmonica e Funcao Harmonica

### Melodia e Forma (Capitulos 10-15)
- Notas Estranhas ao Acorde
- Analise Melodica
- Forma na Musica Popular
- Frases em Combinacao
- Texturas de Acompanhamento
- Criando Contraste Entre Secoes

### Harmonia Avancada (Capitulos 16-23)
- Baixo Cifrado
- Dominantes Secundarias
- Acordes Diminutos Secundarios
- Mistura de Modos
- Acorde Napolitano
- Acordes de Sexta Aumentada
- Modulacao
- Modulacao Enarmonica

### Forma e Estrutura (Capitulos 24-25)
- Formas Binaria e Ternaria
- Forma Sonata e Rondo

### Conducao de Vozes e Contraponto (Capitulos 26-30)
- Conducao de Vozes com Triades
- Conducao de Vozes com Acordes de Setima
- Conducao de Vozes com Notas Estranhas
- Conducao de Vozes com Harmonias Cromaticas
- Introducao ao Contraponto

### Topicos Especiais (Capitulos 31-35)
- Introducao a Teoria do Jazz
- Impressionismo e Tonalidade Estendida
- Teoria dos Conjuntos
- Serialismo
- Minimalismo

## Terminologia Musical

A traducao utiliza a terminologia musical padrao em portugues brasileiro:

| Ingles | Portugues |
|--------|-----------|
| Pitch | Altura |
| Sharp | Sustenido |
| Flat | Bemol |
| Natural | Bequadro |
| Scale | Escala |
| Chord | Acorde |
| Triad | Triade |
| Interval | Intervalo |
| Key Signature | Armadura de Clave |
| Time Signature | Formula de Compasso |
| Whole Note | Semibreve |
| Half Note | Minima |
| Quarter Note | Seminima |
| Eighth Note | Colcheia |
| Cadence | Cadencia |
| Voice Leading | Conducao de Vozes |
| Counterpoint | Contraponto |

## Como Usar

Os arquivos traduzidos estão em **Markdown** na pasta `pt-br/`. Para visualizar:

1. **Visualização local**: Use qualquer visualizador de Markdown ou GitHub
2. **Índice principal**: Comece pelo [pt-br/README.md](pt-br/README.md)
3. **Navegação**: Os links entre capítulos estão preservados

**Nota:** Fórmulas matemáticas usam LaTeX (formato `\(...\)`) e podem requerer um renderizador apropriado.

## Workflow de Tradução

Este projeto foi traduzido usando o seguinte processo:

### 1. Extração do Conteúdo (HTML → Markdown)
```bash
venv/bin/python scripts/convert_to_markdown.py all
```
- Remove navegação, menus, scripts
- Preserva conteúdo principal, imagens, LaTeX
- Salva em `markdown/`

### 2. Tradução (Markdown EN → PT-BR)
- Tradução automática com Claude
- Preserva formatação, fórmulas matemáticas, links
- Aplica terminologia musical brasileira
- Salva em `pt-br/`

### 3. Mapeamento de Arquivos
- Nomes de arquivos mantidos em inglês (compatibilidade)
- Títulos traduzidos para português
- Ver [FILE_MAPPING.md](FILE_MAPPING.md) para correspondências

## Creditos

- **Autor Original:** Robert Hutchinson
- **Obra Original:** [Music Theory for the 21st-Century Classroom](https://musictheory.pugetsound.edu/mt21c/MusicTheory.html)
- **Licenca Original:** GNU Free Documentation License

## Licenca

Este trabalho de traducao segue a mesma licenca do material original: GNU Free Documentation License (GFDL).

## Contribuicoes

Contribuicoes sao bem-vindas! Se voce encontrar erros de traducao ou tiver sugestoes de melhoria, por favor abra uma issue ou envie um pull request.

## Aviso Legal

Este e um projeto de traducao nao-oficial. Todo o conteudo original pertence ao autor Robert Hutchinson e a University of Puget Sound.
