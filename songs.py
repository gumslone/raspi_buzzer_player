#---------------------------------------------------
# Song library for buzzer_player.py
#
# NOTES maps note names to their frequency in Hz. Each song is a
# (melody, tempo) pair of equal-length lists: melody holds the note
# frequency (0 = rest), tempo holds the note length as a divisor of the
# pace (a larger number is a shorter note).
#
#		some notes for melodies were taken from:
#		http://www.astlessons.com/pianoforkids1.html
#		http://www.astlessons.com/pianoforkids2.html
#---------------------------------------------------
from collections import namedtuple

notes = {
	'B0' : 31,
	'C1' : 33, 'CS1' : 35,
	'D1' : 37, 'DS1' : 39,
	'EB1' : 39,
	'E1' : 41,
	'F1' : 44, 'FS1' : 46,
	'G1' : 49, 'GS1' : 52,
	'A1' : 55, 'AS1' : 58,
	'BB1' : 58,
	'B1' : 62,
	'C2' : 65, 'CS2' : 69,
	'D2' : 73, 'DS2' : 78,
	'EB2' : 78,
	'E2' : 82,
	'F2' : 87, 'FS2' : 93,
	'G2' : 98, 'GS2' : 104,
	'A2' : 110, 'AS2' : 117,
	'BB2' : 123,
	'B2' : 123,
	'C3' : 131, 'CS3' : 139,
	'D3' : 147, 'DS3' : 156,
	'EB3' : 156,
	'E3' : 165,
	'F3' : 175, 'FS3' : 185,
	'G3' : 196, 'GS3' : 208,
	'A3' : 220, 'AS3' : 233,
	'BB3' : 233,
	'B3' : 247,
	'C4' : 262, 'CS4' : 277,
	'D4' : 294, 'DS4' : 311,
	'EB4' : 311,
	'E4' : 330,
	'F4' : 349, 'FS4' : 370,
	'G4' : 392, 'GS4' : 415,
	'A4' : 440, 'AS4' : 466,
	'BB4' : 466,
	'B4' : 494,
	'C5' : 523, 'CS5' : 554,
	'D5' : 587, 'DS5' : 622,
	'EB5' : 622,
	'E5' : 659,
	'F5' : 698, 'FS5' : 740,
	'G5' : 784, 'GS5' : 831,
	'A5' : 880, 'AS5' : 932,
	'BB5' : 932,
	'B5' : 988,
	'C6' : 1047, 'CS6' : 1109,
	'D6' : 1175, 'DS6' : 1245,
	'EB6' : 1245,
	'E6' : 1319,
	'F6' : 1397, 'FS6' : 1480,
	'G6' : 1568, 'GS6' : 1661,
	'A6' : 1760, 'AS6' : 1865,
	'BB6' : 1865,
	'B6' : 1976,
	'C7' : 2093, 'CS7' : 2217,
	'D7' : 2349, 'DS7' : 2489,
	'EB7' : 2489,
	'E7' : 2637,
	'F7' : 2794, 'FS7' : 2960,
	'G7' : 3136, 'GS7' : 3322,
	'A7' : 3520, 'AS7' : 3729,
	'BB7' : 3729,
	'B7' : 3951,
	'C8' : 4186, 'CS8' : 4435,
	'D8' : 4699, 'DS8' : 4978
}



melody = [
  notes['E7'], notes['E7'], 0, notes['E7'],
  0, notes['C7'], notes['E7'], 0,
  notes['G7'], 0, 0,  0,
  notes['G6'], 0, 0, 0,
 
  notes['C7'], 0, 0, notes['G6'],
  0, 0, notes['E6'], 0,
  0, notes['A6'], 0, notes['B6'],
  0, notes['AS6'], notes['A6'], 0,
 
  notes['G6'], notes['E7'], notes['G7'],
  notes['A7'], 0, notes['F7'], notes['G7'],
  0, notes['E7'], 0, notes['C7'],
  notes['D7'], notes['B6'], 0, 0,
 
  notes['C7'], 0, 0, notes['G6'],
  0, 0, notes['E6'], 0,
  0, notes['A6'], 0, notes['B6'],
  0, notes['AS6'], notes['A6'], 0,
 
  notes['G6'], notes['E7'], notes['G7'],
  notes['A7'], 0, notes['F7'], notes['G7'],
  0, notes['E7'], 0, notes['C7'],
  notes['D7'], notes['B6'], 0, 0
]
tempo = [
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
 
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
 
  9, 9, 9,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
 
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
 
  9, 9, 9,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
]


underworld_melody = [
  notes['C4'], notes['C5'], notes['A3'], notes['A4'],
  notes['AS3'], notes['AS4'], 0,
  0,
  notes['C4'], notes['C5'], notes['A3'], notes['A4'],
  notes['AS3'], notes['AS4'], 0,
  0,
  notes['F3'], notes['F4'], notes['D3'], notes['D4'],
  notes['DS3'], notes['DS4'], 0,
  0,
  notes['F3'], notes['F4'], notes['D3'], notes['D4'],
  notes['DS3'], notes['DS4'], 0,
  0, notes['DS4'], notes['CS4'], notes['D4'],
  notes['CS4'], notes['DS4'],
  notes['DS4'], notes['GS3'],
  notes['G3'], notes['CS4'],
  notes['C4'], notes['FS4'], notes['F4'], notes['E3'], notes['AS4'], notes['A4'],
  notes['GS4'], notes['DS4'], notes['B3'],
  notes['AS3'], notes['A3'], notes['GS3'],
  0, 0, 0
]

underworld_tempo = [
  12, 12, 12, 12,
  12, 12, 6,
  3,
  12, 12, 12, 12,
  12, 12, 6,
  3,
  12, 12, 12, 12,
  12, 12, 6,
  3,
  12, 12, 12, 12,
  12, 12, 6,
  6, 18, 18, 18,
  6, 6,
  6, 6,
  6, 6,
  18, 18, 18, 18, 18, 18,
  10, 10, 10,
  10, 10, 10,
  3, 3, 3
]

adventure_time_melody = [
    notes['D5'], 
    notes['G5'], notes['G5'], notes['G5'], notes['G5'], notes['FS5'],
    notes['FS5'], notes['E5'], notes['D5'], notes['E5'], notes['D5'], notes['D5'],
    notes['C5'], notes['B5'], notes['A5'], notes['G4'],  
    0, notes['C5'], notes['B5'], notes['A5'], notes['G4'], 0,  
    notes['G5'], 0, notes['G5'], notes['G5'], 0, notes['G5'], 
    notes['FS5'], 0, notes['E5'], notes['E5'], notes['D5'], notes['D5'], 
    notes['C5'], notes['C5'], notes['C5'], notes['D5'], 
    notes['D5'], notes['A5'], notes['B5'], notes['A5'], notes['G4'], 
    notes['G5']
  ]
adventure_time_tempo = [
    24,
    24, 12, 12, 12, 24,
    12, 24, 24, 24, 12, 24,
    12, 12, 12, 12,
    24, 12, 24, 24, 12, 24,  
    24, 24, 24, 12, 24, 12, 
    24, 24, 24, 12, 12, 24, 
    8, 24, 24, 8, 
    8, 24, 12, 24, 24, 
    12 
  ]


star_wars_melody = [ 
					notes['G4'], notes['G4'], notes['G4'], 
					notes['EB4'], 0, notes['BB4'], notes['G4'], 
					notes['EB4'], 0, notes['BB4'], notes['G4'], 0,
					
					notes['D4'], notes['D4'], notes['D4'], 
					notes['EB4'], 0, notes['BB3'], notes['FS3'],
					notes['EB3'], 0, notes['BB3'], notes['G3'], 0,
					
					notes['G4'], 0, notes['G3'], notes['G3'], 0,
					notes['G4'], 0, notes['FS4'], notes['F4'], 
					notes['E4'], notes['EB4'], notes['E4'], 0,
					notes['GS3'], notes['CS3'], 0, 
					
					notes['C3'], notes['B3'], notes['BB3'], notes['A3'], notes['BB3'], 0,
					notes['EB3'], notes['FS3'], notes['EB3'], notes['FS3'], 
					notes['BB3'], 0, notes['G3'], notes['BB3'], notes['D4'], 0,
					
					
					notes['G4'], 0, notes['G3'], notes['G3'], 0,
					notes['G4'], 0, notes['FS4'], notes['F4'], 
					notes['E4'], notes['EB4'], notes['E4'], 0,
					notes['GS3'], notes['CS3'], 0, 
					
					notes['C3'], notes['B3'], notes['BB3'], notes['A3'], notes['BB3'], 0,
					
					notes['EB3'], notes['FS3'], notes['EB3'],  
					notes['BB3'], notes['G3'], notes['EB3'], 0, notes['BB3'], notes['G3'],
					]


star_wars_tempo = [
					2, 2, 2, 
					4, 8, 6, 2, 
					4, 8, 6, 2, 8,
					
					2, 2, 2,
					4, 8, 6, 2,
					4, 8, 6, 2, 8,
					
					2, 16, 4, 4, 8,
					2, 8, 4, 6,
					6, 4, 4, 8,
					4, 2, 8, 
					4, 4, 6, 4, 2, 8,
					4, 2, 4, 4, 
					2, 8, 4, 6, 2, 8,
					
					2, 16, 4, 4, 8,
					2, 8, 4, 6,
					6, 4, 4, 8,
					4, 2, 8, 
					4, 4, 6, 4, 2, 8,
					4, 2, 2, 
					4, 2, 4, 8, 4, 2,
					]

popcorn_melody = [
	
	notes['A4'], notes['G4'], notes['A4'], notes['E4'], notes['C4'], notes['E4'], notes['A3'], 
	notes['A4'], notes['G4'], notes['A4'], notes['E4'], notes['C4'], notes['E4'], notes['A3'], 
	
	notes['A4'], notes['B4'], notes['C5'], notes['B4'], notes['C5'], notes['A4'], notes['B4'], notes['A4'], notes['B4'], notes['G4'], 
	notes['A4'], notes['G4'],notes['A4'], notes['F4'], notes['A4'],
	
	
	notes['A4'], notes['G4'], notes['A4'], notes['E4'], notes['C4'], notes['E4'], notes['A3'], 
	notes['A4'], notes['G4'], notes['A4'], notes['E4'], notes['C4'], notes['E4'], notes['A3'], 
	
	notes['A4'], notes['B4'], notes['C5'], notes['B4'], notes['C5'], notes['A4'], notes['B4'], notes['A4'], notes['B4'], notes['G4'], 
	notes['A4'], notes['G4'],notes['A4'], notes['B4'], notes['C5'],
	
	notes['E5'], notes['D5'], notes['E5'], notes['C5'], notes['G4'], notes['C5'], notes['E4'], 
	notes['E5'], notes['D5'], notes['E5'], notes['C5'], notes['G4'], notes['C5'], notes['E4'], 
	
	notes['E5'], notes['FS5'], notes['G5'], notes['FS5'], notes['G5'], notes['E5'], notes['FS5'], notes['E5'], notes['FS5'], notes['D5'], 
	notes['E5'], notes['D5'],notes['E5'], notes['C5'], notes['E5'],
	
	###
	
	notes['E5'], notes['D5'], notes['E5'], notes['C5'], notes['G4'], notes['C5'], notes['E4'], 
	notes['E5'], notes['D5'], notes['E5'], notes['C5'], notes['G4'], notes['C5'], notes['E4'], 
	
	notes['E5'], notes['FS5'], notes['G5'], notes['FS5'], notes['G5'], notes['E5'], notes['FS5'], notes['E5'], notes['FS5'], notes['D5'], 
	notes['E5'], notes['D5'],notes['B4'], notes['D5'], notes['E5'],
]
popcorn_tempo = [
	8,8,8,8,8,8,4,
	8,8,8,8,8,8,4,
	
	8,8,8,8,8,8,8,8,8,8,
	8,8,8,8,4,
	
	8,8,8,8,8,8,4,
	8,8,8,8,8,8,4,
	
	8,8,8,8,8,8,8,8,8,8,
	8,8,8,8,4,
	
	8,8,8,8,8,8,4,
	8,8,8,8,8,8,4,
	
	8,8,8,8,8,8,8,8,8,8,
	8,8,8,8,4,
	
	8,8,8,8,8,8,4,
	8,8,8,8,8,8,4,
	
	8,8,8,8,8,8,8,8,8,8,
	8,8,8,8,4,
]

twinkle_twinkle_melody = [
	notes['C4'], notes['C4'], notes['G4'], notes['G4'], notes['A4'], notes['A4'], notes['G4'],
	notes['F4'], notes['F4'], notes['E4'], notes['E4'], notes['D4'], notes['D4'], notes['C4'],
	
	notes['G4'], notes['G4'], notes['F4'], notes['F4'], notes['E4'], notes['E4'], notes['D4'],
	notes['G4'], notes['G4'], notes['F4'], notes['F4'], notes['E4'], notes['E4'], notes['D4'],
	
	notes['C4'], notes['C4'], notes['G4'], notes['G4'], notes['A4'], notes['A4'], notes['G4'],
	notes['F4'], notes['F4'], notes['E4'], notes['E4'], notes['D4'], notes['D4'], notes['C4'],
]

twinkle_twinkle_tempo = [
	4,4,4,4,4,4,2,
	4,4,4,4,4,4,2,
	
	4,4,4,4,4,4,2,
	4,4,4,4,4,4,2,
	
	4,4,4,4,4,4,2,
	4,4,4,4,4,4,2,
]

crazy_frog_melody = [
	notes['A4'], notes['C5'], notes['A4'], notes['A4'], notes['D5'], notes['A4'], notes['G4'], 
	notes['A4'], notes['E5'], notes['A4'], notes['A4'], notes['F5'], notes['E5'], notes['C5'],
	notes['A4'], notes['E5'], notes['A5'], notes['A4'], notes['G4'], notes['G4'], notes['E4'], notes['B4'], 
	notes['A4'],0,
	
	notes['A4'], notes['C5'], notes['A4'], notes['A4'], notes['D5'], notes['A4'], notes['G4'], 
	notes['A4'], notes['E5'], notes['A4'], notes['A4'], notes['F5'], notes['E5'], notes['C5'],
	notes['A4'], notes['E5'], notes['A5'], notes['A4'], notes['G4'], notes['G4'], notes['E4'], notes['B4'], 
	notes['A4'],0,
	
	
	notes['A3'], notes['G3'], notes['E3'], notes['D3'],
	
	notes['A4'], notes['C5'], notes['A4'], notes['A4'], notes['D5'], notes['A4'], notes['G4'], 
	notes['A4'], notes['E5'], notes['A4'], notes['A4'], notes['F5'], notes['E5'], notes['C5'],
	notes['A4'], notes['E5'], notes['A5'], notes['A4'], notes['G4'], notes['G4'], notes['E4'], notes['B4'], 
	notes['A4'],
]

crazy_frog_tempo = [
	2,4,4,8,4,4,4,
	2,4,4,8,4,4,4,
	4,4,4,8,4,8,4,4,
	1,4,
	
	2,4,4,8,4,4,4,
	2,4,4,8,4,4,4,
	4,4,4,8,4,8,4,4,
	1,4,
	
	8,4,4,4,
	
	2,4,4,8,4,4,4,
	2,4,4,8,4,4,4,
	4,4,4,8,4,8,4,4,
	1,
]

deck_the_halls_melody = [
	notes['G5'], notes['F5'], notes['E5'], notes['D5'],
	notes['C5'], notes['D5'], notes['E5'], notes['C5'],
	notes['D5'], notes['E5'], notes['F5'], notes['D5'], notes['E5'], notes['D5'],
	notes['C5'], notes['B4'], notes['C5'], 0,
	
	notes['G5'], notes['F5'], notes['E5'], notes['D5'],
	notes['C5'], notes['D5'], notes['E5'], notes['C5'],
	notes['D5'], notes['E5'], notes['F5'], notes['D5'], notes['E5'], notes['D5'],
	notes['C5'], notes['B4'], notes['C5'], 0,
	
	notes['D5'], notes['E5'], notes['F5'], notes['D5'],
	notes['E5'], notes['F5'], notes['G5'], notes['D5'],
	notes['E5'], notes['F5'], notes['G5'], notes['A5'], notes['B5'], notes['C6'],
	notes['B5'], notes['A5'], notes['G5'], 0,
	
	notes['G5'], notes['F5'], notes['E5'], notes['D5'],
	notes['C5'], notes['D5'], notes['E5'], notes['C5'],
	notes['D5'], notes['E5'], notes['F5'], notes['D5'], notes['E5'], notes['D5'],
	notes['C5'], notes['B4'], notes['C5'], 0,
]

deck_the_halls_tempo = [
	2, 4, 2, 2,
	2, 2, 2, 2,
	4, 4, 4, 4, 2, 4,
	2, 2, 2, 2,
	
	2, 4, 2, 2,
	2, 2, 2, 2,
	4, 4, 4, 4, 2, 4,
	2, 2, 2, 2,
	
	2,4,2,2,
	2,4,2,2,
	4,4,2,4,4,2,
	2,2,2,2,
	
	2, 4, 2, 2,
	2, 2, 2, 2,
	4, 4, 4, 4, 2, 4,
	2, 2, 2, 2,
]

manaderna_melody = [
	notes['E4'],notes['E4'],notes['F4'],notes['G4'],
	notes['G4'],notes['F4'],notes['E4'],notes['D4'],
	notes['C4'],notes['C4'],notes['D4'],notes['E4'],
	notes['E4'],0,notes['D4'],notes['D4'],0,
	
	notes['E4'],notes['E4'],notes['F4'],notes['G4'],
	notes['G4'],notes['F4'],notes['E4'],notes['D4'],
	notes['C4'],notes['C4'],notes['D4'],notes['E4'],
	notes['D4'],0,notes['C4'],notes['C4'],0,
	
	notes['D4'],notes['D4'],notes['E4'],notes['C4'],
	notes['D4'],notes['E4'],notes['F4'],notes['E4'],notes['C4'],
	notes['D4'],notes['E4'],notes['F4'],notes['E4'],notes['D4'],
	notes['C4'],notes['D4'],notes['G3'],0,
	
	notes['E4'],notes['E4'],notes['F4'],notes['G4'],
	notes['G4'],notes['F4'],notes['E4'],notes['D4'],
	notes['C4'],notes['C4'],notes['D4'],notes['E4'],
	notes['D4'],0,notes['C4'],notes['C4'],
]

manaderna_tempo = [
	2,2,2,2,
	2,2,2,2,
	2,2,2,2,
	2,4,4,2,4,
	
	2,2,2,2,
	2,2,2,2,
	2,2,2,2,
	2,4,4,2,4,
	
	2,2,2,2,
	2,4,4,2,2,
	2,4,4,2,2,
	2,2,1,4,
	
	2,2,2,2,
	2,2,2,2,
	2,2,2,2,
	2,4,4,2,
]

bonnagard_melody = [
	notes['C5'],notes['C5'],notes['C5'],notes['G4'],
	notes['A4'],notes['A4'],notes['G4'],
	notes['E5'],notes['E5'],notes['D5'],notes['D5'],
	notes['C5'],0,notes['G4'],
	
	notes['C5'],notes['C5'],notes['C5'],notes['G4'],
	notes['A4'],notes['A4'],notes['G4'],
	notes['E5'],notes['E5'],notes['D5'],notes['D5'],
	notes['C5'],0,notes['G4'],notes['G4'],
	
	notes['C5'],notes['C5'],notes['C5'],notes['G4'],notes['G4'],
	notes['C5'],notes['C5'],notes['G4'],
	notes['C5'],notes['C5'],notes['C5'],notes['C5'],notes['C5'],notes['C5'],
	notes['C5'],notes['C5'],notes['C5'],notes['C5'],notes['C5'],notes['C5'],0,
	
	notes['C5'],notes['C5'],notes['C5'],notes['G4'],
	notes['A4'],notes['A4'],notes['G4'],
	notes['E5'],notes['E5'],notes['D5'],notes['D5'],
	notes['C5'],0,
]

bonnagard_tempo = [
	2,2,2,2,
	2,2,1,
	2,2,2,2,
	1,2,2,
	
	2,2,2,2,
	2,2,1,
	2,2,2,2,
	1,2,4,4,
	
	2,2,2,4,4,
	2,2,1,
	4,4,2,4,4,2,
	4,4,4,4,2,2,4,
	
	2,2,2,2,
	2,2,1,
	2,2,2,2,
	1,1,
]

final_countdown_melody = [
	notes['A3'],notes['E5'],notes['D5'],notes['E5'],notes['A4'],
	notes['F3'],notes['F5'],notes['E5'],notes['F5'],notes['E5'],notes['D5'],
	notes['D3'],notes['F5'],notes['E5'],notes['F5'],notes['A4'],
	notes['G3'],0,notes['D5'],notes['C5'],notes['D5'],notes['C5'],notes['B4'],notes['D5'],
	notes['C5'],notes['A3'],notes['E5'],notes['D5'],notes['E5'],notes['A4'],
	notes['F3'],notes['F5'],notes['E5'],notes['F5'],notes['E5'],notes['D5'],
	notes['D3'],notes['F5'],notes['E5'],notes['F5'],notes['A4'],
	notes['G3'],0,notes['D5'],notes['C5'],notes['D5'],notes['C5'],notes['B4'],notes['D5'],
	notes['C5'],notes['B4'],notes['C5'],notes['D5'],notes['C5'],notes['D5'],
	notes['E5'],notes['D5'],notes['C5'],notes['B4'],notes['A4'],notes['F5'],
	notes['E5'],notes['E5'],notes['F5'],notes['E5'],notes['D5'],
	notes['E5'],
]

final_countdown_tempo = [
	1,16,16,4,4,
	1,16,16,8,8,4,
	1,16,16,4,4,
	2,4,16,16,8,8,8,8,
	4,4,16,16,4,4,
	1,16,16,8,8,4,
	1,16,16,4,4,
	2,4,16,16,8,8,8,8,
	4,16,16,4,16,16,
	8,8,8,8,4,4,
	2,8,4,16,16,
	1,
]


jingle_bells_melody = [
	notes['E5'], notes['E5'], notes['E5'],
	notes['E5'], notes['E5'], notes['E5'],
	notes['E5'], notes['G5'], notes['C5'], notes['D5'], notes['E5'],
	notes['F5'], notes['F5'], notes['F5'], notes['F5'],
	notes['F5'], notes['E5'], notes['E5'], notes['E5'], notes['E5'],
	notes['G5'], notes['G5'], notes['F5'], notes['D5'], notes['C5'],
]

jingle_bells_tempo = [
	4, 4, 2,
	4, 4, 2,
	4, 4, 4, 4, 1,
	4, 4, 4, 4,
	4, 4, 4, 8, 8,
	4, 4, 4, 4, 1,
]

ode_to_joy_melody = [
	notes['E4'], notes['E4'], notes['F4'], notes['G4'],
	notes['G4'], notes['F4'], notes['E4'], notes['D4'],
	notes['C4'], notes['C4'], notes['D4'], notes['E4'],
	notes['E4'], notes['D4'], notes['D4'],
	notes['E4'], notes['E4'], notes['F4'], notes['G4'],
	notes['G4'], notes['F4'], notes['E4'], notes['D4'],
	notes['C4'], notes['C4'], notes['D4'], notes['E4'],
	notes['D4'], notes['C4'], notes['C4'],
]

ode_to_joy_tempo = [
	4, 4, 4, 4,
	4, 4, 4, 4,
	4, 4, 4, 4,
	4, 4, 2,
	4, 4, 4, 4,
	4, 4, 4, 4,
	4, 4, 4, 4,
	4, 4, 2,
]

happy_birthday_melody = [
	notes['C4'], notes['C4'], notes['D4'], notes['C4'], notes['F4'], notes['E4'],
	notes['C4'], notes['C4'], notes['D4'], notes['C4'], notes['G4'], notes['F4'],
	notes['C4'], notes['C4'], notes['C5'], notes['A4'], notes['F4'], notes['E4'], notes['D4'],
	notes['AS4'], notes['AS4'], notes['A4'], notes['F4'], notes['G4'], notes['F4'],
]

happy_birthday_tempo = [
	8, 8, 4, 4, 4, 2,
	8, 8, 4, 4, 4, 2,
	8, 8, 4, 4, 4, 4, 2,
	8, 8, 4, 4, 4, 2,
]

imperial_march_melody = [
	notes['A4'], notes['A4'], notes['A4'], notes['F4'], notes['C5'],
	notes['A4'], notes['F4'], notes['C5'], notes['A4'],
	notes['E5'], notes['E5'], notes['E5'], notes['F5'], notes['C5'],
	notes['GS4'], notes['F4'], notes['C5'], notes['A4'],
]

imperial_march_tempo = [
	4, 4, 4, 6, 16,
	6, 16, 4, 2,
	4, 4, 4, 6, 16,
	6, 16, 4, 2,
]

tetris_melody = [
	notes['E5'], notes['B4'], notes['C5'], notes['D5'], notes['C5'], notes['B4'],
	notes['A4'], notes['A4'], notes['C5'], notes['E5'], notes['D5'], notes['C5'],
	notes['B4'], notes['B4'], notes['C5'], notes['D5'],
	notes['E5'], notes['C5'], notes['A4'], notes['A4'],
]

tetris_tempo = [
	4, 8, 8, 4, 8, 8,
	4, 8, 8, 4, 8, 8,
	4, 8, 8, 4,
	4, 4, 4, 4,
]


fur_elise_melody = [
	notes['E5'], notes['DS5'], notes['E5'], notes['DS5'], notes['E5'], notes['B4'], notes['D5'], notes['C5'], notes['A4'],
	notes['C4'], notes['E4'], notes['A4'], notes['B4'],
	notes['E4'], notes['GS4'], notes['B4'], notes['C5'],
	notes['E4'], notes['E5'], notes['DS5'], notes['E5'], notes['DS5'], notes['E5'], notes['B4'], notes['D5'], notes['C5'], notes['A4'],
	notes['C4'], notes['E4'], notes['A4'], notes['B4'],
	notes['E4'], notes['C5'], notes['B4'], notes['A4'],
]

fur_elise_tempo = [
	8, 8, 8, 8, 8, 8, 8, 8, 8,
	8, 8, 8, 8,
	8, 8, 8, 8,
	8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
	8, 8, 8, 8,
	8, 8, 8, 4,
]

merry_christmas_melody = [
	notes['D4'],
	notes['G4'], notes['G4'], notes['A4'], notes['G4'], notes['FS4'], notes['E4'],
	notes['E4'], notes['E4'], notes['A4'], notes['A4'], notes['B4'], notes['A4'], notes['G4'],
	notes['FS4'], notes['D4'], notes['D4'], notes['B4'], notes['B4'], notes['C5'], notes['B4'], notes['A4'],
	notes['G4'], notes['E4'], notes['D4'], notes['D4'], notes['E4'], notes['A4'], notes['FS4'],
	notes['G4'],
]

merry_christmas_tempo = [
	4,
	4, 8, 8, 8, 8, 4,
	4, 4, 4, 8, 8, 8, 8,
	4, 4, 8, 8, 8, 8, 8, 8,
	4, 4, 4, 8, 8, 4, 4,
	2,
]

nokia_tune_melody = [
	notes['E5'], notes['D5'], notes['FS4'], notes['GS4'],
	notes['CS5'], notes['B4'], notes['D4'], notes['E4'],
	notes['B4'], notes['A4'], notes['CS4'], notes['E4'],
	notes['A4'],
]

nokia_tune_tempo = [
	8, 8, 4, 4,
	8, 8, 4, 4,
	8, 8, 4, 4,
	2,
]

pink_panther_melody = [
	0, notes['DS4'], notes['E4'],
	0, notes['FS4'], notes['G4'],
	0, notes['DS4'], notes['E4'], notes['FS4'], notes['G4'], notes['C5'], notes['B4'], notes['E4'], notes['G4'], notes['B4'],
	notes['AS4'],
]

pink_panther_tempo = [
	8, 8, 4,
	8, 8, 4,
	8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
	2,
]

zelda_lullaby_melody = [
	notes['B4'], notes['D5'], notes['A4'],
	notes['B4'], notes['D5'], notes['A4'],
	notes['B4'], notes['D5'], notes['G5'], notes['FS5'], notes['E5'], notes['D5'],
	notes['E5'],
]

zelda_lullaby_tempo = [
	2, 4, 4,
	2, 4, 4,
	4, 4, 4, 8, 8, 4,
	1,
]


Song = namedtuple('Song', ['title', 'melody', 'tempo', 'pause', 'pace'])

SONGS = [
	Song("The Final Countdown", final_countdown_melody, final_countdown_tempo, 0.30, 1.2000),
	Song("Per Olssons Bonnagard (Old MacDonald Had A Farm) Melody", bonnagard_melody, bonnagard_tempo, 0.30, 0.800),
	Song("Manaderna (Symphony No. 9) Melody", manaderna_melody, manaderna_tempo, 0.30, 0.800),
	Song("Deck The Halls Melody", deck_the_halls_melody, deck_the_halls_tempo, 0.30, 0.800),
	Song("Crazy Frog (Axel F) Theme", crazy_frog_melody, crazy_frog_tempo, 0.30, 0.900),
	Song("Twinkle, Twinkle, Little Star Melody", twinkle_twinkle_melody, twinkle_twinkle_tempo, 0.50, 1.000),
	Song("Popcorn Melody", popcorn_melody, popcorn_tempo, 0.50, 1.000),
	Song("Star Wars Theme", star_wars_melody, star_wars_tempo, 0.50, 1.000),
	Song("Super Mario Theme", melody, tempo, 1.3, 0.800),
	Song("Super Mario Underworld Theme", underworld_melody, underworld_tempo, 1.3, 0.800),
	Song("Adventure Time Theme", adventure_time_melody, adventure_time_tempo, 1.3, 1.500),
	Song("Jingle Bells", jingle_bells_melody, jingle_bells_tempo, 0.30, 0.900),
	Song("Ode To Joy (Beethoven Symphony No. 9)", ode_to_joy_melody, ode_to_joy_tempo, 0.30, 0.800),
	Song("Happy Birthday", happy_birthday_melody, happy_birthday_tempo, 0.30, 0.900),
	Song("Imperial March (Darth Vader)", imperial_march_melody, imperial_march_tempo, 0.30, 1.000),
	Song("Tetris (Korobeiniki)", tetris_melody, tetris_tempo, 0.30, 0.900),
	Song("Fur Elise (Beethoven)", fur_elise_melody, fur_elise_tempo, 0.30, 0.700),
	Song("We Wish You A Merry Christmas", merry_christmas_melody, merry_christmas_tempo, 0.30, 0.900),
	Song("Nokia Tune (Gran Vals)", nokia_tune_melody, nokia_tune_tempo, 0.30, 0.900),
	Song("Pink Panther Theme", pink_panther_melody, pink_panther_tempo, 0.30, 0.900),
	Song("Zelda's Lullaby", zelda_lullaby_melody, zelda_lullaby_tempo, 0.30, 0.800),
]


# ---------------------------------------------------------------------------
# Compact notation
#
# The songs above predate this and spell every note out as notes['X'] arrays.
# That is verbose, so additional songs are written in a compact string format
# instead: whitespace-separated "NOTE:DURATION" tokens, where NOTE is a key of
# the notes table (or "R" for a rest) and DURATION is the tempo divisor
# (4 = quarter, 8 = eighth, 2 = half, 1 = whole, 16 = sixteenth). The duration
# is optional and defaults to 4. parse_notation() turns such a string into the
# (melody, tempo) pair the player expects.
# ---------------------------------------------------------------------------

def parse_notation(notation, default_duration=4):
	melody = []
	tempo = []
	for token in notation.split():
		name, _, duration = token.partition(':')
		melody.append(0 if name == 'R' else notes[name])
		tempo.append(int(duration) if duration else default_duration)
	return melody, tempo


# (title, notation) — short, recognisable hooks of public-domain melodies.
# These are simplified single-voice arrangements transcribed by ear, so they
# are meant to be recognisable on a buzzer rather than note-perfect scores.
SIMPLE_SONGS = [
	("Mary Had a Little Lamb", "E5 D5 C5 D5 E5 E5 E5:2 D5 D5 D5:2 E5 G5 G5:2 E5 D5 C5 D5 E5 E5 E5 E5 D5 D5 E5 D5 C5:1"),
	("Row Row Row Your Boat", "C5 C5 C5 D5 E5 E5 D5 E5 F5 G5:2 C6:8 C6:8 C6:8 G5:8 G5:8 G5:8 E5:8 E5:8 E5:8 C5:8 C5:8 C5:8 G5 F5 E5 D5 C5:2"),
	("London Bridge Is Falling Down", "G5 A5:8 G5:8 F5 E5 F5 G5:2 D5 E5 F5:2 E5 F5 G5:2 G5 A5:8 G5:8 F5 E5 F5 G5:2 D5:2 G5 E5 C5:2"),
	("Itsy Bitsy Spider", "G4 C5 C5 C5 D5 E5 E5 D5 C5 D5 E5:2 C5 E5 E5 F5 G5:2 F5 E5 F5 G5 E5 C5 C5 D5 E5 E5 D5 C5 D5 E5:2 C5"),
	("Hot Cross Buns", "E5 D5 C5:2 E5 D5 C5:2 C5 C5 C5 C5 D5 D5 D5 D5 E5 D5 C5:2"),
	("Frere Jacques", "C5 D5 E5 C5 C5 D5 E5 C5 E5 F5 G5:2 E5 F5 G5:2 G5:8 A5:8 G5:8 F5:8 E5 C5 G5:8 A5:8 G5:8 F5:8 E5 C5 C5 G4 C5:2 C5 G4 C5:2"),
	("Pop Goes the Weasel", "C5 C5 D5 D5 E5 G5 E5 C5 C5 C5 D5 D5 E5:2 C5 C5 C5 D5 D5 E5 G5 E5 C5 A5 G5 E5 C5:2"),
	("This Old Man", "G5 E5:2 G5 G5 E5:2 G5 A5 G5 F5 E5 D5 E5 F5 G5:2 C5 C5 C5 D5 E5 F5 G5:2 G5 D5 D5 E5 C5:2"),
	("If You're Happy and You Know It", "C5 F5 F5 F5 F5 F5 A5 G5 F5 G5 A5:2 C5 G5 G5 G5 G5 G5 B5 A5 G5 A5 B5:2"),
	("Yankee Doodle", "C5 C5 D5 E5 C5 E5 D5 G4 C5 C5 D5 E5 C5:2 B4:2 C5 C5 D5 E5 F5 E5 D5 C5 B4 G4 A4 B4 C5:2 C5:2"),
	("Oh My Darling Clementine", "C5 C5 C5 F5 A5 A5 A5 F5 F5 A5 C6 C6 B5 A5 G5:2 G5 A5 B5 B5 A5 G5 A5 F5:2"),
	("She'll Be Coming Round the Mountain", "C5 E5 E5 E5 E5 E5 G5 E5 D5 C5 D5:2 D5 E5 D5 C5:2"),
	("Three Blind Mice", "E5 D5 C5:2 E5 D5 C5:2 G5 F5 F5 E5:2 G5 F5 F5 E5:2"),
	("Hickory Dickory Dock", "G4 C5 D5 E5 G5 E5 C5 D5 E5 D5 E5 F5 G5:2"),
	("The Muffin Man", "D5 G5 G5 G5 A5 B5:2 G5 B5 A5 G5 A5:2 D5 G5 G5 G5 A5 B5:2 G5 D5 A5 A5 B5 G5:2"),
	("When Johnny Comes Marching Home", "E4 G4 G4 A4 G4 F4 E4 D4 C4 C4 D4 E4 G4 E4:2"),
	("Skip to My Lou", "C5 C5 C5 A4 G5 G5 G5 E5 C5 C5 C5 A4 G5 E5 C5:2"),
	("Lavender's Blue", "C5 C5 F5 F5 A5 A5 F5:2 G5 G5 A5 G5 F5 G5 A5:2"),
	("Rock-a-bye Baby", "G5 E5 G5 E5 C5 G5 E5:2 F5 D5 D5 G5 D5 C5:2"),
	("Brahms' Lullaby", "E5 E5 G5:2 E5 E5 G5:2 E5 G5 C6 B5 A5 A5 G5:2 D5 E5 F5 D5 E5:8 F5:8 G5:2 D5 G5 F5 D5 C5:2"),
	("Oh Susanna", "C5 D5 E5 G5 G5 A5 G5 E5 C5 D5 E5 E5 D5 C5 D5:2"),
	("Camptown Races", "G5 G5 E5 G5 A5 G5 E5:2 E5 D5 E5 D5 C5:2"),
	("When the Saints Go Marching In", "C5 E5 F5 G5:2 C5 E5 F5 G5:2 C5 E5 F5 G5 E5 C5 E5 D5:2"),
	("My Bonnie Lies Over the Ocean", "G4 E5 D5 C5 B4 A4 G4:2 A4 B4 C5 A4 D5:2"),
	("Home on the Range", "C5 C5 F5 F5 F5 G5 A5 F5 G5 A5 G5 F5 C5:2"),
	("Auld Lang Syne", "C5 F5 F5 F5 A5 G5 F5 G5 A5 G5 F5 F5 A5 C6 D6:2"),
	("Greensleeves", "A4 C5 D5 E5 F5 E5 D5 B4 G4 A4 B4 C5 A4 A4 GS4 A4 B4 GS4 E4:2"),
	("Scarborough Fair", "A4 A4 E5 E5 E5 B4 C5 B4 A4 G4 E4 E4 A4:2"),
	("Drunken Sailor", "E5 E5 E5 E5 D5 D5 D5 D5 E5 D5 C5 B4 A4:2"),
	("Michael Row the Boat Ashore", "C5 E5 G5 C6 B5 G5 A5 G5 E5 G5 E5 C5:2"),
	("Swing Low Sweet Chariot", "G5 E5 C5 E5 D5:2 E5 C5 E5 D5 C5:2"),
	("He's Got the Whole World", "G5 C6 C6 C6 B5 C6 A5:2 A5 G5 A5 G5 E5:2"),
	("Kumbaya", "C5 F5 A5 A5 G5 F5 A5 G5 F5:2"),
	("Amazing Grace", "G4 C5 E5 C5 E5 D5 C5 A4 G4:2 G4 C5 E5 C5 E5 D5 G5:2"),
	("Down in the Valley", "G4 C5 C5 D5 E5 D5 C5:2 E5 G5 G5 F5 E5 D5 C5:2"),
	("Red River Valley", "C5 E5 G5 G5 G5 A5 G5 E5 D5 C5:2"),
	("Polly Wolly Doodle", "G5 G5 G5 E5 G5 C6 G5 E5 C5 D5 E5 D5 C5:2"),
	("Turkey in the Straw", "C5 B4 A4 G4 F4 G4 A4 B4 C5 C5 C5 A4 G4 C5:2"),
	("The Yellow Rose of Texas", "C5 C5 C5 G5 E5 C5 E5 D5 C5 D5 E5 D5 C5:2"),
	("My Country Tis of Thee", "C5 C5 D5 B4 C5 D5 E5 E5 F5 E5 D5 C5 D5 C5 B4 C5:2"),
	("America the Beautiful", "G5 G5 E5 E5 G5 G5 D5:2 D5 E5 F5 FS5 G5 G5 D5:2"),
	("Battle Hymn of the Republic", "G5 G5 G5 G5 G5 C5 E5 E5 E5 D5 C5 D5 E5 E5 D5 C5:2"),
	("The Star-Spangled Banner", "G5 E5 C5 E5 G5 C6:2 E6 D6 C6 E5 FS5 G5:2"),
	("Grand Old Flag", "G5 E5 E5 F5 G5 C6 B5 C6 D6 G5 E5:2"),
	("Dixie", "A4 FS4 FS4 D4 E4 FS4 G4 A4 A4 A4 D5:2"),
	("Silent Night", "G5 A5:8 G5:8 E5:2 G5 A5:8 G5:8 E5:2 D6 D6 B5:2 C6 C6 G5:2"),
	("Joy to the World", "C6 B5 A5 G5:2 F5 E5 D5 C5:2 G5 A5 A5 B5 B5 C6:2"),
	("Hark the Herald Angels Sing", "C5 C5 G5 G5 G5 F5 E5:2 C5 C5 G5 G5 F5 F5 E5:2"),
	("O Come All Ye Faithful", "G5 D5 G5 A5 D5 B5 A5 B5 C6 B5 A5 G5:2"),
	("The First Noel", "E5 D5 C5 D5 E5 F5 G5:2 A5 B5 C6 B5 A5 G5:2"),
	("Away in a Manger", "G5 C6 C6 B5 C6 D6 E6 C6:2 A5 D6 D6 C6 B5 A5 G5:2"),
	("O Christmas Tree", "C5 F5 F5 F5 G5 A5 A5 A5 A5 BB5 C6 F5 F5 A5 G5 F5:2"),
	("Good King Wenceslas", "C5 C5 C5 D5 C5 C5 G5:2 A5 G5 F5 E5 D5 C5:2"),
	("We Three Kings", "A4 G4 FS4 E4 D4:2 A4 G4 FS4 E4 D4:2 G4 G4 A4 B4 A4 G4:2"),
	("Jolly Old Saint Nicholas", "E5 E5 E5 C5 D5 D5 D5 G4 E5 E5 D5 C5 D5:2"),
	("Up on the Housetop", "C5 C5 C5 C5 G4 A4 G4 F4 C5 C5 G4 G4 E4 C4:2"),
	("O Little Town of Bethlehem", "F5 F5 G5 F5 A5 BB5 A5 G5 F5 A5 D6 C6 F5:2"),
	("Angels We Have Heard on High", "G5 A5 G5 F5 E5 F5 G5 A5 G5 F5 E5 F5 G5 C6 A5 G5:2"),
	("Rudolph the Red-Nosed Reindeer", "G5 A5 G5 E5 C5 A5 G5:2 A5 B5 A5 G5 A5 G5 E5:2"),
	("Santa Claus Is Coming to Town", "G5 C6 C6 D6 D6 E6 C6 C6 A5 G5:2"),
	("Frosty the Snowman", "C5 D5 E5 F5 G5:2 G5 F5 E5 F5 G5:2"),
	("Carol of the Bells", "A4 G4 A4 E4 A4 G4 A4 E4 A4 G4 A4 E4:2"),
	("It Came Upon a Midnight Clear", "G4 C5 C5 B4 C5 E5 D5 C5 B4 A4 G4 C5:2"),
	("God Rest Ye Merry Gentlemen", "E5 E5 B4 B4 A4 A4 GS4 B4 E5 E5 B4 B4 A4 GS4 E4:2"),
	("The Twelve Days of Christmas", "C5 C5 D5 C5 F5 E5 C5 C5 D5 C5 G5 F5:2"),
	("O Holy Night", "E5 E5 F5 G5 G5 F5 E5 D5 C5 D5 E5 G5 F5 E5:2"),
	("Beethoven's Fifth Symphony", "G4 G4 G4 EB4 F4 F4 F4 D4:2"),
	("Eine kleine Nachtmusik", "G5 D5 G5 D5 G5 D5 G5 B5 D6 D5 G5 B5 D6:2"),
	("Mozart Turkish March", "B4 A4 GS4 A4 C5:2 D5 C5 B4 C5 E5:2"),
	("The Blue Danube", "D5 G5 B5:2 B5 D6:2 C6 A5:2 A5:2 F5 A5:2 A5 C6:2"),
	("Can-Can", "A5 G5 F5 E5 D5 E5 F5 D5 E5 C5 D5 B4 C5:2"),
	("In the Hall of the Mountain King", "B4 CS5 D5 E5 FS5 D5 FS5 F5 D5 F5 E5 DS5 E5:2"),
	("William Tell Overture", "E5 E5 E5 G5 C6 C6 C6 E6 G5 G5 G5 E5 C5 E5 G5 C6:2"),
	("Pomp and Circumstance", "A5 GS5 A5 E5 A5 B5 C6:2 B5 A5 GS5 A5 E5:2"),
	("Wedding March (Mendelssohn)", "C5 G5 G5 G5 C5 G5 G5 G5 C5 G5 C6 B5 A5 G5 F5 E5 D5 C5:2"),
	("Here Comes the Bride", "F5 BB5 BB5 BB5:2 F5 C6 BB5 A5 BB5:2"),
	("Pachelbel's Canon", "FS5 E5 D5 CS5 B4 A4 B4 CS5 D5 CS5 B4 A4 G4 FS4 G4 E4:2"),
	("Minuet in G", "D5 G4 A4 B4 C5 D5 G4 G4 E5 C5 D5 E5 FS5 G5 G4 G4:2"),
	("The Entertainer", "D5 DS5 E5 C6 E5 C6 E5 C6:2 C6 D6 DS6 E6 C6 D6 E6 B5 D6 C6:2"),
	("Habanera (Carmen)", "D5 CS5 C5 B4 BB4 A4 GS4 G4 FS4 G4 GS4 A4:2"),
	("Toreador Song (Carmen)", "C5 A4 A4 BB4 C5 C5 C5 BB4 C5 D5 BB4 G4:2"),
	("Dance of the Sugar Plum Fairy", "E6 C6 GS5 C6 E6 C6 GS5 C6 E6 C6 GS5 B5 A5:2"),
	("Nutcracker March", "G5 E5 G5 E5 D5 F5 A5:2 G5 E5 G5 E5 D5 F5 G5:2"),
	("Swan Lake", "B4 E5 G5 FS5 E5 B5 A5 FS5 E5 G5 FS5 DS5 FS5 B4:2"),
	("1812 Overture", "C5 C5 G4 C5 E5 G5 C6 G5 E5 C5:2"),
	("Air on the G String", "D5 D5 CS5 D5 FS5 G5 A5 D5:2"),
	("Clair de Lune", "BB4 C5 D5 BB4 C5 D5 F5 EB5 D5 C5 BB4:2"),
	("Ave Maria", "F5 F5 G5 F5 F5 A5 F5 F5 C6 A5 F5 A5 G5 F5:2"),
	("Pac-Man Theme", "B5 B6 FS6 DS6 B6 FS6 DS6 C6 C7 G6 E6 C7 G6 E6"),
	("Indiana Jones Theme", "E5 F5 G5 C6:2 D5 E5 F5:2 G5 A5 B5 F6:2 A5 B5 C6 D6 E6:2"),
	("James Bond Theme", "B4 C5 C5 C5 C5 B4 B4 B4 B4 A4 B4 B4 E5:2"),
	("Mission Impossible Theme", "G5 G5 BB5 C6 G5 G5 F5 FS5 G5 G5 BB5 C6 G5 G5 F5 FS5"),
	("The Simpsons Theme", "C5 E5 FS5 A5 G5 E5 C5 A4 FS4 FS4 FS4 G4:2"),
	("Ghostbusters", "D5 D5 D5 D5 D5 D5 D5 C5 D5 D5 D5 F5 D5 C5 D5:2"),
	("Harry Potter (Hedwig's Theme)", "E5 A5 C6 B5 A5 E6 D6 B5:2 A5 C6 B5 GS5 BB5 E5:2"),
	("Pirates of the Caribbean", "E5 G5 A5 A5 A5 B5 C6 C6 C6 D6 B5 B5 A5 G5 A5:2"),
	("Game of Thrones Theme", "G4 C5 EB5 F5 G4 C5 EB5 F5 G4 C5 D5 F5 G4 C5 EB5 F5"),
	("Doctor Who Theme", "E4 E4 E4 E4 E4 E4 E4 G4 E4 D4 E4 B3 E4 E4 E4 E4 E4 E4 E4 A4 G4"),
	("The Lion Sleeps Tonight", "G5 A5 G5 E5 G5 A5 G5 E5 G5 A5 G5 E5 D5 E5:2"),
	("Moonlight Sonata", "GS4 CS5 E5 GS4 CS5 E5 GS4 CS5 E5 GS4 CS5 E5"),
]

for _title, _notation in SIMPLE_SONGS:
	_melody, _tempo = parse_notation(_notation)
	SONGS.append(Song(_title, _melody, _tempo, 0.30, 0.900))

