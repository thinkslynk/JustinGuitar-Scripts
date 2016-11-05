#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script uses handbrake cli to extract mp4s from the isos provided on justinguitar.com"""

import os
import sys
import subprocess

MENU_OPTIONS = [
    {'name': "The Beginner's Course", 'discs': [
        ["00. Copyright",
         "01. Intro",
         "02. Common Questions",
         "03. What  guitar should I buy",
         "04. What accessories do I need",
         "05. Guitar Anatomy",
         "06. Make the most of your practice time",
         "07. Body posture and finger placement",
         "08. Picks - How to choose one and hold it",
         "09. Reading TAB and Chord Boxes",
         "10. Get your guitar in tune",
         "11. The D Chord",
         "12. The A Chord",
         "13. The E Chord",
         "14. Anchor Fingers",
         "15. One Minute Changes",
         "16. 4-4 All Down Rhythm",
         "17. Stage 1 Practice Schedule",
         "18. The A minor Chord",
         "19. The E minor Chord",
         "20. The D minor Chord",
         "21. One Minute Changes",
         "22. Introducing the Metronome",
         "23. Foot Tapping (How and Why)",
         "24. Stage 2 Practice Schedule"],

        ["00. Copyright",
         "01. The G Chord",
         "02. The C Chord",
         "03. Names of Open Strings",
         "04. One Minute Changes",
         "05. Basic Finger Workout",
         "06. Rhythm Guitar Basics 1",
         "07. Stage 3 Practice Schedule",
         "08. G7 C7 and B7 Chords",
         "09. The F Maj 7 Chord",
         "10. The A Chord…again",
         "11. One Minute Changes",
         "12. Forcing the Changes",
         "13. Rhythm Guitar Basics 2",
         "14. Stage 4 Practice Schedule",
         "15. A7 D7 and E7 Chords",
         "16. The Note Circle",
         "17. Air Changes",
         "18. One Minute Changes",
         "19. Triplet Rhythms",
         "20. Rhythm Guitar Basics 3",
         "21. Stage 5 Practice Schedule"],

        ["00. Copyright",
         "01. The Dreaded F Chord",
         "02. One Minute Changes",
         "03. Using a Capo",
         "04. Action and Basic Guitar Setup",
         "05. Rhythm Guitar Basics 4",
         "06. Picking Individual Strings",
         "07. Stage 6 Practice Schedule",
         "08. Notes in the Open Position",
         "09. Power Chords 1",
         "10. Asus2 Asus4 Dsus2 Dsus4 Esus4 Chords",
         "11. One Minute Changes",
         "12. Rhythm Guitar Basics 5",
         "13. Minor Pentatonic Scale",
         "14. Stage 7 Practice Schedule",
         "15. G Chord Variations",
         "16. One Minute Changes",
         "17. 12 Bar Blues Style",
         "18. Basic Fingerstyle Exercise",
         "19. Minor Pentatonic Picking Exercises",
         "20. Power Chords 2",
         "21. Stage 8 Practice Schedule"],

        ["01. Easy Slash Chords",
         "02. Power Chord Shifts and Palm Mutes",
         "03. Applied Fingerstyle Patterns",
         "04. 12 Bar Blues Variations",
         "05. Minor Pentatonic Patterns",
         "06. Basic Blues Improvisations",
         "07. Consolidation and Practice Schedule",
         "08. Extras — One minute changes",
         "09. Extras —Bloopers Reel",
         "10. Extras — BLUES LEAD GUITAR 1 DVD — Introduction",
         "11. Extras — BLUES LEAD GUITAR 1 DVD — Blues Scales",
         "12. Extras — BLUES LEAD GUITAR 1 DVD — Five Licks",
         "13. Extras — MASTER THE MAJOR SCALE DVD — Introduction",
         "14. Extras — MASTER THE MAJOR SCALE DVD — G Major Scale Position 1",
         "15. Extras — MASTER THE MAJOR SCALE DVD — Exploring Position 1",
         "16. Extras — Solo Blues Acoustic Piece — Intro and Demo",
         "17. Extras — Solo Blues Acoustic Piece — Section 1",
         "18. Extras — Solo Blues Acoustic Piece — Section 2",
         "19. Extras — Solo Blues Acoustic Piece — Section 3",
         "20. Extras — Solo Blues Acoustic Piece — Section 4",
         "21. Extras — Solo Blues Acoustic Piece — Section 5",
         "22. Extras — Solo Blues Acoustic Piece — Slow Version",
         "23. Extras — Solo Blues Acoustic Piece — Medium Version",
         "24. Extras — Solo Blues Acoustic Piece — Full speed Version"]
    ]},

    {'name': "Really Useful Strumming Techniques 1", 'discs': [
        ["00. Copyright",
         "01. Introduction",
         "02. Plectrums",
         "03. Holding The Pick",
         "04. Posture",
         "05. Dynamics",
         "06. Theory Basic Principles",
         "07. Strumming Patterns 1 - 4",
         "08. Strumming Patterns 1",
         "09. Strumming Patterns 2",
         "10. Strumming Patterns 3",
         "11. Strumming Patterns 4",
         "12. Working With A Metronome",
         "13. Strumming Patterns 5 - 8",
         "14. Strumming Patterns 5",
         "15. Strumming Patterns 6",
         "16. Strumming Patterns 7",
         "17. Strumming Patterns 8",
         "18. Muting Unwanted Strings",
         "19. Chord Changing Trick",
         "20. Ties",
         "21. Strumming Patterns 9 - 12",
         "22. Strumming Patterns 9",
         "23. Strumming Patterns 10",
         "24. Strumming Patterns 11",
         "25. Strumming Patterns 12",
         "26. Extended Ties",
         "27. Strumming Patterns 13 - 15",
         "28. Strumming Patterns 13",
         "29. Strumming Patterns 14",
         "30. Strumming Patterns 15",
         "31. Pick The Bass",
         "32. Strumming Patterns 16",
         "33. Strumming Patterns 17",
         "34. Strumming Patterns 18",
         "35. Exploding Dynamics",
         "36. Percussive Playing",
         "37. Strumming Patterns 19",
         "38. Strumming Patterns 20",
         "39. 16th Notes In Brief",
         "40. Outro"]
    ]}]

QUALITY_OPTIONS = [
    {'name': 'HQ', 'profile': 'High Profile', 'format': 'mp4'},
    {'name': 'Mobile', 'profile': 'iPhone & iPod touch', 'format': 'mp4'}]


def printRootMenu():
    for i in range(0, len(MENU_OPTIONS)):
        print("\t" + str(i) + ") " + MENU_OPTIONS[i]['name'])

    # Get input
    optionInput = raw_input("\nWhich series would you like to export? ")

    try:
        return MENU_OPTIONS[int(optionInput)]['discs']
    except ValueError:
        print("Unable to process input: " + optionInput)
        sys.exit(1)
    except IndexError:
        print("Invalid option: " + optionInput)
        sys.exit(1)


def printDiscMenu(discs):

    disc = discs[0]

    # See if we need to ask which disc is being used
    if len(discs) > 1:
        optionInput = raw_input("\nWhich disc(1-" + str(len(discs)) + ")? ")
        try:
            disc = discs[int(optionInput) - 1]
        except ValueError:
            print("Unable to process input: " + optionInput)
            sys.exit(1)
        except IndexError:
            print("Invalid option: " + optionInput)
            sys.exit(1)

    return disc


def printQualityMenu():
    for i in range(0, len(QUALITY_OPTIONS)):
        print("\t" + str(i) + ") " + QUALITY_OPTIONS[i]['name'])

    # Get input
    optionInput = raw_input("\nWhich quality? ")

    try:
        return QUALITY_OPTIONS[int(optionInput)]
    except ValueError:
        print("Unable to process input: " + optionInput)
        sys.exit(1)
    except IndexError:
        print("Invalid option: " + optionInput)
        sys.exit(1)


def export(chapters, quality, source, destination):

    i = 0
    for c in chapters:
        i += 1
        out = os.path.join(destination, str(c) + '.' + str(quality['format']))
        cmd = ('handbrakecli -i ' +
               str(source) + ' -t 1 -c ' + str(i) +
               ' -o "' + out +
               '" -Z "' + str(quality['profile']) + '"')

        subprocess.check_output(cmd, shell=True)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: ' + sys.argv[0] + ' source outputDirectory')
        sys.exit(1)

    discs = printRootMenu()
    chapters = printDiscMenu(discs)
    quality = printQualityMenu()

    export(chapters, quality, sys.argv[1], sys.argv[2])
