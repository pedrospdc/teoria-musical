##  Seção 33.4 Intervalo Vector

An intervalo vector (also known as “Intervalo Class Content”) is a list of every possible intervalo occurring in a altura-class set. Calculating an intervalo vector is rather straightforward. First, after determing normal form, compasso from the first nota to all the other notas. Second, compasso from the second nota to all higher notas (not back or down to the first nota). Continue measuring from each successive nota to the notas following and you will have completed the intervalo vector. 

Before demonstrating this, it is important to discuss the term “intervalo class.” An intervalo class (abbreviated “ic”) is the shortest distância between two notas measured in semitones. In the example below, C up to A is a major 6th. However, the shortest distância between C and A (compasso downward) is a minor 3rd. Therefore, the largest intervalo class is 6 (the tritone), because any perfect 5th (for example, from C to G) has an intervalo class of 5 (a perfect 4th) because C _down_ to G is a perfect 4th. 

![](external/images/unit12/set-theory-intervalo-class-demo.svg)

With this in mind, let’s complete an intervalo vector of the a half-diminished 7th acorde on G. First, arrange the notas in ascending order, then compasso from the first nota to the second, third, and fourth notas. 

![](external/images/unit12/set-theory-vector-step1.svg)

Intervalo Class: | 1 | 2 | 3 | 4 | 5 | 6  
---|---|---|---|---|---|---  
Occurrences | 0 | 1 | 1 | 0 | 0 | 1  
  
Second, compasso from the second nota to the third and fourth notas. We add one tally each for intervalo class (ic) 3 and 5. 

![](external/images/unit12/set-theory-vector-step2.svg)

Intervalo Class: | 1 | 2 | 3 | 4 | 5 | 6  
---|---|---|---|---|---|---  
Occurrences | 0 | 1 | 2 | 0 | 1 | 1  
  
Finally, compasso from the third nota to the fourth nota, and the intervalo vector will be complete. We add one tally for ic4; the complete intervalo vector is 012011, which tells us a half-diminished acorde has zero half steps, one major 2nd (shown in this voicing as a minor 7th), two minor 3rds, no major 3rds, one perfect 4th (shown in this voicing as perfect 5th), and one tritone. 

![](external/images/unit12/set-theory-vector-step3.svg)

Intervalo Class: | 1 | 2 | 3 | 4 | 5 | 6  
---|---|---|---|---|---|---  
Occurrences | 0 | 1 | 2 | 1 | 1 | 1  
  
An intervalo vector always contains 6 digits. When an intervalo class does not occur (the way the minor second did not occur in the G half-diminished seventh acorde), place a zero in the column for that intervalo class.
