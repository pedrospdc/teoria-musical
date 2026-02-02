##  Section 33.4 Interval Vector

An interval vector (also known as “Interval Class Content”) is a list of every possible interval occurring in a pitch-class set. Calculating an interval vector is rather straightforward. First, after determing normal form, measure from the first note to all the other notes. Second, measure from the second note to all higher notes (not back or down to the first note). Continue measuring from each successive note to the notes following and you will have completed the interval vector. 

Before demonstrating this, it is important to discuss the term “interval class.” An interval class (abbreviated “ic”) is the shortest distance between two notes measured in semitones. In the example below, C up to A is a major 6th. However, the shortest distance between C and A (measure downward) is a minor 3rd. Therefore, the largest interval class is 6 (the tritone), because any perfect 5th (for example, from C to G) has an interval class of 5 (a perfect 4th) because C _down_ to G is a perfect 4th. 

![](external/images/unit12/set-theory-interval-class-demo.svg)

With this in mind, let’s complete an interval vector of the a half-diminished 7th chord on G. First, arrange the notes in ascending order, then measure from the first note to the second, third, and fourth notes. 

![](external/images/unit12/set-theory-vector-step1.svg)

Interval Class: | 1 | 2 | 3 | 4 | 5 | 6  
---|---|---|---|---|---|---  
Occurrences | 0 | 1 | 1 | 0 | 0 | 1  
  
Second, measure from the second note to the third and fourth notes. We add one tally each for interval class (ic) 3 and 5. 

![](external/images/unit12/set-theory-vector-step2.svg)

Interval Class: | 1 | 2 | 3 | 4 | 5 | 6  
---|---|---|---|---|---|---  
Occurrences | 0 | 1 | 2 | 0 | 1 | 1  
  
Finally, measure from the third note to the fourth note, and the interval vector will be complete. We add one tally for ic4; the complete interval vector is 012011, which tells us a half-diminished chord has zero half steps, one major 2nd (shown in this voicing as a minor 7th), two minor 3rds, no major 3rds, one perfect 4th (shown in this voicing as perfect 5th), and one tritone. 

![](external/images/unit12/set-theory-vector-step3.svg)

Interval Class: | 1 | 2 | 3 | 4 | 5 | 6  
---|---|---|---|---|---|---  
Occurrences | 0 | 1 | 2 | 1 | 1 | 1  
  
An interval vector always contains 6 digits. When an interval class does not occur (the way the minor second did not occur in the G half-diminished seventh chord), place a zero in the column for that interval class.
