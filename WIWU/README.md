# 🎵 WIWU - Make Music With Code!

WIWU lets you code music using note names like C4, A#3, Gb5 and save them as audio files.

## Setup on Replit
1. Upload WIWU.py to your Replit project
2. In the Replit console, run: `pip install numpy`
3. Import and use WIWU in your code!

## Quick Start

```python
from WIWU import Song

song = Song()
song.add_note("C4")
song.add_note("E4")
song.add_note("G4")
song.save("mysong.wav")
```

## Note Format
Notes are written as the note name + octave number:
- `C4` = Middle C
- `A4` = Concert A (440 Hz)
- `F#3` = F sharp in octave 3
- `Bb5` = B flat in octave 5

Valid notes: C, C#, Db, D, D#, Eb, E, F, F#, Gb, G, G#, Ab, A, A#, Bb, B

## Methods

### Song(tempo=120, volume=0.5)
Create a new song.

### song.add_note(note, duration=1.0)
Add a single note. Duration is in beats.

### song.add_rest(duration=1.0)
Add silence.

### song.add_chord([notes], duration=1.0)
Add multiple notes at once.

### song.save(filename)
Save the song as a .wav file.

### song.preview()
Show song info without saving.

## Example Songs
Check out `example.py` for full working examples including a scale, Twinkle Twinkle, and chords!
