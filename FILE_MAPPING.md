# Mapeamento de Arquivos / File Mapping

Este documento mapeia os nomes de arquivos originais (em inglês) para seus títulos traduzidos em português brasileiro.

## Por que os nomes de arquivos estão em inglês?

Os nomes de arquivos foram mantidos em inglês para:
- Preservar compatibilidade com links cruzados
- Facilitar sincronização com o repositório original
- Evitar problemas com caracteres especiais em URLs
- Manter consistência na estrutura do projeto

## Mapeamento Completo

### Capítulos Principais

| Arquivo | Título em Português |
|---------|-------------------|
| BasicConcepts.md | Conceitos Básicos |
| MajorScalesAndKeySignatures.md | Escalas Maiores e Armaduras de Clave |
| MinorScalesAndKeySignatures.md | Escalas Menores e Armaduras de Clave |
| BasicsOfRhythm.md | Fundamentos de Ritmo |
| Intervals.md | Intervalos |
| Triads.md | Tríades |
| RomanNumeralsAndCadences.md | Algarismos Romanos e Cadências |
| SeventhChords.md | Acordes de Sétima |
| HarmonicProgression.md | Progressão Harmônica e Função Harmônica |
| NonChordTones.md | Notas Estranhas ao Acorde |
| MelodicAnalysis.md | Análise Melódica |
| FormInPopularMusic.md | Forma na Música Popular |
| PhrasesInCombination.md | Frases em Combinação |
| AccompanimentalTexture.md | Texturas de Acompanhamento |
| CreatingContrast.md | Criando Contraste Entre Seções |
| FiguredBass.md | Baixo Cifrado |
| SecondaryDominants.md | Dominantes Secundárias |
| SecondaryDiminishedChords.md | Acordes Diminutos Secundários |
| ModeMixture.md | Mistura de Modos |
| Neapolitan.md | Acorde Napolitano |
| AugmentedSixthChords.md | Acordes de Sexta Aumentada |
| Modulation.md | Modulação |
| EnharmonicModulation.md | Modulação Enarmônica |
| BinaryAndTernaryForms.md | Formas Binárias e Ternárias |
| SonataAndRondoForms.md | Formas Sonata e Rondó |
| VoiceLeadingTriads.md | Condução de Vozes com Tríades |
| VoiceLeadingSeventhChords.md | Condução de Vozes com Acordes de Sétima |
| VoiceLeadingNCTs.md | Condução de Vozes com Notas Estranhas |
| VoiceLeadingChromaticHarmonies.md | Condução de Vozes com Harmonias Cromáticas |
| IntroductionToCounterpoint.md | Introdução ao Contraponto |
| IntroductionToJazzTheory.md | Introdução à Teoria do Jazz |
| ImpressionismAndExtendedTonality.md | Impressionismo e Tonalidade Estendida |
| SetTheory.md | Teoria dos Conjuntos |
| Serialism.md | Serialismo |
| Minimalism.md | Minimalismo |

### Seções e Tópicos

| Arquivo | Título em Português |
|---------|-------------------|
| Pitch.md | Altura |
| Notation.md | Notação |
| HalfStepsAndWholeSteps.md | Semitons e Tons Inteiros |
| TheMajorScale.md | A Escala Maior |
| Accidentals.md | Acidentes |
| TimeSignature.md | Fórmula de Compasso |
| cadences.md | Cadências |
| PassingTones.md | Notas de Passagem |
| NeighborTones.md | Notas Auxiliares |
| Suspension.md | Suspensão |
| Anticipation.md | Antecipação |

## Terminologia Musical - EN → PT-BR

| Inglês | Português |
|--------|-----------|
| Half step | Semitom |
| Whole step | Tom inteiro / Tom |
| Scale | Escala |
| Chord | Acorde |
| Triad | Tríade |
| Interval | Intervalo |
| Cadence | Cadência |
| Voice Leading | Condução de vozes |
| Counterpoint | Contraponto |
| Key signature | Armadura de clave |
| Time signature | Fórmula de compasso |
| Sharp | Sustenido |
| Flat | Bemol |
| Natural | Bequadro |

## Workflow de Tradução

1. **Conversão HTML → Markdown**: `convert_to_markdown.py`
   - Remove navegação, scripts, menus
   - Preserva conteúdo principal
   - Mantém LaTeX, imagens, links

2. **Tradução Markdown → PT-BR**: Agente de tradução
   - Traduz texto mantendo formatação
   - Preserva fórmulas matemáticas
   - Mantém nomes de arquivos

3. **Estrutura de diretórios**:
   ```
   original/     - HTML original em inglês
   markdown/     - Markdown em inglês (limpo)
   pt-br/        - Markdown traduzido para português
   ```
