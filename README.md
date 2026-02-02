# Teoria Musical para a Sala de Aula do Seculo XXI

Traducao para portugues brasileiro do livro "Music Theory for the 21st-Century Classroom" de Robert Hutchinson.

## [Acesse o conteudo completo na Wiki](https://github.com/pedrospdc/teoria-musical/wiki)

## Sobre o Projeto

Este repositorio contem a traducao completa do site de teoria musical originalmente disponivel em ingles em [musictheory.pugetsound.edu](https://musictheory.pugetsound.edu/mt21c/MusicTheory.html).

O objetivo e tornar este excelente material didatico acessivel para estudantes e professores de musica brasileiros, utilizando a terminologia musical padrao em portugues brasileiro.

## Estrutura do Repositorio

```
teoria-musical/
├── markdown/                   # Markdown em ingles (extraido do HTML)
├── original/                   # HTML original em ingles (referencia)
├── scripts/                    # Scripts de conversao e traducao
│   ├── convert_to_markdown.py  # HTML → Markdown
│   ├── download_external_files.py  # Download de imagens
│   └── fix_latex_to_unicode.py     # Conversao LaTeX → Unicode
└── FILE_MAPPING.md             # Mapeamento arquivo → título PT-BR
```

O conteudo traduzido fica na [Wiki do repositorio](https://github.com/pedrospdc/teoria-musical/wiki), com 277 paginas e mais de 1100 imagens.

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

## Workflow de Tradução

1. **Extracao do HTML original** para Markdown (`scripts/convert_to_markdown.py`)
2. **Download de imagens** do site original (`scripts/download_external_files.py`)
3. **Conversao de LaTeX** para Unicode (`scripts/fix_latex_to_unicode.py`)
4. **Traducao** do ingles para portugues brasileiro com Claude
5. **Publicacao** na Wiki do GitHub

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
