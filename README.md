<a href="https://www.buymeacoffee.com/gumslone" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

# raspi_buzzer_player

Play **121 melodies** on your Raspberry Pi with a cheap passive (or active)
buzzer — game and movie themes, classical pieces, Christmas carols, folk songs
and nursery rhymes. Pure Python 3, no dependencies beyond `RPi.GPIO`.

Repository: https://github.com/gumslone/raspi_buzzer_player

## Features

- **121 built-in songs** across many genres — run `--list` to browse them.
- **Tiny command line** — play everything, a single song, or a custom set,
  selected by number or by title (substring match).
- **Compact song notation** so adding a new tune is a single line of text.
- **No third-party dependencies** beyond `RPi.GPIO` (preinstalled on Raspberry
  Pi OS); square-wave tone generation is done in pure Python.
- **Clean shutdown** — the GPIO pin is always released, even on `Ctrl+C`.

## Hardware

A passive or active buzzer wired to a GPIO pin:

```
Passive buzzer        Pi
   VCC --------------- 3.3V
   GND --------------- GND
   SIG --------------- GPIO27   (BCM numbering)
```

The signal pin is configured in `buzzer_player.py`:

```python
buzzer_pin = 27   # BCM pin number
```

Change that value if your buzzer is on a different pin.

## Requirements

- A Raspberry Pi running Raspberry Pi OS (or any Linux with `RPi.GPIO`).
- Python 3.
- The `RPi.GPIO` library (shipped with Raspberry Pi OS; otherwise
  `pip install RPi.GPIO`).

## Usage

```sh
python3 buzzer_player.py             # play every song in order
python3 buzzer_player.py --list      # list all songs with their numbers
python3 buzzer_player.py 9           # play one song by number
python3 buzzer_player.py mario       # play by title (substring match)
python3 buzzer_player.py 9 star bond # play several songs in sequence
python3 buzzer_player.py --help      # full option list
```

Song selection by title is a case-insensitive substring match, so
`python3 buzzer_player.py zelda` plays *Zelda's Lullaby*. Press `Ctrl+C` at any
time to stop; the buzzer pin is released cleanly on exit.

## How it works

The project is split into two files:

| File | Responsibility |
| --- | --- |
| `songs.py` | The note table and the song library. No GPIO import, so it can be imported and inspected on any machine. |
| `buzzer_player.py` | GPIO setup, tone generation, playback loop and the command-line interface. |

A passive buzzer makes sound when its pin is toggled on and off quickly. To
play a note, `buzz()` toggles `buzzer_pin` high then low for half the note's
period, repeated for the note's duration — generating a square wave at the
target frequency. A frequency of `0` is treated as a rest (silence). Each song
is a `melody` list of frequencies paired with an equal-length `tempo` list of
note durations, plus `pause` (gap between notes) and `pace` (overall speed)
parameters.

The `notes` table maps note names (`C4`, `FS5`, `BB3`, …) to their frequency in
Hz, covering 103 pitches from B0 (31 Hz) to DS8 (4978 Hz).

## Adding songs

New songs use a compact notation: whitespace-separated `NOTE:DURATION` tokens.

- `NOTE` is a key of the `notes` table (e.g. `C5`, `FS4`, `BB3`), or `R` for a
  rest.
- `DURATION` is the tempo divisor: `1` = whole, `2` = half, `4` = quarter,
  `8` = eighth, `16` = sixteenth. It is optional and defaults to `4`.

Add a `(title, notation)` entry to the `SIMPLE_SONGS` list in `songs.py`:

```python
("My Song", "C5 C5 G5 G5 A5 A5 G5:2 F5 F5 E5 E5 D5 D5 C5:2"),
```

It is picked up automatically by the command line — no other changes needed.
Note that the bundled melodies are simplified single-voice arrangements
transcribed by ear and tuned for a buzzer, so they are meant to be
recognisable rather than note-perfect scores.

## Project layout

```
buzzer_player.py   GPIO playback + command-line interface
songs.py           note table and 121-song library
README.md          this file
LICENSE            The Unlicense (public domain)
```

## Credits

Some of the note data for the melodies originated from
[astlessons.com](http://www.astlessons.com/pianoforkids1.html).

## License

Released into the public domain under [The Unlicense](LICENSE).
