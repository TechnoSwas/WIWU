WIWU Documentation
==================

WIWU lets you code music using note names like C4, A#3, Gb5 and save them as audio files!

Installation
------------

.. code-block:: bash

   pip install WIWU

Quick Start
-----------

.. code-block:: python

   import WIWU

   song = WIWU.Song()
   song.add_note("C4")
   song.add_note("E4")
   song.add_note("G4")
   song.save("mysong.wav")

Methods
-------

**Song(tempo=120, volume=0.5)**
   Create a new song.

**song.add_note(note, duration=1.0)**
   Add a single note. Duration is in beats.

**song.add_rest(duration=1.0)**
   Add silence.

**song.add_chord(notes, duration=1.0)**
   Play multiple notes at the same time.

**song.save(filename)**
   Save your song as a WAV audio file.
