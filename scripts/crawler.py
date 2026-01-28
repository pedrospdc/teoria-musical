#!/usr/bin/env python3
"""
Crawler para baixar todas as páginas do site Music Theory for the 21st-Century Classroom
"""

import os
import re
import time
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from pathlib import Path

BASE_URL = "https://musictheory.pugetsound.edu/mt21c/"
OUTPUT_DIR = Path(__file__).parent.parent / "original"

# Lista de páginas conhecidas do site
PAGES = [
    "MusicTheory.html",
    "frontmatter.html",
    "frontmatter-3.html",
    "frontmatter-4.html",
    "frontmatter-5.html",
    # Chapter 1: Basic Concepts
    "BasicConcepts.html",
    "Pitch.html",
    "Notation.html",
    "OctaveRegisters.html",
    "Accidentals.html",
    "EnharmonicNotes.html",
    "BasicConceptsPracticeExercises.html",
    # Chapter 2: Major Scales and Key Signatures
    "MajorScalesAndKeySignatures.html",
    "HalfStepsAndWholeSteps.html",
    "TheMajorScale.html",
    "MajorKeySignatures.html",
    "MajorKeysPracticeExercises.html",
    # Chapter 3: Minor Scales and Key Signatures
    "MinorScalesAndKeySignatures.html",
    "MinorScales.html",
    "MinorKeySignatures.html",
    "ScaleDegreeNames.html",
    "MinorKeysPracticeExercises.html",
    # Chapter 4: Basics of Rhythm
    "BasicsOfRhythm.html",
    "TimeSignature.html",
    "DurationalSymbols.html",
    "DotsAndTies.html",
    "meter.html",
    "Tuplets.html",
    "CommonRhythmicNotationErrors.html",
    "BasicsOfRhythmPracticeExercises.html",
    # Chapter 5: Intervals
    "Intervals.html",
    "IntervalsIntroduction.html",
    "HowToIdentifyIntervals.html",
    "HowToWriteIntervals.html",
    "InversionOfIntervals.html",
    "AugmentedAndDiminishedIntervals.html",
    "IntervalsPracticeExercises.html",
    # Chapter 6: Triads
    "Triads.html",
    "TriadsIntroduction.html",
    "LeadSheetSymbols.html",
    "InvertedTriads.html",
    "AnalyzingChords.html",
    "SimpleSusChords.html",
    "SummaryOfTriadConstruction.html",
    "TriadsPracticeExercises.html",
    # Chapter 7: Roman Numerals and Cadences
    "RomanNumeralsAndCadences.html",
    "RomanNumeralChordSymbols.html",
    "DiatonicChordsInMajor.html",
    "DiatonicChordsInMinor.html",
    "cadences.html",
    "RomanNumeralPracticeExercises.html",
    # Chapter 8: Seventh Chords
    "SeventhChords.html",
    "SeventhChordsIntroduction.html",
    "IVover5SusChord.html",
    "RomanNumeralsOfDiatonicSeventhChords.html",
    "SeventhChordsExercises.html",
    # Chapter 9: Harmonic Progression
    "HarmonicProgression.html",
    "CircleOfFifths.html",
    "HarmonicRhythm.html",
    "ShorterProgressionsFromTheCircleOfFifths.html",
    "HarmonicFunction.html",
    "ExceptionsCreatedBySequences.html",
    "SubtonicVIIinPopMusic.html",
    "BestsellerProgression.html",
    "i-VII-VI-VII.html",
    "HarmonicProgressionExercises.html",
    # Chapter 10: Non-Chord Tones
    "NonChordTones.html",
    "NonChordTonesIntroduction.html",
    "PassingTones.html",
    "NeighborTones.html",
    "Appoggiatura.html",
    "EscapeTone.html",
    "DoubleNeighbor.html",
    "Anticipation.html",
    "PedalPoint.html",
    "Suspension.html",
    "Retardation.html",
    "IncompleteNeighbor.html",
    "NonChordTonesPracticeExercises.html",
    # Chapter 11: Melodic Analysis
    "MelodicAnalysis.html",
    "MotiveSection.html",
    "MelodicAlteration.html",
    "FragmentSection.html",
    "PhraseSection.html",
    "subphrase.html",
    "MelodicAnalysisPracticeExercises.html",
    # Chapter 12: Form in Popular Music
    "FormInPopularMusic.html",
    "VerseChorusForm.html",
    "AABAForm.html",
    "ABACForm.html",
    "TwelveBarBlues.html",
    "HarmonicallyClosedAndOpenSections.html",
    "PopFormPracticeExercises.html",
    # Chapter 13: Phrases in Combination
    "PhrasesInCombination.html",
    "PerfectAuthenticCadence.html",
    "SentenceStructure.html",
    "PeriodForm.html",
    "AsymmetricalPeriod.html",
    "DoublePeriodForm.html",
    "PhraseGroupsAndPhraseChains.html",
    "Elision.html",
    "SummaryOfPhrasesInCombination.html",
    "PhrasesInCombinationPracticeExercises.html",
    # Chapter 14: Accompanimental Textures
    "AccompanimentalTexture.html",
    "Texture.html",
    "ChoraleTexture.html",
    "ArpeggiatedAccompaniments.html",
    "BlockChordAccompaniments.html",
    "AfterbeatsOffbeats.html",
    "ThreeTwoClave.html",
    "DistinctiveBassLines.html",
    # Chapter 15: Creating Contrast
    "CreatingContrast.html",
    "The-Elements-of-Music.html",
    "Eine-kleine-ii.html",
    "CreatingContrast-5.html",
    # Chapter 16: Figured Bass
    "FiguredBass.html",
    "FiguredBassHistoricalContext.html",
    "FiguredBassInversionSymbols.html",
    "TheCadentialSixFourChord.html",
    "OtherOccurrencesofSixFourChords.html",
    "FiguredBassAdditionalInformation.html",
    "FiguredBassPracticeExercises.html",
    # Chapter 17: Secondary Dominants
    "SecondaryDominants.html",
    "ExamplesWithSecondaryDominants.html",
    "Tonicization.html",
    "SecondaryDominantsInMajorAndMinor.html",
    "AnalyzingSecondaryDominants.html",
    "WritingSecondaryDominants.html",
    "IrregularResoltionsOfSecondaryDominants.html",
    "SecondaryDominantPracticeExercises.html",
    # Chapter 18: Secondary Diminished Chords
    "SecondaryDiminishedChords.html",
    "SecondaryDiminishedChordSection.html",
    "SecondaryDiminishedChordsInMajorAndMinor.html",
    "AnalyzingSecondaryDiminishedChords.html",
    "WritingSecondaryDiminishedChords.html",
    "SecondaryDiminishedPracticeExercises.html",
    # Chapter 19: Mode Mixture
    "ModeMixture.html",
    "ModeMixtureSection.html",
    "HarmonizationOfBorrowedScaleDegrees.html",
    "AnalyzingAndWritingBorrowedChords.html",
    "TheDeceptiveCadenceWithFlatSix.html",
    "Picardy3rd.html",
    "ModeMixturePracticeExercises.html",
    # Chapter 20: Neapolitan
    "Neapolitan.html",
    "NeapolitanIntroduction.html",
    "ExamplesOfTheNeapolitanChord.html",
    "NeapolitanPracticeExercises.html",
    # Chapter 21: Augmented Sixth Chords
    "AugmentedSixthChords.html",
    "AugmentedSixthIntroduction.html",
    "TypesOfAugmentedSixthChords.html",
    "AnalyzingAugmentedSixthChords.html",
    "LeadSheetAnalysisOfAugmentedSixthChords.html",
    "ExamplesWithAugmentedSixthChords.html",
    "DistinguishingBetweenChromaticHarmonies.html",
    "DescendingChromaticBassLines.html",
    "ChromaticPreDominantChords.html",
    "AugmentedSixthPracticeExercises.html",
    # Chapter 22: Modulation
    "Modulation.html",
    "ModulationIntroduction.html",
    "TonicizationVersusModulation.html",
    "KeyRelationships.html",
    "ModulationsWithDiatonicPivotChords.html",
    "HowToRecognizeAKeyAfterAModulation.html",
    "ModulationsWithChromaticPivotChords.html",
    "ModulationsWithoutPivotChords.html",
    "ModulationPracticeExercises.html",
    # Chapter 23: Enharmonic Modulation
    "EnharmonicModulation.html",
    "EnharmonicModulationIntroduction.html",
    "TheV7andGer6asPivotChords.html",
    "TheFullyDiminishedSeventhAsPivotChord.html",
    "EnharmonicModulationPracticeExercises.html",
    # Chapter 24: Binary and Ternary Forms
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
    # Chapter 25: Sonata and Rondo Forms
    "SonataAndRondoForms.html",
    "SonataIntroduction.html",
    "FourStructuralFunctions.html",
    "RondoForm.html",
    "RondoCharacter.html",
    "SonataAndRondoForms-6.html",
    "SonataAndRondoPracticeExercises.html",
    # Chapter 26: Voice Leading Triads
    "VoiceLeadingTriads.html",
    "VoiceLeading.html",
    "TypesOfMotion.html",
    "ObjectionableParallels.html",
    "VoiceRanges.html",
    "RulesOfMelody.html",
    "RulesOfSpacing.html",
    "VoiceLeadingFourPartsRootPosition.html",
    "VoiceLeadingFirstInversionTriads.html",
    "VoiceLeadingSecondInversionTriads.html",
    "SpecialSituations.html",
    "TypesOfSixFourChords.html",
    "SummaryOfDoublingRules.html",
    "VoiceLeadingTriadsPracticeExercises.html",
    # Chapter 27: Voice Leading Seventh Chords
    "VoiceLeadingSeventhChords.html",
    "VoiceLeadingSeventhChordsIntro.html",
    "SuccessiveSeventhChords.html",
    "V7toIVoiceLeading.html",
    "SpecialResolutionOfVII7.html",
    "WhenToUseSeventhChords.html",
    "VoiceLeading7thChordsPracticeExercises.html",
    # Chapter 28: Voice Leading with NCTs
    "VoiceLeadingNCTs.html",
    "VoiceLeadingNCTsIntro.html",
    "AvoidingObjectionableParallels.html",
    "AddingsNCTs.html",
    "VoiceLeadingNCTsPracticeExercises.html",
    # Chapter 29: Voice Leading Chromatic Harmonies
    "VoiceLeadingChromaticHarmonies.html",
    "VoiceLeadingSecondaryChords.html",
    "VoiceLeadingBorrowedChords.html",
    "VoiceLeadingNeapolitanChord.html",
    "VoiceLeadingAugmentedSixthChords.html",
    "VoiceLeadingChromaticHarmoniesExercises.html",
    # Chapter 30: Counterpoint
    "IntroductionToCounterpoint.html",
    "SpeciesCounterpoint.html",
    "FirstSpecies.html",
    "SecondSpecies.html",
    "ThirdSpecies.html",
    "FourthSpecies.html",
    "FifthSpecies.html",
    "InventionExpositions.html",
    "FugueAnalysis.html",
    "IntroductionToCounterpointExercises.html",
    # Chapter 31: Jazz Theory
    "IntroductionToJazzTheory.html",
    "JazzChordBasics.html",
    "ChordSymbolSpecifics.html",
    "AlteredDominantSeventhChords.html",
    "ChordLabels.html",
    "HowToWriteJazzChords.html",
    "HowToAnalyzeJazzChords.html",
    "JazzChordVoicings.html",
    "StandardChordProgressions.html",
    "JazzScales.html",
    "HowToDetermineChord-ScaleRelationships.html",
    "harmonizing-bebop-scale.html",
    "JazzExercises.html",
    # Chapter 32: Impressionism
    "ImpressionismAndExtendedTonality.html",
    "Impressionism.html",
    "Pandiatonicism.html",
    "QuintalHarmony.html",
    "polychords.html",
    "Impressionism-Practice-Exercises.html",
    # Chapter 33: Set Theory
    "SetTheory.html",
    "SetTheorySection.html",
    "NormalForm.html",
    "PrimeForm.html",
    "IntervalVector.html",
    "ForteNumbers.html",
    "ListsOfSetClasses.html",
    "TranspositionTn.html",
    "InversionTnI.html",
    "Set-Theory-Practice-Exercises.html",
    # Chapter 34: Serialism
    "Serialism.html",
    "TwelveToneTechnique.html",
    "DeterminingRowForms.html",
    "WritingRowForms.html",
    "Serialism-6.html",
    "RowFormsInMusic.html",
    "NonTwelveToneSerialism.html",
    "SerialismExercises.html",
    # Chapter 35: Minimalism
    "Minimalism.html",
    "AdditiveMinimalism.html",
    "PhaseShifting.html",
    "Minimalism-5.html",
    # Back Matter
    "backmatter.html",
    "backmatter-2.html",
    "appendix-gfdl.html",
    "backmatter-4.html",
    "backmatter-5.html",
]

def download_page(url, output_path):
    """Baixa uma página e salva no disco"""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(response.text)
        return True
    except Exception as e:
        print(f"Erro ao baixar {url}: {e}")
        return False

def find_all_links(html_content, base_url):
    """Encontra todos os links internos em uma página"""
    soup = BeautifulSoup(html_content, 'html.parser')
    links = set()
    for a in soup.find_all('a', href=True):
        href = a['href']
        if href.endswith('.html') and not href.startswith('http'):
            links.add(href)
    return links

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    downloaded = set()
    to_download = set(PAGES)

    print(f"Iniciando download de {len(to_download)} páginas...")

    total = len(to_download)
    count = 0

    for page in sorted(to_download):
        if page in downloaded:
            continue

        url = urljoin(BASE_URL, page)
        output_path = OUTPUT_DIR / page

        count += 1
        print(f"[{count}/{total}] Baixando {page}...")

        if download_page(url, output_path):
            downloaded.add(page)
            # Pequeno delay para não sobrecarregar o servidor
            time.sleep(0.5)
        else:
            print(f"  FALHA: {page}")

    print(f"\nDownload concluído! {len(downloaded)} páginas baixadas para {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
