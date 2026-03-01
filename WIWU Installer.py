import subprocess
import sys

print(“🎵 Installing WIWU…”)
subprocess.check_call([sys.executable, “-m”, “pip”, “install”, “–upgrade”, “WIWU”])

print(”\n🎵 Running WIWU demo…”)

import WIWU

song = WIWU.Song(tempo=120)

song.add_note(“C4”)
song.add_note(“E4”)
song.add_note(“G4”)
song.add_note(“C5”, 2.0)

song.add_chord([“C4”, “E4”, “G4”], 2.0)

song.save(“wiwu_demo.wav”)

print(”\n✅ Done! Check for wiwu_demo.wav in your folder!”)