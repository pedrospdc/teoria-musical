#!/bin/bash
# Renomeia arquivos da wiki para português e atualiza links

cd "$(dirname "$0")/.."

echo "Renomeando arquivos da wiki para português..."

# Mapeamento EN -> PT-BR
declare -A RENAME_MAP=(
    ["BasicConcepts.md"]="Conceitos-Basicos.md"
    ["MajorScalesAndKeySignatures.md"]="Escalas-Maiores-e-Armaduras.md"
    ["MinorScalesAndKeySignatures.md"]="Escalas-Menores-e-Armaduras.md"
    ["BasicsOfRhythm.md"]="Fundamentos-de-Ritmo.md"
    ["Intervals.md"]="Intervalos.md"
    ["Triads.md"]="Triades.md"
    ["RomanNumeralsAndCadences.md"]="Algarismos-Romanos-e-Cadencias.md"
    ["SeventhChords.md"]="Acordes-de-Setima.md"
    ["HarmonicProgression.md"]="Progressao-Harmonica.md"
    ["NonChordTones.md"]="Notas-Estranhas.md"
    ["MelodicAnalysis.md"]="Analise-Melodica.md"
    ["FormInPopularMusic.md"]="Forma-na-Musica-Popular.md"
    ["PhrasesInCombination.md"]="Frases-em-Combinacao.md"
    ["AccompanimentalTexture.md"]="Texturas-de-Acompanhamento.md"
    ["CreatingContrast.md"]="Criando-Contraste.md"
    ["FiguredBass.md"]="Baixo-Cifrado.md"
    ["SecondaryDominants.md"]="Dominantes-Secundarias.md"
    ["SecondaryDiminishedChords.md"]="Acordes-Diminutos-Secundarios.md"
    ["ModeMixture.md"]="Mistura-de-Modos.md"
    ["Neapolitan.md"]="Acorde-Napolitano.md"
    ["AugmentedSixthChords.md"]="Acordes-de-Sexta-Aumentada.md"
    ["Modulation.md"]="Modulacao.md"
    ["EnharmonicModulation.md"]="Modulacao-Enarmonica.md"
    ["BinaryAndTernaryForms.md"]="Formas-Binarias-e-Ternarias.md"
    ["SonataAndRondoForms.md"]="Formas-Sonata-e-Rondo.md"
    ["VoiceLeadingTriads.md"]="Conducao-de-Vozes-Triades.md"
    ["VoiceLeadingSeventhChords.md"]="Conducao-de-Vozes-Setimas.md"
    ["VoiceLeadingNCTs.md"]="Conducao-de-Vozes-Notas-Estranhas.md"
    ["VoiceLeadingChromaticHarmonies.md"]="Conducao-de-Vozes-Cromatico.md"
    ["IntroductionToCounterpoint.md"]="Introducao-ao-Contraponto.md"
    ["IntroductionToJazzTheory.md"]="Introducao-a-Teoria-do-Jazz.md"
    ["ImpressionismAndExtendedTonality.md"]="Impressionismo-e-Tonalidade-Estendida.md"
    ["SetTheory.md"]="Teoria-dos-Conjuntos.md"
    ["Serialism.md"]="Serialismo.md"
    ["Minimalism.md"]="Minimalismo.md"
    ["Pitch.md"]="Altura.md"
    ["Notation.md"]="Notacao.md"
    ["HalfStepsAndWholeSteps.md"]="Semitons-e-Tons.md"
    ["TheMajorScale.md"]="Escala-Maior.md"
    ["Accidentals.md"]="Acidentes.md"
    ["TimeSignature.md"]="Formula-de-Compasso.md"
    ["cadences.md"]="Cadencias.md"
    ["PassingTones.md"]="Notas-de-Passagem.md"
    ["NeighborTones.md"]="Notas-Auxiliares.md"
    ["Suspension.md"]="Suspensao.md"
    ["Anticipation.md"]="Antecipacao.md"
    ["OctaveRegisters.md"]="Registros-de-Oitava.md"
    ["EnharmonicNotes.md"]="Notas-Enarmonicas.md"
    ["MinorScales.md"]="Escalas-Menores.md"
    ["MinorKeySignatures.md"]="Armaduras-Menores.md"
    ["ScaleDegreeNames.md"]="Graus-da-Escala.md"
    ["DurationalSymbols.md"]="Figuras-de-Duracao.md"
    ["DotsAndTies.md"]="Pontos-e-Ligaduras.md"
    ["meter.md"]="Metrica.md"
    ["Tuplets.md"]="Quialteras.md"
)

# Passo 1: Renomear arquivos
echo "Passo 1: Renomeando arquivos..."
count=0
for old_name in "${!RENAME_MAP[@]}"; do
    new_name="${RENAME_MAP[$old_name]}"
    if [ -f "wiki/$old_name" ]; then
        mv "wiki/$old_name" "wiki/$new_name"
        echo "  ✓ $old_name → $new_name"
        ((count++))
    fi
done

# Passo 2: Atualizar links em todos os arquivos
echo ""
echo "Passo 2: Atualizando links internos..."
for old_name in "${!RENAME_MAP[@]}"; do
    new_name="${RENAME_MAP[$old_name]}"
    old_base="${old_name%.md}"
    new_base="${new_name%.md}"

    # Atualizar links no formato [texto](arquivo) e [texto](arquivo.md)
    find wiki -name "*.md" -type f -exec sed -i \
        -e "s|](${old_base})|](${new_base})|g" \
        -e "s|](${old_name})|](${new_name})|g" {} +
done

# Passo 3: Atualizar Home.md e _Sidebar.md
cat > wiki/Home.md << 'EOL'
# Teoria Musical para a Sala de Aula do Século XXI

Bem-vindo à tradução brasileira de **Music Theory for the 21st-Century Classroom** de Robert Hutchinson.

## 📚 Sobre Este Material

Curso completo de teoria musical em português brasileiro, desde conceitos básicos até tópicos avançados.

## 🎵 Como Navegar

Use a **barra lateral** para navegar pelos capítulos organizados por tema.

**Iniciantes:** Comece por [Conceitos Básicos](Conceitos-Basicos)

## 📖 Estrutura do Curso

- **Parte I**: Fundamentos (Cap. 1-4)
- **Parte II**: Harmonia Básica (Cap. 5-9)
- **Parte III**: Melodia e Forma (Cap. 10-15)
- **Parte IV**: Harmonia Avançada (Cap. 16-23)
- **Parte V**: Formas Musicais (Cap. 24-25)
- **Parte VI**: Condução de Vozes (Cap. 26-30)
- **Parte VII**: Tópicos Especiais (Cap. 31-35)

## 📝 Créditos

**Autor Original**: Robert Hutchinson
**Licença**: GNU Free Documentation License
**Repositório**: [github.com/pedrospdc/teoria-musical](https://github.com/pedrospdc/teoria-musical)
EOL

cat > wiki/_Sidebar.md << 'EOL'
### 📚 Teoria Musical PT-BR

**[🏠 Início](Home)**

---

### Fundamentos

1. [Conceitos Básicos](Conceitos-Basicos)
   - [Altura](Altura)
   - [Notação](Notacao)
   - [Registros de Oitava](Registros-de-Oitava)
   - [Acidentes](Acidentes)
   - [Notas Enarmônicas](Notas-Enarmonicas)

2. [Escalas Maiores](Escalas-Maiores-e-Armaduras)
   - [Semitons e Tons](Semitons-e-Tons)
   - [Escala Maior](Escala-Maior)

3. [Escalas Menores](Escalas-Menores-e-Armaduras)
   - [Escalas Menores](Escalas-Menores)
   - [Armaduras Menores](Armaduras-Menores)
   - [Graus da Escala](Graus-da-Escala)

4. [Fundamentos de Ritmo](Fundamentos-de-Ritmo)
   - [Fórmula de Compasso](Formula-de-Compasso)
   - [Figuras de Duração](Figuras-de-Duracao)
   - [Pontos e Ligaduras](Pontos-e-Ligaduras)
   - [Métrica](Metrica)
   - [Quiálteras](Quialteras)

---

### Harmonia Básica

5. [Intervalos](Intervalos)
6. [Tríades](Triades)
7. [Algarismos Romanos](Algarismos-Romanos-e-Cadencias)
   - [Cadências](Cadencias)
8. [Acordes de Sétima](Acordes-de-Setima)
9. [Progressão Harmônica](Progressao-Harmonica)

---

### Melodia e Forma

10. [Notas Estranhas](Notas-Estranhas)
    - [Notas de Passagem](Notas-de-Passagem)
    - [Notas Auxiliares](Notas-Auxiliares)
    - [Suspensão](Suspensao)
    - [Antecipação](Antecipacao)

11. [Análise Melódica](Analise-Melodica)
12. [Forma Popular](Forma-na-Musica-Popular)
13. [Frases](Frases-em-Combinacao)
14. [Texturas](Texturas-de-Acompanhamento)
15. [Contraste](Criando-Contraste)

---

### Harmonia Avançada

16. [Baixo Cifrado](Baixo-Cifrado)
17. [Dominantes Secundárias](Dominantes-Secundarias)
18. [Diminutos Secundários](Acordes-Diminutos-Secundarios)
19. [Mistura de Modos](Mistura-de-Modos)
20. [Napolitano](Acorde-Napolitano)
21. [Sextas Aumentadas](Acordes-de-Sexta-Aumentada)
22. [Modulação](Modulacao)
23. [Modulação Enarmônica](Modulacao-Enarmonica)

---

### Formas Musicais

24. [Binárias e Ternárias](Formas-Binarias-e-Ternarias)
25. [Sonata e Rondó](Formas-Sonata-e-Rondo)

---

### Condução de Vozes

26. [Tríades](Conducao-de-Vozes-Triades)
27. [Sétimas](Conducao-de-Vozes-Setimas)
28. [Notas Estranhas](Conducao-de-Vozes-Notas-Estranhas)
29. [Cromático](Conducao-de-Vozes-Cromatico)
30. [Contraponto](Introducao-ao-Contraponto)

---

### Tópicos Especiais

31. [Jazz](Introducao-a-Teoria-do-Jazz)
32. [Impressionismo](Impressionismo-e-Tonalidade-Estendida)
33. [Teoria dos Conjuntos](Teoria-dos-Conjuntos)
34. [Serialismo](Serialismo)
35. [Minimalismo](Minimalismo)
EOL

echo ""
echo "✓ Concluído!"
echo "  Arquivos renomeados: $count"
echo "  Links atualizados em todos os arquivos"
echo "  Home.md e _Sidebar.md atualizados"
