# Example usage of WIWU
# Run this file to test the library!

import WIWU
from WIWU import Song

# --- Example 1: Simple melody ---
print("=== Example 1: Simple Melody ===")
song = Song(tempo=120)

song.add_note("C4")
song.add_note("D4")
song.add_note("E4")
song.add_note("F4")
song.add_note("G4")
song.add_note("A4")
song.add_note("B4")
song.add_note("C5")

song.save("scale.wav")

# --- Example 2: Twinkle Twinkle ---
print("\n=== Example 2: Twinkle Twinkle ===")
twinkle = Song(tempo=100)

twinkle.add_note("C4")
twinkle.add_note("C4")
twinkle.add_note("G4")
twinkle.add_note("G4")
twinkle.add_note("A4")
twinkle.add_note("A4")
twinkle.add_note("G4", 2.0)  # Hold for 2 beats

twinkle.add_note("F4")
twinkle.add_note("F4")
twinkle.add_note("E4")
twinkle.add_note("E4")
twinkle.add_note("D4")
twinkle.add_note("D4")
twinkle.add_note("C4", 2.0)  # Hold for 2 beats

twinkle.save("twinkle.wav")

# --- Example 3: Chords ---
print("\n=== Example 3: Chords ===")
chords = Song(tempo=80)

chords.add_chord(["C4", "E4", "G4"])   # C major
chords.add_chord(["F4", "A4", "C5"])   # F major
chords.add_chord(["G4", "B4", "D5"])   # G major
chords.add_chord(["C4", "E4", "G4"])   # C major

chords.save("chords.wav")

print("\n🎉 All examples saved! Check your files folder for the .wav files")
