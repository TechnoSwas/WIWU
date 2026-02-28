"""
WIWU - A simple music note library
Make music with notes like C5, A4, G3 and save them to audio files!
"""

import numpy as np
import wave
import struct
import os

# Sample rate for audio
SAMPLE_RATE = 44100

# Note frequencies (note name -> base frequency in Hz at octave 4)
BASE_FREQUENCIES = {
    'C': 261.63,
    'C#': 277.18, 'Db': 277.18,
    'D': 293.66,
    'D#': 311.13, 'Eb': 311.13,
    'E': 329.63,
    'F': 349.23,
    'F#': 369.99, 'Gb': 369.99,
    'G': 392.00,
    'G#': 415.30, 'Ab': 415.30,
    'A': 440.00,
    'A#': 466.16, 'Bb': 466.16,
    'B': 493.88,
}


def note_to_frequency(note: str) -> float:
    """Convert a note like C5 or A4 to its frequency in Hz."""
    note = note.strip()
    
    # Split note name and octave
    if len(note) >= 2 and note[-1].isdigit():
        octave = int(note[-1])
        name = note[:-1].upper()
    elif len(note) >= 3 and note[-1].isdigit():
        octave = int(note[-1])
        name = note[:-1].upper()
    else:
        raise ValueError(f"Invalid note format: '{note}'. Use format like C5, A4, F#3")
    
    if name not in BASE_FREQUENCIES:
        raise ValueError(f"Unknown note: '{name}'. Valid notes: C, C#, D, D#, E, F, F#, G, G#, A, A#, B")
    
    base_freq = BASE_FREQUENCIES[name]
    # Adjust for octave (octave 4 is the base)
    frequency = base_freq * (2 ** (octave - 4))
    return frequency


def generate_tone(frequency: float, duration: float, volume: float = 0.5) -> np.ndarray:
    """Generate a sine wave tone for a given frequency and duration."""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    tone = np.sin(2 * np.pi * frequency * t)
    
    # Apply a simple envelope to avoid clicking sounds
    fade_samples = int(SAMPLE_RATE * 0.01)  # 10ms fade
    if len(tone) > fade_samples * 2:
        tone[:fade_samples] *= np.linspace(0, 1, fade_samples)
        tone[-fade_samples:] *= np.linspace(1, 0, fade_samples)
    
    return tone * volume


def generate_silence(duration: float) -> np.ndarray:
    """Generate silence for a given duration."""
    return np.zeros(int(SAMPLE_RATE * duration))


class Song:
    """
    The main class for creating music with WIWU!
    
    Example:
        song = Song()
        song.add_note("C4")
        song.add_note("E4")
        song.add_note("G4")
        song.save("my_song.wav")
    """
    
    def __init__(self, tempo: int = 120, volume: float = 0.5):
        """
        Create a new song.
        
        Args:
            tempo: Beats per minute (default 120)
            volume: Volume from 0.0 to 1.0 (default 0.5)
        """
        self.tempo = tempo
        self.volume = volume
        self.tracks = []  # list of (audio_array) segments
        self._beat_duration = 60.0 / tempo  # duration of one beat in seconds
        print(f"🎵 New WIWU song created! Tempo: {tempo} BPM")
    
    def add_note(self, note: str, duration: float = 1.0):
        """
        Add a musical note to the song.
        
        Args:
            note: Note name like 'C4', 'A#3', 'Gb5'
            duration: Duration in beats (default 1.0 = one beat)
        
        Example:
            song.add_note("C4")        # one beat
            song.add_note("G4", 0.5)   # half beat
            song.add_note("E5", 2.0)   # two beats
        """
        freq = note_to_frequency(note)
        seconds = duration * self._beat_duration
        tone = generate_tone(freq, seconds, self.volume)
        self.tracks.append(tone)
        print(f"  ♪ Added note {note} ({freq:.1f} Hz, {seconds:.2f}s)")
    
    def add_rest(self, duration: float = 1.0):
        """
        Add a rest (silence) to the song.
        
        Args:
            duration: Duration in beats (default 1.0)
        """
        seconds = duration * self._beat_duration
        silence = generate_silence(seconds)
        self.tracks.append(silence)
        print(f"  - Added rest ({seconds:.2f}s)")
    
    def add_chord(self, notes: list, duration: float = 1.0):
        """
        Add multiple notes played at the same time (a chord).
        
        Args:
            notes: List of note names like ['C4', 'E4', 'G4']
            duration: Duration in beats (default 1.0)
        
        Example:
            song.add_chord(['C4', 'E4', 'G4'])  # C major chord
        """
        seconds = duration * self._beat_duration
        combined = np.zeros(int(SAMPLE_RATE * seconds))
        for note in notes:
            freq = note_to_frequency(note)
            tone = generate_tone(freq, seconds, self.volume / len(notes))
            combined += tone
        self.tracks.append(combined)
        print(f"  ♫ Added chord {notes} ({seconds:.2f}s)")
    
    def save(self, filename: str = "song.wav"):
        """
        Save the song to a WAV audio file.
        
        Args:
            filename: Name of the file to save (default 'song.wav')
        
        Example:
            song.save("my_awesome_song.wav")
        """
        if not self.tracks:
            print("⚠️  No notes added yet! Add some notes before saving.")
            return
        
        if not filename.endswith('.wav'):
            filename += '.wav'
        
        # Combine all tracks
        audio = np.concatenate(self.tracks)
        
        # Convert to 16-bit integers
        audio_int = np.int16(audio * 32767)
        
        # Write to WAV file
        with wave.open(filename, 'w') as wav_file:
            wav_file.setnchannels(1)  # Mono
            wav_file.setsampwidth(2)  # 2 bytes = 16 bit
            wav_file.setframerate(SAMPLE_RATE)
            wav_file.writeframes(audio_int.tobytes())
        
        duration = len(audio) / SAMPLE_RATE
        print(f"\n✅ Song saved to '{filename}' ({duration:.2f} seconds)")
    
    def clear(self):
        """Clear all notes from the song."""
        self.tracks = []
        print("🗑️  Song cleared!")
    
    def preview(self):
        """Show a summary of the song."""
        total_seconds = sum(len(t) for t in self.tracks) / SAMPLE_RATE
        print(f"\n🎵 Song Preview:")
        print(f"   Tempo: {self.tempo} BPM")
        print(f"   Total duration: {total_seconds:.2f} seconds")
        print(f"   Number of segments: {len(self.tracks)}")


def play_note(note: str, duration: float = 1.0, tempo: int = 120):
    """
    Quick function to create and save a single note.
    
    Args:
        note: Note name like 'C4'
        duration: Duration in beats
        tempo: Beats per minute
    """
    song = Song(tempo=tempo)
    song.add_note(note, duration)
    filename = f"{note}_{duration}beat.wav"
    song.save(filename)
    return filename


# List of all valid notes for reference
NOTES = list(BASE_FREQUENCIES.keys())

print("🎵 WIWU loaded! Start making music!")
print("   Try: song = Song()")
print("        song.add_note('C4')")
print("        song.save('mysong.wav')")
