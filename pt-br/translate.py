#!/usr/bin/env python3
"""
Script para traduzir as páginas HTML de teoria musical do inglês para português brasileiro.
"""

import os
import re

# Diretório dos arquivos
DIR = "/home/user/teoria-musical/pt-br"

# Lista de arquivos a traduzir
FILES = [
    "BinaryAndTernaryForms.html",
    "BinaryAndTernaryIntroduction.html",
    "SectionalVersusContinuous.html",
    "BalancedBinary.html",
    "RoundedBinary.html",
    "SimpleBinary.html",
    "BinaryPrinciple.html",
    "TernaryForm.html",
    "DistinguishingBetweenRoundedBinaryAndTernary.html",
    "BinaryAndTernaryPracticeExercises.html",
    "SonataAndRondoForms.html",
    "SonataIntroduction.html",
    "FourStructuralFunctions.html",
    "RondoForm.html",
    "RondoCharacter.html",
    "SonataAndRondoForms-6.html",
    "SonataAndRondoPracticeExercises.html",
]

# Traduções - termos musicais específicos e frases completas
TRANSLATIONS = [
    # Títulos de página e capítulo
    (r'<title>Binary and Ternary Forms</title>', '<title>Formas Binárias e Ternárias</title>'),
    (r'<title>Binary and Ternary Form</title>', '<title>Forma Binária e Ternária</title>'),
    (r'<title>Sectional versus Continuous</title>', '<title>Seccional versus Contínua</title>'),
    (r'<title>Balanced Binary</title>', '<title>Binária Balanceada</title>'),
    (r'<title>Rounded Binary</title>', '<title>Binária com Recapitulação</title>'),
    (r'<title>Simple Binary</title>', '<title>Binária Simples</title>'),
    (r'<title>Binary Principle</title>', '<title>Princípio Binário</title>'),
    (r'<title>Ternary Form</title>', '<title>Forma Ternária</title>'),
    (r'<title>Distinguishing between Rounded Binary and Ternary</title>', '<title>Distinguindo entre Binária com Recapitulação e Ternária</title>'),
    (r'<title>Practice Exercises</title>', '<title>Exercícios Práticos</title>'),
    (r'<title>Sonata and Rondo Forms</title>', '<title>Formas Sonata e Rondó</title>'),
    (r'<title>Sonata Form</title>', '<title>Forma Sonata</title>'),
    (r'<title>The Four Structural Functions in Music</title>', '<title>As Quatro Funções Estruturais na Música</title>'),
    (r'<title>Rondo Form</title>', '<title>Forma Rondó</title>'),
    (r'<title>Rondo Character</title>', '<title>Caráter de Rondó</title>'),
    (r'<title>Standard Forms in a Multimovement Classical Piece</title>', '<title>Formas Padrão em uma Peça Clássica de Múltiplos Movimentos</title>'),

    # Títulos em spans (seções e capítulos)
    (r'<span class="title">Binary and Ternary Forms</span>', '<span class="title">Formas Binárias e Ternárias</span>'),
    (r'<span class="title">Binary and Ternary Form</span>', '<span class="title">Forma Binária e Ternária</span>'),
    (r'<span class="title">Sectional versus Continuous</span>', '<span class="title">Seccional versus Contínua</span>'),
    (r'<span class="title">Balanced Binary</span>', '<span class="title">Binária Balanceada</span>'),
    (r'<span class="title">Rounded Binary</span>', '<span class="title">Binária com Recapitulação</span>'),
    (r'<span class="title">Simple Binary</span>', '<span class="title">Binária Simples</span>'),
    (r'<span class="title">Binary Principle</span>', '<span class="title">Princípio Binário</span>'),
    (r'<span class="title">Ternary Form</span>', '<span class="title">Forma Ternária</span>'),
    (r'<span class="title">Compound Ternary</span>', '<span class="title">Ternária Composta</span>'),
    (r'<span class="title">Distinguishing between Rounded Binary and Ternary</span>', '<span class="title">Distinguindo entre Binária com Recapitulação e Ternária</span>'),
    (r'<span class="title">Written-Out Repeats</span>', '<span class="title">Repetições Escritas</span>'),
    (r'<span class="title">Practice Exercises</span>', '<span class="title">Exercícios Práticos</span>'),
    (r'<span class="title">Sonata and Rondo Forms</span>', '<span class="title">Formas Sonata e Rondó</span>'),
    (r'<span class="title">Sonata Form</span>', '<span class="title">Forma Sonata</span>'),
    (r'<span class="title">Diagram of Sonata Form</span>', '<span class="title">Diagrama da Forma Sonata</span>'),
    (r'<span class="title">Sonatina Form</span>', '<span class="title">Forma Sonatina</span>'),
    (r'<span class="title">Sonata Principle</span>', '<span class="title">Princípio da Sonata</span>'),
    (r'<span class="title">The Monothematic Sonata</span>', '<span class="title">A Sonata Monotemática</span>'),
    (r'<span class="title">The Four Structural Functions in Music</span>', '<span class="title">As Quatro Funções Estruturais na Música</span>'),
    (r'<span class="title">Expository Function</span>', '<span class="title">Função Expositiva</span>'),
    (r'<span class="title">Transitional Function</span>', '<span class="title">Função de Transição</span>'),
    (r'<span class="title">Developmental Function</span>', '<span class="title">Função de Desenvolvimento</span>'),
    (r'<span class="title">Terminative Function</span>', '<span class="title">Função Terminativa</span>'),
    (r'<span class="title">Rondo Form</span>', '<span class="title">Forma Rondó</span>'),
    (r'<span class="title">Sonata Rondo Form</span>', '<span class="title">Forma Sonata-Rondó</span>'),
    (r'<span class="title">Rondo Character</span>', '<span class="title">Caráter de Rondó</span>'),
    (r'<span class="title">Standard Forms in a Multimovement Classical Piece</span>', '<span class="title">Formas Padrão em uma Peça Clássica de Múltiplos Movimentos</span>'),
    (r'<span class="title">Exercise Group.</span>', '<span class="title">Grupo de Exercícios.</span>'),

    # Tipos de elementos
    (r'<span class="type">Chapter</span>', '<span class="type">Capítulo</span>'),
    (r'<span class="type">Section</span>', '<span class="type">Seção</span>'),
    (r'<span class="type">Subsection</span>', '<span class="type">Subseção</span>'),
    (r'<span class="type">Exercises</span>', '<span class="type">Exercícios</span>'),
    (r'<span class="type">Figure</span>', '<span class="type">Figura</span>'),
    (r'<span class="type">Answer</span>', '<span class="type">Resposta</span>'),

    # Conteúdo principal - parágrafos e termos
    (r'"<dfn class="terminology">sectional</dfn>"', '"<dfn class="terminology">seccional</dfn>"'),
    (r'"<dfn class="terminology">continuous</dfn>"', '"<dfn class="terminology">contínua</dfn>"'),
    (r'<dfn class="terminology">balanced binary</dfn>', '<dfn class="terminology">binária balanceada</dfn>'),
    (r'<dfn class="terminology">rounded binary</dfn>', '<dfn class="terminology">binária com recapitulação</dfn>'),
    (r'<dfn class="terminology">"Simple" binary</dfn>', '<dfn class="terminology">Binária "simples"</dfn>'),
    (r'<dfn class="terminology">Binary principle</dfn>', '<dfn class="terminology">Princípio binário</dfn>'),
    (r'<dfn class="terminology">Ternary form</dfn>', '<dfn class="terminology">Forma ternária</dfn>'),
    (r'<dfn class="terminology">compound ternary</dfn>', '<dfn class="terminology">ternária composta</dfn>'),
    (r'<dfn class="terminology">Sonata form</dfn>', '<dfn class="terminology">Forma sonata</dfn>'),
    (r'<dfn class="terminology">sonatina form</dfn>', '<dfn class="terminology">forma sonatina</dfn>'),
    (r'<dfn class="terminology">expository function</dfn>', '<dfn class="terminology">função expositiva</dfn>'),
    (r'<dfn class="terminology">transitional function</dfn>', '<dfn class="terminology">função de transição</dfn>'),
    (r'<dfn class="terminology">developmental function</dfn>', '<dfn class="terminology">função de desenvolvimento</dfn>'),
    (r'<dfn class="terminology">Terminative function</dfn>', '<dfn class="terminology">Função terminativa</dfn>'),
    (r'<dfn class="terminology">rondo</dfn>', '<dfn class="terminology">rondó</dfn>'),
    (r'<dfn class="terminology">"two-reprise</dfn>', '<dfn class="terminology">"duas reprises</dfn>'),

    # Frases completas - Introdução Binária e Ternária
    (r'>In this chapter we will compare the following:<', '>Neste capítulo, compararemos o seguinte:<'),
    (r'>Sectional versus Continuous<', '>Seccional versus Contínua<'),
    (r'>Binary versus Ternary<', '>Binária versus Ternária<'),
    (r'>Rounded Binary versus Ternary<', '>Binária com Recapitulação versus Ternária<'),

    # Frases - Seccional vs Contínua
    (r'to a binary or ternary form when the first section \(the A section\) ends on the tonic\.', 'a uma forma binária ou ternária quando a primeira seção (a seção A) termina na tônica.'),
    (r'\(Note: We use lowercase letters to refer to phrases and uppercase letters to refer to sections\.\)', '(Nota: Usamos letras minúsculas para nos referir a frases e letras maiúsculas para nos referir a seções.)'),
    (r'is used when the first section of a binary or ternary form does <em class="emphasis">not</em> end on the tonic chord', 'é usada quando a primeira seção de uma forma binária ou ternária <em class="emphasis">não</em> termina no acorde de tônica'),
    (r'While this often means the first section ends in a new key, it can also mean the first section ends on the dominant chord in a half cadence\.', 'Embora isso frequentemente signifique que a primeira seção termina em uma nova tonalidade, também pode significar que a primeira seção termina no acorde de dominante em uma semicadência.'),
    (r'In naming any binary or ternary form, use the terms sectional or continuous before binary or ternary', 'Ao nomear qualquer forma binária ou ternária, use os termos seccional ou contínua antes de binária ou ternária'),
    (r'"<em class="emphasis">sectional</em> binary," "<em class="emphasis">continuous</em> binary," "<em class="emphasis">sectional</em> ternary," or "<em class="emphasis">continuous</em> ternary\."', '"binária <em class="emphasis">seccional</em>", "binária <em class="emphasis">contínua</em>", "ternária <em class="emphasis">seccional</em>" ou "ternária <em class="emphasis">contínua</em>".'),
    (r'which means <em class="emphasis">both</em> the first section \(the A section\) and second section \(the A\' or B section\) are repeated', 'que significa que <em class="emphasis">ambas</em> a primeira seção (a seção A) e a segunda seção (a seção A\' ou B) são repetidas'),
    (r'used in conjunction with binary \("rounded binary"\) to specify that the opening material returns after the contrasting section', 'usada em conjunto com binária ("binária com recapitulação") para especificar que o material de abertura retorna após a seção contrastante'),
    (r'>In the following sections we will discuss three types of binary forms:<', '>Nas seções seguintes, discutiremos três tipos de formas binárias:<'),
    (r'>Balanced Binary<', '>Binária Balanceada<'),
    (r'>Rounded Binary<', '>Binária com Recapitulação<'),
    (r'>"Simple" Binary \(usually called "binary"\)<', '>Binária "Simples" (geralmente chamada de "binária")<'),

    # Binária Balanceada
    (r'form, according to Douglass Green in his book', 'forma, segundo Douglass Green em seu livro'),
    (r'features a binary form with a first section \(the A section\) ending in a new key, and the second section ending <em class="emphasis">with essentially the same cadence</em>, now transposed to the original key', 'apresenta uma forma binária com uma primeira seção (a seção A) terminando em uma nova tonalidade, e a segunda seção terminando <em class="emphasis">com essencialmente a mesma cadência</em>, agora transposta para a tonalidade original'),
    (r'>Because the first section of a balanced binary ends in a new key, it is inherently a <em class="emphasis">continuous</em> binary form\.<', '>Como a primeira seção de uma binária balanceada termina em uma nova tonalidade, ela é inerentemente uma forma binária <em class="emphasis">contínua</em>.<'),
    (r'>Balanced binary form can be found in movements from the Baroque era', '>A forma binária balanceada pode ser encontrada em movimentos da era Barroca'),
    (r'including dance suites by Bach, Handel, and others', 'incluindo suítes de dança de Bach, Handel e outros'),
    (r'>The movement below shows the endings of the first and section sections of the Courante', '>O movimento abaixo mostra os finais das primeira e segunda seções da Courante'),

    # Binária com Recapitulação
    (r'form, the material at the beginning of the first section returns, often shortened, after a contrasting phrase at the beginning of the second section', 'forma, o material do início da primeira seção retorna, frequentemente encurtado, após uma frase contrastante no início da segunda seção'),
    (r'>A generic phrase diagram of rounded binary form is shown below\.<', '>Um diagrama de frases genérico da forma binária com recapitulação é mostrado abaixo.<'),
    (r'>Below is an example of a rounded binary form\.<', '>Abaixo está um exemplo de forma binária com recapitulação.<'),
    (r'Because both the first section \(the A section\) and second section \(the B section\) repeat in the example above, this form would be called "two-reprise continuous rounded binary form\."', 'Como tanto a primeira seção (a seção A) quanto a segunda seção (a seção B) se repetem no exemplo acima, essa forma seria chamada de "forma binária contínua com recapitulação de duas reprises".'),
    (r'>Another example of a rounded binary form is below\.<', '>Outro exemplo de forma binária com recapitulação está abaixo.<'),
    (r'>This form of the example above would be called "two-reprise continuous rounded binary form" because:<', '>Essa forma do exemplo acima seria chamada de "forma binária contínua com recapitulação de duas reprises" porque:<'),
    (r'>"Two-reprise" means both the first and second sections repeat<', '>"Duas reprises" significa que tanto a primeira quanto a segunda seção se repetem<'),
    (r'>"Continuous" means the first section does not end on the tonic chord<', '>"Contínua" significa que a primeira seção não termina no acorde de tônica<'),
    (r'>In a rounded binary form the opening melody returns after contrasting material<', '>Em uma forma binária com recapitulação, a melodia de abertura retorna após material contrastante<'),
    (r'>Rounded binary form is often encountered in compositions during the Classical era', '>A forma binária com recapitulação é frequentemente encontrada em composições da era Clássica'),
    (r'in music by Haydn, Mozart, and Beethoven', 'na música de Haydn, Mozart e Beethoven'),
    (r'especially as the form of a theme from a theme and variations, and as the minuet and/or trio section in a Minuet and Trio', 'especialmente como a forma de um tema de um tema e variações, e como a seção do minueto e/ou trio em um Minueto e Trio'),

    # Binária Simples
    (r'is a term used to describe a binary form that does not have features like the similar endings of a balanced binary or the return of opening material like the rounded binary', 'é um termo usado para descrever uma forma binária que não possui características como os finais semelhantes de uma binária balanceada ou o retorno do material de abertura como a binária com recapitulação'),
    (r'>You will encounter this type of binary form in music especially throughout the Baroque era, as well as in the early Classical era\.<', '>Você encontrará esse tipo de forma binária na música, especialmente ao longo da era Barroca, bem como no início da era Clássica.<'),
    (r'>Notice in the example above that the first section and second section can begin similarly in a binary form, resulting in the large-scale form AA\'\.', '>Note no exemplo acima que a primeira seção e a segunda seção podem começar de forma semelhante em uma forma binária, resultando na forma de grande escala AA\'.'),
    (r'>The second section often features development of the primary idea from the first section\.', '>A segunda seção frequentemente apresenta desenvolvimento da ideia principal da primeira seção.'),
    (r'>We will discuss development in the next chapter\.<', '>Discutiremos o desenvolvimento no próximo capítulo.<'),

    # Princípio Binário
    (r', as defined by Peter Spencer and Peter Temko in their book', ', como definido por Peter Spencer e Peter Temko em seu livro'),
    (r', states that the first section of a binary form modulates to a new key and the second section modulates back to the first key', ', afirma que a primeira seção de uma forma binária modula para uma nova tonalidade e a segunda seção modula de volta para a primeira tonalidade'),
    (r'>We find this principal exemplified in a high percentage of binary forms in the Baroque era, and diagrammed in the example below\.<', '>Encontramos esse princípio exemplificado em uma alta porcentagem de formas binárias na era Barroca, e diagramado no exemplo abaixo.<'),
    (r'>Diagram illustrating Binary Principle<', '>Diagrama ilustrando o Princípio Binário<'),

    # Forma Ternária
    (r'is usually diagrammed as ABA and is described as "statement, digression, restatement\."', 'é geralmente diagramada como ABA e descrita como "afirmação, digressão, reafirmação".'),
    (r'>A piece in a rather simple and straightforward ternary is shown below\.<', '>Uma peça em uma forma ternária bastante simples e direta é mostrada abaixo.<'),
    (r'>Below is a diagram of K\. 15mm by Mozart\.<', '>Abaixo está um diagrama de K. 15mm de Mozart.<'),
    (r'>Character pieces from the Romantic era with titles such as "Nocturne," "Intermezzo," and "Song Without Words,"', '>Peças de caráter da era Romântica com títulos como "Noturno", "Intermezzo" e "Canção Sem Palavras",'),
    (r'>among others, by composers such as Schubert, Chopin, Mendelssohn, Schumann, and Brahms, are often in a larger ternary form where each section might be longer than eight bars\.<', '>entre outras, de compositores como Schubert, Chopin, Mendelssohn, Schumann e Brahms, estão frequentemente em uma forma ternária maior, onde cada seção pode ter mais de oito compassos.<'),
    (r'>Below are examples from a larger ternary piece', '>Abaixo estão exemplos de uma peça ternária maior'),
    (r'>is a ternary form in which one of the sections \(the A or the B\) is itself a binary or ternary form\.', '>é uma forma ternária na qual uma das seções (a A ou a B) é ela mesma uma forma binária ou ternária.'),
    (r'>Examples can be found in the minuet and trio as well as the da capo aria\.<', '>Exemplos podem ser encontrados no minueto e trio, bem como na ária da capo.<'),
    (r'>In the next section, we will examine the differences between rounded binary and ternary\.<', '>Na próxima seção, examinaremos as diferenças entre binária com recapitulação e ternária.<'),

    # Distinguindo entre Binária com Recapitulação e Ternária
    (r'>In homework and on the test, you will encounter pieces that are five or six phrases long that could be rounded binary or ternary\.', '>Nos exercícios e na prova, você encontrará peças de cinco ou seis frases que podem ser binária com recapitulação ou ternária.'),
    (r'>While other authors have their own means to differentiate rounded binary from ternary, this text offers the following criteria to consider:<', '>Enquanto outros autores têm seus próprios meios para diferenciar binária com recapitulação de ternária, este texto oferece os seguintes critérios a considerar:<'),
    (r'><em class="emphasis">Proportion</em>: consider the proportion of the contrasting section to the other sections\.', '><em class="emphasis">Proporção</em>: considere a proporção da seção contrastante em relação às outras seções.'),
    (r'>If the contrasting section is too small to stand alone, the form is more likely to be rounded binary\.<', '>Se a seção contrastante for muito pequena para existir sozinha, a forma provavelmente é binária com recapitulação.<'),
    (r'><em class="emphasis">Nature</em>: consider the nature of the contrasting section\.</div>', '><em class="emphasis">Natureza</em>: considere a natureza da seção contrastante.</div>'),
    (r'>If the melody is built from motives from the first section, the form is likely to be a rounded binary\.', '>Se a melodia é construída a partir de motivos da primeira seção, a forma provavelmente é binária com recapitulação.'),
    (r'>Ternary form will have a contrasting melody in the contrasting section\.<', '>A forma ternária terá uma melodia contrastante na seção contrastante.<'),
    (r'>If the harmony consists mostly of a dominant pedal', '>Se a harmonia consiste principalmente de um pedal de dominante'),
    (r'the form is likely to be a rounded binary', 'a forma provavelmente é binária com recapitulação'),
    (r'><em class="emphasis">Era</em>: consider the era when the piece was written\.', '><em class="emphasis">Época</em>: considere a época em que a peça foi escrita.'),
    (r'>A piece by a Baroque composer \(J\.S\. Bach, Handel, Scarlatti, Couperin\) or Classical composer \(Haydn, Mozart, and Beethoven\) is more likely to be in rounded binary form', '>Uma peça de um compositor Barroco (J.S. Bach, Handel, Scarlatti, Couperin) ou compositor Clássico (Haydn, Mozart e Beethoven) provavelmente está em forma binária com recapitulação'),
    (r'whereas a piece by a Romantic era composer \(Schubert, Schumann, Chopin, Mendelssohn, and Brahms, among others\) is more likely to be in ternary form', 'enquanto uma peça de um compositor da era Romântica (Schubert, Schumann, Chopin, Mendelssohn e Brahms, entre outros) provavelmente está em forma ternária'),
    (r'>Note that these are generalities\. Baroque and Classical composers wrote compositions in ternary form and Romantic composers wrote pieces in rounded binary form\.<', '>Note que essas são generalidades. Compositores Barrocos e Clássicos escreveram composições em forma ternária e compositores Românticos escreveram peças em forma binária com recapitulação.<'),
    (r'>Consider the following piece by Beethoven:<', '>Considere a seguinte peça de Beethoven:<'),
    (r'>In terms of proportion', '>Em termos de proporção'),
    (r'>contain contrasting material to bars', '>contêm material contrastante aos compassos'),
    (r'>Because the contrasting material lasts for half as long as the open section, we consider the proportion as pointing toward rounded binary\.<', '>Como o material contrastante dura metade do tempo da seção de abertura, consideramos a proporção como apontando para binária com recapitulação.<'),
    (r'>In terms of the nature of the contrasting section', '>Em termos da natureza da seção contrastante'),
    (r'the melody is built from the contour of the first four notes of the first measure', 'a melodia é construída a partir do contorno das quatro primeiras notas do primeiro compasso'),
    (r'>Both the harmony and melody point us in the direction of rounded binary\.<', '>Tanto a harmonia quanto a melodia nos apontam para a direção da binária com recapitulação.<'),
    (r'>Finally, consider the era in which Beethoven lived\.', '>Finalmente, considere a época em que Beethoven viveu.'),
    (r'>Is he considered a Classical or Romantic composer\?', '>Ele é considerado um compositor Clássico ou Romântico?'),
    (r'>This is a difficult question to answer, as Beethoven is a unique figure who is a bridge between the Classical and Romantic eras\.', '>Esta é uma pergunta difícil de responder, pois Beethoven é uma figura única que é uma ponte entre as eras Clássica e Romântica.'),
    (r"However, it's generally safe to consider Beethoven as belonging to the Classical era, and therefore as likely to write a rounded binary form", 'No entanto, geralmente é seguro considerar Beethoven como pertencente à era Clássica e, portanto, provavelmente escreveria uma forma binária com recapitulação'),
    (r'>You will encounter examples on homework and the test where these three criteria are not unanimous and you will have to weigh the evidence to come to a conclusion\.<', '>Você encontrará exemplos nos exercícios e na prova onde esses três critérios não são unânimes e você terá que pesar as evidências para chegar a uma conclusão.<'),
    (r'>Occasionally you will encounter an example where the repeats are written out\.', '>Ocasionalmente, você encontrará um exemplo onde as repetições são escritas.'),
    (r'>When you encounter such a piece, put the repeats in your diagram even though there are not in the score\.<', '>Quando encontrar uma peça assim, coloque as repetições em seu diagrama, mesmo que não estejam na partitura.<'),

    # Exercícios Práticos - Binária e Ternária
    (r'>Day One<', '>Dia Um<'),
    (r'>Day Two<', '>Dia Dois<'),
    (r'>Day Three<', '>Dia Três<'),
    (r'>please fill in the blanks below the staves and diagram the form\. Also, name the form\.', '>por favor, preencha os espaços em branco abaixo das pautas e faça o diagrama da forma. Além disso, nomeie a forma.'),
    (r'>You will need to determine which notes are non-chord tones in order to determine Roman numerals\.<', '>Você precisará determinar quais notas são notas estranhas ao acorde para determinar os números romanos.<'),
    (r'>For the piece above, complete the following diagram based on your analysis\.', '>Para a peça acima, complete o seguinte diagrama com base em sua análise.'),
    (r'>Include section labels using uppercase letters, phrase labels using lowercase letters, and cadences using the abbreviations PAC, IAC, HC, DC, PC\.<', '>Inclua rótulos de seção usando letras maiúsculas, rótulos de frase usando letras minúsculas e cadências usando as abreviações PAC, IAC, HC, DC, PC.<'),
    (r'>Circle all of the terms that apply to the name of the form:<', '>Circule todos os termos que se aplicam ao nome da forma:<'),
    (r'>On scratch paper, create a diagram of the form\.', '>Em papel de rascunho, crie um diagrama da forma.'),
    (r'>Click <a class="external"', '>Clique <a class="external"'),
    (r'>here to download the first homework assignment for this chapter\.</a><', '>aqui para baixar a primeira tarefa deste capítulo.</a><'),
    (r'>here to download the second homework assignment for this chapter\.</a><', '>aqui para baixar a segunda tarefa deste capítulo.</a><'),
    (r'>here to download the third homework assignment for this chapter\.</a><', '>aqui para baixar a terceira tarefa deste capítulo.</a><'),
    (r'>here to download the review sheet for material studied prior to this chapter\.</a><', '>aqui para baixar a folha de revisão do material estudado antes deste capítulo.</a><'),
    (r'>PDF versions of the textbook, homework exercises, and practice exercises can be found at', '>Versões em PDF do livro, exercícios de tarefa e exercícios práticos podem ser encontradas em'),

    # Forma Sonata e Rondó
    (r'also known as "first-movement form," is "\[t\]he most important principle of musical form, or formal type, from the Classical period well into the 20th century," according to the Grove Music Online', 'também conhecida como "forma do primeiro movimento", é "\[o\] princípio mais importante de forma musical, ou tipo formal, do período Clássico até o século XX," de acordo com o Grove Music Online'),
    (r'>The purpose of this chapter is to serve as an introduction to formal, thematic, and harmonic aspects of sonata form\.', '>O objetivo deste capítulo é servir como uma introdução aos aspectos formais, temáticos e harmônicos da forma sonata.'),
    (r'>We will focus on sonata form as it existed during the height of the Classical era\.', '>Focaremos na forma sonata como ela existia durante o auge da era Clássica.'),
    (r'>Further and more detailed study of sonata form occurs in higher-level music theory courses\.<', '>Estudo mais aprofundado e detalhado da forma sonata ocorre em cursos de teoria musical de nível mais avançado.<'),
    (r'>Below is a generalized diagram of sonata form, which serves as our starting point\.', '>Abaixo está um diagrama generalizado da forma sonata, que serve como nosso ponto de partida.'),
    (r'>Real-world examples will contain differences and elaborations\.<', '>Exemplos do mundo real conterão diferenças e elaborações.<'),
    (r'>Exposition<', '>Exposição<'),
    (r'>Development<', '>Desenvolvimento<'),
    (r'>Recapitulation<', '>Recapitulação<'),
    (r'>It is fairly common for a piece in sonata form to have multiple secondary themes', '>É bastante comum que uma peça em forma sonata tenha múltiplos temas secundários'),
    (r'>In some sonatas, the development section features new material\.', '>Em algumas sonatas, a seção de desenvolvimento apresenta material novo.'),
    (r'>Some sonatas will not have a closing theme\.', '>Algumas sonatas não terão um tema de encerramento.'),
    (r'>As we work with real world examples, you will see the ways in which composers realize sonata form\.<', '>Ao trabalharmos com exemplos do mundo real, você verá as maneiras pelas quais os compositores realizam a forma sonata.<'),
    (r'>While the diagram above designates three large sections \(exposition, development, recapitulation\)', '>Enquanto o diagrama acima designa três grandes seções (exposição, desenvolvimento, recapitulação)'),
    (r'>repeat signs in sonatas from the classical era designate the sonata as a two-reprise form', '>os sinais de repetição em sonatas da era clássica designam a sonata como uma forma de duas reprises'),
    (r'>the exposition repeats, then the development and recapitulation repeat as a single unit', '>a exposição se repete, então o desenvolvimento e a recapitulação se repetem como uma unidade única'),

    # Sonatina
    (r'>While "sonatina" is sometimes understood to mean a short sonata or an easy sonata for beginners, in terms of form', '>Embora "sonatina" às vezes seja entendida como uma sonata curta ou uma sonata fácil para iniciantes, em termos de forma'),
    (r'>is sonata form without the development section\.', '>é a forma sonata sem a seção de desenvolvimento.'),
    (r'>Sonatina form is sometimes encountered in the second, slow movement of a larger work like a symphony, as well as in overtures\.', '>A forma sonatina às vezes é encontrada no segundo movimento, lento, de uma obra maior como uma sinfonia, bem como em aberturas.'),

    # Princípio da Sonata
    (r'>Important to sonata form is sonata principle', '>Importante para a forma sonata é o princípio da sonata'),
    (r'>The exposition of a sonata form presents the thematic material and articulates the movement from tonic to dominant', '>A exposição de uma forma sonata apresenta o material temático e articula o movimento da tônica para a dominante'),

    # Sonata Monotemática
    (r'>Haydn was especially fond of restating the Primary Theme in the dominant where the Secondary Theme would normally occur\.', '>Haydn era especialmente afeiçoado a reexpor o Tema Principal na dominante onde o Tema Secundário normalmente ocorreria.'),
    (r'>This reinforces the idea that the tonal design of a sonata was as important as thematic design\.<', '>Isso reforça a ideia de que o design tonal de uma sonata era tão importante quanto o design temático.<'),

    # Quatro Funções Estruturais
    (r'>In the "Structural Functions" chapter of', '>No capítulo "Funções Estruturais" de'),
    (r', Peter Temko and Peter Spencer enumerate four structural functions\.', ', Peter Temko e Peter Spencer enumeram quatro funções estruturais.'),
    (r'>Expository function<', '>Função expositiva<'),
    (r'>Transitional function<', '>Função de transição<'),
    (r'>Developmental function<', '>Função de desenvolvimento<'),
    (r'>Terminative function<', '>Função terminativa<'),
    (r'>Music expressing', '>Música que expressa'),
    (r'>maintains a stable tonal center and clear melodies, usually with well-defined phrases\.', '>mantém um centro tonal estável e melodias claras, geralmente com frases bem definidas.'),
    (r'>The vast majority of the music we encountered in binary and ternary form in the last chapter was expository in nature\.', '>A grande maioria da música que encontramos em forma binária e ternária no capítulo anterior era de natureza expositiva.'),
    (r'>Additionally, the primary and secondary themes in a sonata form are usually have expository function\.', '>Além disso, os temas primário e secundário em uma forma sonata geralmente têm função expositiva.'),
    (r'>Below is the secondary theme from the first movement of', '>Abaixo está o tema secundário do primeiro movimento de'),
    (r'>Notice the perfect authentic cadence that closes off this four-phrase parallel double period within the larger sonata form\.', '>Note a cadência autêntica perfeita que encerra este período duplo paralelo de quatro frases dentro da forma sonata maior.'),
    (r'>Cadences are important demarcations within a form\.<', '>As cadências são demarcações importantes dentro de uma forma.<'),
    (r'>Music of', '>Música de'),
    (r'>moves from one tonal center to another and often features a contrasting accompanimental texture more rhythmically active than preceding expository material\.', '>move de um centro tonal para outro e frequentemente apresenta uma textura de acompanhamento contrastante mais ritmicamente ativa do que o material expositivo anterior.'),
    (r'>Tonicizations may also occur within a transition\.', '>Tonicizações também podem ocorrer dentro de uma transição.'),
    (r'>Transitions are sometimes called bridges\.', '>Transições às vezes são chamadas de pontes.'),
    (r'>Mozart and Haydn often ended their sonata form transitions with a half cadence followed by a rest to signal that the secondary theme was about to commence\.', '>Mozart e Haydn frequentemente terminavam suas transições da forma sonata com uma semicadência seguida de uma pausa para sinalizar que o tema secundário estava prestes a começar.'),
    (r'>Again, notice the importance of cadences to demarcate the form\.<', '>Novamente, note a importância das cadências para demarcar a forma.<'),
    (r'>often contains sequences and fragmentation of earlier melodies\.', '>frequentemente contém sequências e fragmentação de melodias anteriores.'),
    (r'>In addition, developmental music modulates through multiple keys\.', '>Além disso, música de desenvolvimento modula através de múltiplas tonalidades.'),
    (r'>Phrase lengths may be irregular and', '>Os comprimentos das frases podem ser irregulares e'),
    (r'>elisions</a> may be used by the composer to keep the listener off balance\.<', '>elisões</a> podem ser usadas pelo compositor para manter o ouvinte desequilibrado.<'),
    (r'>It can sometimes be difficult to distinguish between transitional and developmental music\.', '>Às vezes pode ser difícil distinguir entre música de transição e de desenvolvimento.'),
    (r'>A development section is typically longer than a transition and therefore will contain more sections of a varying nature and as well as a greater number of modulations\.<', '>Uma seção de desenvolvimento é tipicamente mais longa do que uma transição e, portanto, conterá mais seções de natureza variada, bem como um maior número de modulações.<'),
    (r'>Examples from a development section can be found in', '>Exemplos de uma seção de desenvolvimento podem ser encontrados em'),
    (r'>of this text\. Note the fragmentation and sequencing of melodic ideas as well as the different keys expressed in the examples throughout that section\.<', '>deste texto. Note a fragmentação e sequenciamento de ideias melódicas, bem como as diferentes tonalidades expressas nos exemplos ao longo dessa seção.<'),
    (r'>is typically expressed through a rather emphatic alternation of tonic and dominant harmonies, usually to affirm a tonal center\.', '>é tipicamente expressa através de uma alternância bastante enfática de harmonias de tônica e dominante, geralmente para afirmar um centro tonal.'),
    (r'>The closing theme of a sonata has terminative function\.<', '>O tema de encerramento de uma sonata tem função terminativa.<'),
    (r'>Go to the <a class="internal" href="SonataAndRondoPracticeExercises\.html"', '>Vá para os <a class="internal" href="SonataAndRondoPracticeExercises.html"'),
    (r'>at the end of this chapter to practice identifying these four structural functions aurally\.<', '>no final deste capítulo para praticar a identificação dessas quatro funções estruturais auditivamente.<'),

    # Forma Rondó
    (r'>is a piece that begins with a refrain \(an A section\) that alternates with episodes \(B and C\)\.', '>é uma peça que começa com um refrão (uma seção A) que alterna com episódios (B e C).'),
    (r'>The 5-part rondo, an example of which we encountered in an earlier chapter, has ABACA form or ABABA form\.', '>O rondó de 5 partes, um exemplo do qual encontramos em um capítulo anterior, tem forma ABACA ou ABABA.'),
    (r'>The 7-part rondo typically has ABACABA form, although other designs exist\.', '>O rondó de 7 partes tipicamente tem forma ABACABA, embora outros designs existam.'),
    (r'>A diagram for 7-part Classical form is shown below\.<', '>Um diagrama para a forma clássica de 7 partes é mostrado abaixo.<'),
    (r'>The refrain \(the A section\) is always in tonic\.', '>O refrão (a seção A) está sempre na tônica.'),
    (r'>The first episode \(the B section\) was typically in a closely related key', '>O primeiro episódio (a seção B) era tipicamente em uma tonalidade próxima'),
    (r'>the dominant \(V\) if in major or the mediant \(III\) if in minor\.', '>a dominante (V) se em maior ou a mediante (III) se em menor.'),
    (r'>There was greater variety of keys used for the second episode \(the C section\)', '>Havia maior variedade de tonalidades usadas para o segundo episódio (a seção C)'),
    (r'>including tonic minor in a major sonata or the submediant \(vi or VI\)\.', '>incluindo menor homônimo em uma sonata maior ou a submediante (vi ou VI).'),
    (r'>A retransition in this case is defined as a transition returning to material previously heard\.<', '>Uma retransição neste caso é definida como uma transição retornando a material ouvido anteriormente.<'),
    (r'>Note that the B section being first stated in the dominant then later in tonic is an example of sonata principle', '>Note que a seção B sendo primeiro apresentada na dominante e depois na tônica é um exemplo do princípio da sonata'),
    (r'>An example of Classical seven-part rondo form is found below', '>Um exemplo de forma rondó clássica de sete partes é encontrado abaixo'),
    (r'>Refrain<', '>Refrão<'),
    (r'>A brief sequential transition follows, leading to the mediant', '>Uma breve transição sequencial segue, levando à mediante'),
    (r'>Transition<', '>Transição<'),
    (r'>The first episode \(the B section\) is in the mediant', '>O primeiro episódio (a seção B) está na mediante'),
    (r'>the relative major of C minor\.', '>a relativa maior de Dó menor.'),
    (r'>The primary purpose of this first episode to establish a key different than the starting key\.', '>O objetivo principal deste primeiro episódio é estabelecer uma tonalidade diferente da tonalidade inicial.'),
    (r'>Notice that the themes during this episode are not particularly tuneful\.<', '>Note que os temas durante este episódio não são particularmente melodiosos.<'),
    (r'>First Episode<', '>Primeiro Episódio<'),
    (r'>The final melody of the first episode is clearly in the form of a parallel period\.<', '>A melodia final do primeiro episódio está claramente na forma de um período paralelo.<'),
    (r'>Conclusion of First Episode<', '>Conclusão do Primeiro Episódio<'),
    (r'>A retransition follows and leads to a half cadence on a G major chord\. The refrain follows in C minor\.<', '>Uma retransição segue e leva a uma semicadência em um acorde de Sol maior. O refrão segue em Dó menor.<'),
    (r'>Retransition to Second Refrain<', '>Retransição para o Segundo Refrão<'),
    (r'>The second episode \(the C section\) follows immediately after the refrain\.', '>O segundo episódio (a seção C) segue imediatamente após o refrão.'),
    (r'>The second episode is in', '>O segundo episódio está em'),
    (r'>the submediant \(VI\) of C minor\.<', '>a submediante (VI) de Dó menor.<'),
    (r'>Second Episode<', '>Segundo Episódio<'),
    (r'>A retransition follows the second episode, ending on a half cadence on G major\.<', '>Uma retransição segue o segundo episódio, terminando em uma semicadência em Sol maior.<'),
    (r'>Retransition to Third Refrain<', '>Retransição para o Terceiro Refrão<'),
    (r'>An abbreviated version of the refrain follows, leading directly to a restatement of the second episode \(the B section\), this time in tonic major \(C major\)\.<', '>Uma versão abreviada do refrão segue, levando diretamente a uma reexposição do segundo episódio (a seção B), desta vez na tônica maior (Dó maior).<'),
    (r'>Third Refrain and Second Episode restated in tonic<', '>Terceiro Refrão e Segundo Episódio reexposto na tônica<'),
    (r'>Following the Second Episode is brief retransition that develops final motives of that episode through sequences\.<', '>Após o Segundo Episódio há uma breve retransição que desenvolve motivos finais desse episódio através de sequências.<'),
    (r'>Retransition to Final Refrain<', '>Retransição para o Refrão Final<'),
    (r'>After one last statement of the refrain in C minor, the Coda begins immediately after the cadence closing the refrain\.<', '>Após uma última exposição do refrão em Dó menor, a Coda começa imediatamente após a cadência que encerra o refrão.<'),
    (r'>Final Refrain<', '>Refrão Final<'),
    (r'>Coda<', '>Coda<'),
    (r'>To review a simple, five-part rondo form, see the section on the second movement of', '>Para revisar uma forma rondó simples de cinco partes, veja a seção sobre o segundo movimento de'),
    (r'>in the chapter on', '>no capítulo sobre'),
    (r'>Creating Contrast Between Sections</a>\.<', '>Criando Contraste Entre Seções</a>.<'),
    (r'>Sonata rondo form is a rondo in which the second episode \(the C section\) is replaced by a development section, resulting in a design of A-B-A-Dev\.-A-B-A\.<', '>A forma sonata-rondó é um rondó no qual o segundo episódio (a seção C) é substituído por uma seção de desenvolvimento, resultando em um design de A-B-A-Des.-A-B-A.<'),

    # Caráter de Rondó
    (r'>Rondo character is characterized by quick tempo in duple meter with light character, typically achieved through the use of staccato articulation\.', '>O caráter de rondó é caracterizado por andamento rápido em compasso binário com caráter leve, tipicamente alcançado através do uso de articulação staccato.'),
    (r'>This duple meter could be either simple', '>Este compasso binário pode ser simples'),
    (r'>or compound', '>ou composto'),
    (r'>During the Classical era, the final movement of a multi-movement composition, e\.g\. a sonata, quartet, or symphony, was often in rondo character\.', '>Durante a era Clássica, o movimento final de uma composição de múltiplos movimentos, por exemplo, uma sonata, quarteto ou sinfonia, era frequentemente em caráter de rondó.'),
    (r'>Not all pieces in rondo form are in rondo character\.<', '>Nem todas as peças em forma rondó estão em caráter de rondó.<'),
    (r'>Listen to the following seven examples to develop familiarity with rondo character\.<', '>Ouça os sete exemplos a seguir para desenvolver familiaridade com o caráter de rondó.<'),

    # Formas Padrão
    (r'>Below are the forms commonly encountered in the various movements of Classical symphonies, string quartets, and sonatas\.<', '>Abaixo estão as formas comumente encontradas nos vários movimentos de sinfonias, quartetos de cordas e sonatas clássicas.<'),
    (r'>First movement: Sonata form<', '>Primeiro movimento: Forma sonata<'),
    (r'>Second movement: Ternary form \(ABA\), sonatina form, or five-part rondo<', '>Segundo movimento: Forma ternária (ABA), forma sonatina ou rondó de cinco partes<'),
    (r'>Third movement: Minuet and Trio \(Compound Ternary\)<', '>Terceiro movimento: Minueto e Trio (Ternária Composta)<'),
    (r'>Fourth movement: Rondo form, sonata form, or sonata rondo form<', '>Quarto movimento: Forma rondó, forma sonata ou forma sonata-rondó<'),

    # Exercícios de Sonata e Rondó
    (r'>Identify the structural function of each excerpt below as expository, transitional, developmental, or terminative\.', '>Identifique a função estrutural de cada trecho abaixo como expositiva, de transição, de desenvolvimento ou terminativa.'),
    (r'>Aurally identify the tonic and determine if the key is maintained or if other keys occur\.', '>Identifique auditivamente a tônica e determine se a tonalidade é mantida ou se outras tonalidades ocorrem.'),
    (r'>Listen for cadences to demarcate the form\.<', '>Ouça as cadências para demarcar a forma.<'),
    (r'>Listen to the pieces below and fill in the diagrams\.', '>Ouça as peças abaixo e preencha os diagramas.'),
    (r'>Cadences and textural changes will designate the form—listen carefully for these\.<', '>Cadências e mudanças texturais designarão a forma—ouça atentamente por elas.<'),
    (r'>Expository<', '>Expositiva<'),
    (r'>Transitional<', '>De transição<'),
    (r'>Developmental<', '>De desenvolvimento<'),
    (r'>Terminative<', '>Terminativa<'),

    # Navegação
    (r'title="Previous"', 'title="Anterior"'),
    (r'title="Next"', 'title="Próximo"'),
    (r'title="Top"', 'title="Topo"'),
    (r'<span class="name">Prev</span>', '<span class="name">Ant</span>'),
    (r'<span class="name">Next</span>', '<span class="name">Próx</span>'),
    (r'<span class="name">Top</span>', '<span class="name">Topo</span>'),
    (r'>Contents<', '>Sumário<'),
    (r'>Index<', '>Índice<'),
    (r'>Search Book<', '>Pesquisar Livro<'),
    (r'>Search Results: <', '>Resultados da Pesquisa: <'),
    (r'>No results\.<', '>Sem resultados.<'),
    (r'>Search term<', '>Termo de pesquisa<'),
]

def translate_file(filepath):
    """Traduz um arquivo HTML aplicando todas as substituições."""
    print(f"Traduzindo: {filepath}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    for pattern, replacement in TRANSLATIONS:
        content = re.sub(pattern, replacement, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  Concluído: {filepath}")

def main():
    """Função principal."""
    print("Iniciando tradução dos arquivos de teoria musical...")
    print(f"Diretório: {DIR}")
    print(f"Arquivos: {len(FILES)}")
    print()

    for filename in FILES:
        filepath = os.path.join(DIR, filename)
        if os.path.exists(filepath):
            translate_file(filepath)
        else:
            print(f"  AVISO: Arquivo não encontrado: {filepath}")

    print()
    print("Tradução concluída!")

if __name__ == "__main__":
    main()
