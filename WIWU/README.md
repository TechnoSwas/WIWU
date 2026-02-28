# 🎵 WIWU - Make Music With Code!

WIWU lets you code music using note names like C4, A#3, Gb5 and save them as audio files!

## Installation

```
pip install WIWU
```

## Quick Start

```python
import WIWU

song = WIWU.Song()
song.add_note("C4")
song.add_note("E4")
song.add_note("G4")
song.save("mysong.wav")
```

---

## Note Format

Notes are written as the **note name + octave number**:

| Note | Example | Description |
|------|---------|-------------|
| C | `C4` | Middle C |
| A | `A4` | Concert A (440 Hz) |
| F# | `F#3` | F sharp in octave 3 |
| Bb | `Bb5` | B flat in octave 5 |

**Valid notes:** C, C#, Db, D, D#, Eb, E, F, F#, Gb, G, G#, Ab, A, A#, Bb, B

**Octaves:** 1 (very low) to 7 (very high). Octave 4 is middle range.

---

## Methods

### `Song(tempo=120, volume=0.5)`
Create a new song.
```python
song = WIWU.Song()              # default 120 BPM
song = WIWU.Song(tempo=80)      # slow
song = WIWU.Song(tempo=180)     # fast
```

### `song.add_note(note, duration=1.0)`
Add a single note. Duration is in beats.
```python
song.add_note("C4")        # one beat
song.add_note("G4", 0.5)   # half beat (short)
song.add_note("E5", 2.0)   # two beats (long)
```

### `song.add_rest(duration=1.0)`
Add silence.
```python
song.add_rest()       # one beat of silence
song.add_rest(2.0)    # two beats of silence
```

### `song.add_chord(notes, duration=1.0)`
Play multiple notes at the same time!
```python
song.add_chord(["C4", "E4", "G4"])        # C major chord
song.add_chord(["A3", "C4", "E4"])        # A minor chord
song.add_chord(["C4", "E4", "G4"], 2.0)   # held for 2 beats
```

### `song.save(filename)`
Save your song as a WAV audio file.
```python
song.save("mysong.wav")
song.save("C:/Users/YourName/Desktop/mysong.wav")  # save to specific location
```

### `song.preview()`
Show song info without saving.
```python
song.preview()
```

---

## Chords Guide

A chord is multiple notes played at the same time. Here are some common chords:

### Major Chords (happy sound)
```python
song.add_chord(["C4", "E4", "G4"])   # C major
song.add_chord(["F4", "A4", "C5"])   # F major
song.add_chord(["G4", "B4", "D5"])   # G major
song.add_chord(["D4", "F#4", "A4"])  # D major
```

### Minor Chords (sad sound)
```python
song.add_chord(["A3", "C4", "E4"])   # A minor
song.add_chord(["D4", "F4", "A4"])   # D minor
song.add_chord(["E4", "G4", "B4"])   # E minor
```

### Example - Chord Progression
```python
import WIWU

song = WIWU.Song(tempo=80)

song.add_chord(["C4", "E4", "G4"], 2.0)   # C major
song.add_chord(["A3", "C4", "E4"], 2.0)   # A minor
song.add_chord(["F4", "A4", "C5"], 2.0)   # F major
song.add_chord(["G4", "B4", "D5"], 2.0)   # G major

song.save("chords.wav")
```

---

## Example Songs

### C Major Scale
```python
import WIWU

song = WIWU.Song()
song.add_note("C4")
song.add_note("D4")
song.add_note("E4")
song.add_note("F4")
song.add_note("G4")
song.add_note("A4")
song.add_note("B4")
song.add_note("C5")
song.save("scale.wav")
```

### Twinkle Twinkle Little Star
```python
import WIWU

song = WIWU.Song(tempo=100)
song.add_note("C4")
song.add_note("C4")
song.add_note("G4")
song.add_note("G4")
song.add_note("A4")
song.add_note("A4")
song.add_note("G4", 2.0)
song.add_note("F4")
song.add_note("F4")
song.add_note("E4")
song.add_note("E4")
song.add_note("D4")
song.add_note("D4")
song.add_note("C4", 2.0)
song.save("twinkle.wav")
```

---

## Made by TechnoSwas 🎵
