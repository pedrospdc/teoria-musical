##  Section 33.1 Set Theory

Set theory is the analytical technique we will use to analyze expressionist music. The primary composers associated with expressionism are Arnold Schoenberg (1874–1951), Anton Webern (1883–1945), and Alban Berg (1885–1935). In this text, we will associate atonal music—music that avoids traditional harmonies and scales—with expressionism. Instead of scales and chords, intervals are the building blocks of Expressionist music. Although composers began writing atonal music in 1908, there was no widely-accepted systematic analytical approach that could show relationships between different pieces until Allen Forte published his seminal The Structure of Atonal Music in 1973, in which Forte applied set theory mathematics to music. However, our approach to normal form and prime form will follow the slightly-modified approach set out by John Rahn in his Basic Atonal Theory (1980), which is the approach followed by Joseph Straus in his well-known and widely-used Introduction to Post-Tonal Theory. 1 

Of the 208 sets that exist, only 6 are different between the Forte and Rahn methods for prime form. See <https://www.mta.ca/pc-set/pc-set_new/pages/pc-table/packed.html>.

###  Subsection 33.1.1 Atonal Music

Listen to the following example by Anton Webern. 

Figure 33.1.1. Webern, 5 movements for string quartet, No. 3. _Sehr bewegt_

Gone are the triadic structures we have studied throughout this text. In this music, intervals are paramount. Let us examine the intervals we find. 

![](external/images/unit12/set-theory-webern-op5no3-ex-1.svg)

Look at the intervallic structure of the first two chords, 2 

Some authors call atonal chords “sonorities” to differentiate them from chords in the traditional triadic sense; we will continue to use “chord” in this text.

not including the C♯ in the cello part. We see the interval of an augmented 5th below the interval of a minor 3rd in the first chord, and the interval of a minor sixth below the interval of a minor 3rd in the second chord. Notice that the names we use for intervals carry tonal implications. An augmented 5th would function differently than a minor 6th, but in atonal music, these intervals have the same sound, are separated by the same number of half steps, and have no tonal implications (they don’t have to resolve any particular way). Therefore, analysts like Allen Forte used integers to represent pitches and intervals to remove the tonal implications of staff notation. 

###  Subsection 33.1.2 Integer Notation for Pitches

One notable trait of set theory is that we will represent pitches with integers, as seen in the table below. 

Note name: | C | C♯/D♭ | D | D♯/E♭ | E | F | F♯/G♭ | G | G♯/A♭ | A | A♯/B♭ | B  
---|---|---|---|---|---|---|---|---|---|---|---|---  
Integer: | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11  
  
It may be helpful to remember that the C major triad (C, E, and G) consists of integers 0, 4, and 7. 

Integer notation of pitches means we assume enharmonic equivalence of notes. For example, D, C𝄪, and E𝄫 are all represented as pitch integer 2. We also assume octave equivalence, which itself presumes the notion of pitch class. When we say Beethoven’s first symphony is in C, we refer not to any specific C (\\(\text{C}_{1}\\), \\(\text{C}_{2}\\), \\(\text{C}_{3}\\), etc.), but to the concept of the pitch class C, which includes any and all Cs. Therefore, you would label the note C as pitch class 0, no matter the register in which it occurs. 

###  Subsection 33.1.3 Integer Notation for Intervals

We will also measure intervals using integers, with each interval represented by the number of semitones (half steps) it contains. The following table contains the number of semitones in each interval. 

Table 33.1.2. Interval Integers

Interval | Number of Semitones | Interval | Number of Semitones  
---|---|---|---  
m2 | 1 | P5 | 7  
M2 | 2 | m6 | 8  
m3 | 3 | M6 | 9  
M3 | 4 | m7 | 10  
P4 | 5 | M7 | 11  
TT | 6 | P8 | 12  
  
###  Subsection 33.1.4 Pitch-Class Sets

In atonal music we will analyze sets of pitch classes, hence the term “pitch-class set analysis.” Let us return to the example by Webern, this time with integers for pitches and for intervals. 

![](external/images/unit12/set-theory-webern-op5no3-ex-2.svg)

The first chord consists of E♭, B, and D, or pitch integers 3, 11, and 2. If we examine the intervallic distance, we find 8 semitones between pitch integers 3 and 11, and 3 semitones between 11 and 2. Note that we are working in a modulo 12 system, meaning we restart our numbering after 11 (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 1, 2, 3, etc.). We are used to modulo 12 thinking since we all deal with clocks. If a meeting ran from 11am to 2pm, it lasted 3 hours. Therefore, an interval from pitch integer 11 to pitch integer 2 spans 3 semitones. The second chord has the same intervallic construction. 

Now, let’s look at the two chords in the second half of the third measure. 

![](external/images/unit12/set-theory-webern-op5no3-ex-3.svg)

We see right away that the second of these chords has the same construction as the two chords we examined the in earlier examples (a minor 6th below a minor 3rd). However, the first chord in this example (G♯, C, A, or 8, 0, 9) appears to be different, with a diminished 4th from G♯ to C (an interval spanning 4 semitones, enharmonically equivalent to a major 3rd) below the interval of a major 6th from C to A (spanning 9 semitones). To see the relationship of this chord to the others, we need to learn about normal form and prime form.
