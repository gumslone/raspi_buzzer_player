#!/usr/bin/env python
#---------------------------------------------------
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org>
#---------------------------------------------------
# 
#		Passive buzzer 			   Pi 
#			VCC ----------------- 3.3V
#			GND ------------------ GND
#			SIG ---------------- Pin Gpio27
#
#		some notes for melodies were taken from:
#		http://www.astlessons.com/pianoforkids1.html
#		http://www.astlessons.com/pianoforkids2.html
#		where you can get more notes
#
#---------------------------------------------------
import argparse
import sys
import time

import RPi.GPIO as GPIO

from songs import SONGS

buzzer_pin = 27


def buzz(frequency, length):
	"""Drive the buzzer at the given frequency (Hz) for length seconds.

	A frequency of 0 is treated as a rest, so we just sleep.
	"""
	if frequency == 0:
		time.sleep(length)
		return
	# The period (sec/cycle) is the inverse of the frequency (cycle/sec);
	# toggle the pin high then low for half the period each.
	half_period = (1.0 / frequency) / 2
	num_cycles = int(length * frequency)

	for _ in range(num_cycles):
		GPIO.output(buzzer_pin, True)
		time.sleep(half_period)
		GPIO.output(buzzer_pin, False)
		time.sleep(half_period)


def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(buzzer_pin, GPIO.OUT)


def destroy():
	GPIO.cleanup()				# Release resource


def play(melody, tempo, pause, pace=0.800):
	for frequency, beats in zip(melody, tempo):
		note_duration = pace / beats
		buzz(frequency, note_duration)		# Change the frequency along the song note
		time.sleep(note_duration * pause)


def find_song(query):
	"""Resolve a CLI argument to a Song: by 1-based index or case-insensitive
	substring match on the title. Returns None if nothing matches."""
	if query.isdigit():
		index = int(query) - 1
		if 0 <= index < len(SONGS):
			return SONGS[index]
		return None
	query = query.lower()
	for song in SONGS:
		if query in song.title.lower():
			return song
	return None


def list_songs():
	for index, song in enumerate(SONGS, start=1):
		print("%2d. %s" % (index, song.title))


def play_songs(songs):
	setup()
	try:
		for index, song in enumerate(songs):
			print(song.title)
			play(song.melody, song.tempo, song.pause, song.pace)
			if index < len(songs) - 1:
				time.sleep(2)
	finally:
		# Runs on normal completion and on Ctrl+C, releasing the GPIO pin.
		destroy()


def main(argv=None):
	parser = argparse.ArgumentParser(
		description="Play melodies on a Raspberry Pi buzzer.")
	parser.add_argument(
		"songs", nargs="*",
		help="songs to play, by number or title (substring); plays all if omitted")
	parser.add_argument(
		"-l", "--list", action="store_true", help="list available songs and exit")
	args = parser.parse_args(argv)

	if args.list:
		list_songs()
		return 0

	if args.songs:
		selected = []
		for query in args.songs:
			song = find_song(query)
			if song is None:
				parser.error("no song matching %r (use --list to see options)" % query)
			selected.append(song)
	else:
		selected = SONGS

	play_songs(selected)
	return 0


if __name__ == '__main__':
	sys.exit(main())
