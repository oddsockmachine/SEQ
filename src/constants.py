# coding=utf-8

# Log to a file, good for debugging
import logging
logging.basicConfig(filename='sequencer.log', level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')
debug = logging.debug
save_location = './saved/'
save_extension = '.json'

# The ints used to represent the state of leds on an led_grid
LED_BLANK = 0  # TODO rename to seq_
LED_CURSOR = 1
LED_ACTIVE = 2
LED_SELECT = 3
LED_BEAT = 4
LED_SCALE_PRIMARY = 5
LED_SCALE_SECONDARY = 6
LED_EDIT = 4
DROPLET_MOVING = 7
DROPLET_SPLASH = 8
DROPLET_STOPPED = 9
DROPLET_HEIGHT = 10

DRUM_OFF = 11
DRUM_SELECT = 12
DRUM_ACTIVE = 13
DRUM_CHANGED = 14

SLIDER_TOP = 20
SLIDER_BODY = 21

INSTRUMENT_A = 90
INSTRUMENT_B = 91
INSTRUMENT_C = 92
INSTRUMENT_D = 93

KEY_BLACK = 80
KEY_WHITE = 81
KEY_ROOT = 82
KEY_SCALE = 83


# The ints used to represent the state of notes on a note_grid
NOTE_OFF = 0
NOTE_ON = 3

TICK = 1
BEAT = 2

pallette_lookup = {
    LED_BLANK: 'BLANK',
    LED_CURSOR: 'CURSOR',
    LED_ACTIVE: 'ACTIVE',
    LED_SELECT: 'SELECT',
    LED_BEAT: 'BEAT',
    LED_SCALE_PRIMARY: 'SCALE_PRIMARY',
    LED_SCALE_SECONDARY: 'SCALE_SECONDARY',
    DROPLET_MOVING: 'DROPLET_MOVING',
    DROPLET_SPLASH: 'DROPLET_SPLASH',
    DROPLET_STOPPED: 'DROPLET_STOPPED',
    DRUM_OFF: 'DRUM_OFF',
    DRUM_SELECT: 'DRUM_SELECT',
    DRUM_ACTIVE: 'DRUM_ACTIVE',
    DRUM_CHANGED: 'DRUM_CHANGED',
    SLIDER_TOP: 'SLIDER_TOP',
    SLIDER_BODY: 'SLIDER_BODY',
    INSTRUMENT_A: 'INSTRUMENT_A',
    INSTRUMENT_B: 'INSTRUMENT_B',
    INSTRUMENT_C: 'INSTRUMENT_C',
    INSTRUMENT_D: 'INSTRUMENT_D',
}

# The glyphs used to display cell information/states in the CLI
# DISPLAY = {0: '. ', 1:'  ', 2:'OO', 3:'XX'}
DISPLAY = {0: '. ',
           1: '░░',
           2: '▒▒',
           3: '▓▓',
           4: '▒▒',
           7: '░░',
           9: '▒▒',
           8: '▓▓',
           21: '▒▒',
           20: '▓▓',
           80: '░░',
           81: '░░',
           82: '▒▒',
           83: '▓▓',
           90: 'xx',
           91: 'XX',
           92: '//',
           93: r'\\',
           }

W = 16  # Width of the display grid
H = 16  # Width of the display grid

# Maximum number of instruments - limited by 16 available midi channels,
# but we may want to run 2 separate sequencers with 8 channels in future
MAX_INSTRUMENTS = 16

# Note letters
A = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
    [1, 0, 1],
    [1, 0, 1],
]
B = [
    [1, 0, 0],
    [1, 0, 0],
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
]
C = [
    [1, 1, 1],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 1, 1],
]
D = [
    [0, 0, 1],
    [0, 0, 1],
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
]
E = [
    [1, 1, 1],
    [1, 0, 0],
    [1, 1, 0],
    [1, 0, 0],
    [1, 1, 1],
]
F = [
    [1, 1, 1],
    [1, 0, 0],
    [1, 1, 0],
    [1, 0, 0],
    [1, 0, 0],
]
G = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 0, 1],
    [1, 1, 1],
]
h = [
    [1, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [1, 0, 1],
    [1, 0, 1],
]
I = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0],
]
L = [
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 1, 1],
]
M = [
    [1, 0, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 0, 1],
    [1, 0, 1],
]
O = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
]
P = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
    [1, 0, 0],
    [1, 0, 0],
]
R = [
    [1, 1, 0],
    [1, 0, 1],
    [1, 1, 0],
    [1, 0, 1],
    [1, 0, 1],
]
S = [
    [1, 1, 1],
    [1, 0, 0],
    [1, 1, 1],
    [0, 0, 1],
    [1, 1, 1],
]
X = [
    [1, 0, 1],
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1],
    [1, 0, 1],
]
Y = [
    [1, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 0],
    [0, 1, 0],
]
PLUS = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0],
    [0, 0, 0],
]
MINUS = [
    [0, 0, 0],
    [0, 0, 0],
    [1, 1, 1],
    [0, 0, 0],
    [0, 0, 0],
]
SHARP = [
    [0, 0, 0],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [0, 0, 0],
]
SPACE = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

ROW = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ]]
COLUMN = [[INSTRUMENT_A], [INSTRUMENT_B], [INSTRUMENT_C], [INSTRUMENT_D],
          [INSTRUMENT_A], [INSTRUMENT_B], [INSTRUMENT_C], [INSTRUMENT_D],
          [INSTRUMENT_A], [INSTRUMENT_B], [INSTRUMENT_C], [INSTRUMENT_D],
          [INSTRUMENT_A], [INSTRUMENT_B], [INSTRUMENT_C], [INSTRUMENT_D], ]
INSTRUMENTS = [[INSTRUMENT_A], [INSTRUMENT_B], [INSTRUMENT_C], [INSTRUMENT_D],
               [INSTRUMENT_A], [INSTRUMENT_B], [INSTRUMENT_C], [INSTRUMENT_D],
               [INSTRUMENT_A], [INSTRUMENT_B], [INSTRUMENT_C], [INSTRUMENT_D],
               [INSTRUMENT_A], [INSTRUMENT_B], [INSTRUMENT_C], [INSTRUMENT_D], ]
NUM_INSTRUMENTS = {
    0: INSTRUMENTS[:0],
    1: INSTRUMENTS[:1],
    2: INSTRUMENTS[:2],
    3: INSTRUMENTS[:3],
    4: INSTRUMENTS[:4],
    5: INSTRUMENTS[:5],
    6: INSTRUMENTS[:6],
    7: INSTRUMENTS[:7],
    8: INSTRUMENTS[:8],
    9: INSTRUMENTS[:9],
    10: INSTRUMENTS[:10],
    11: INSTRUMENTS[:11],
    12: INSTRUMENTS[:12],
    13: INSTRUMENTS[:13],
    14: INSTRUMENTS[:14],
    15: INSTRUMENTS[:15],
    16: INSTRUMENTS[:16],
}

SCALE_CHARS = {
    'ionian':          'io',
    'dorian':          'do',
    'phrygian':        'ph',
    'lydian':          'ly',
    'mixolydian':      'mx',
    'aeolian':         'ae',
    'locrian':         'lo',
    'major':           'ma',
    'minor':           'mi',
    'pentatonic_maj':  'p+',
    'pentatonic_min':  'p-',
    'chromatic':       'ch',
}

LETTERS = {'a': A, 'b': B, 'c': C, 'd': D, 'e': E, 'f': F, 'g': G, 'h': h, 'i': I, 'l': L, 'm': M,
           'o': O, 'p': P, 'r': R, 's': S, 'x': X, 'y': Y,
           '+': PLUS, '-': MINUS, '#': SHARP, ' ':  SPACE, 'num_instruments': INSTRUMENTS}


SINE_WAVE = [64,64,65,65,66,66,66,67,67,68,68,68,69,69,69,70,70,71,71,71,72,72,73,73,73,74,74,75,75,75,76,76,76,77,77,78,78,78,79,79,80,80,80,81,81,81,82,82,83,83,83,84,84,84,85,85,86,86,86,87,87,87,88,88,
88,89,89,90,90,90,91,91,91,92,92,92,93,93,93,94,94,95,95,95,96,96,96,97,97,97,98,98,98,99,99,99,100,100,100,101,101,101,101,102,102,102,103,103,103,104,104,104,105,105,105,106,106,106,106,107,107,107,108,108,108,108,109,109,
109,110,110,110,110,111,111,111,111,112,112,112,112,113,113,113,113,114,114,114,114,115,115,115,115,116,116,116,116,117,117,117,117,117,118,118,118,118,118,119,119,119,119,119,120,120,120,120,120,121,121,121,121,121,122,122,122,122,122,122,123,123,123,123,
123,123,123,124,124,124,124,124,124,124,125,125,125,125,125,125,125,125,125,126,126,126,126,126,126,126,126,126,126,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,
128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,126,126,126,126,126,126,126,126,126,126,125,125,125,125,125,125,125,125,125,124,124,124,124,124,124,124,123,123,
123,123,123,123,123,122,122,122,122,122,122,121,121,121,121,121,120,120,120,120,120,119,119,119,119,119,118,118,118,118,118,117,117,117,117,117,116,116,116,116,115,115,115,115,114,114,114,114,113,113,113,113,112,112,112,112,111,111,111,111,110,110,110,110,
109,109,109,108,108,108,108,107,107,107,106,106,106,106,105,105,105,104,104,104,103,103,103,102,102,102,101,101,101,101,100,100,100,99,99,99,98,98,98,97,97,97,96,96,96,95,95,95,94,94,93,93,93,92,92,92,91,91,91,90,90,90,89,89,
88,88,88,87,87,87,86,86,86,85,85,84,84,84,83,83,83,82,82,81,81,81,80,80,80,79,79,78,78,78,77,77,76,76,76,75,75,75,74,74,73,73,73,72,72,71,71,71,70,70,69,69,69,68,68,68,67,67,66,66,66,65,65,64,
64,64,63,63,62,62,62,61,61,60,60,60,59,59,59,58,58,57,57,57,56,56,55,55,55,54,54,53,53,53,52,52,52,51,51,50,50,50,49,49,48,48,48,47,47,47,46,46,45,45,45,44,44,44,43,43,42,42,42,41,41,41,40,40,
40,39,39,38,38,38,37,37,37,36,36,36,35,35,35,34,34,33,33,33,32,32,32,31,31,31,30,30,30,29,29,29,28,28,28,27,27,27,27,26,26,26,25,25,25,24,24,24,23,23,23,22,22,22,22,21,21,21,20,20,20,20,19,19,
19,18,18,18,18,17,17,17,17,16,16,16,16,15,15,15,15,14,14,14,14,13,13,13,13,12,12,12,12,11,11,11,11,11,10,10,10,10,10,9,9,9,9,9,8,8,8,8,8,7,7,7,7,7,6,6,6,6,6,6,5,5,5,5,
5,5,5,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,5,5,
5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,8,8,8,8,8,9,9,9,9,9,10,10,10,10,10,11,11,11,11,11,12,12,12,12,13,13,13,13,14,14,14,14,15,15,15,15,16,16,16,16,17,17,17,17,18,18,18,18,
19,19,19,20,20,20,20,21,21,21,22,22,22,22,23,23,23,24,24,24,25,25,25,26,26,26,27,27,27,27,28,28,28,29,29,29,30,30,30,31,31,31,32,32,32,33,33,33,34,34,35,35,35,36,36,36,37,37,37,38,38,38,39,39,
40,40,40,41,41,41,42,42,42,43,43,44,44,44,45,45,45,46,46,47,47,47,48,48,48,49,49,50,50,50,51,51,52,52,52,53,53,53,54,54,55,55,55,56,56,57,57,57,58,58,59,59,59,60,60,60,61,61,62,62,62,63,63,64,]


SAWTOOTH_WAVE = [0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13,14,14,14,14,15,15,15,15,16,16,16,
16,17,17,17,17,18,18,18,18,19,19,19,19,20,20,20,20,21,21,21,21,22,22,22,22,23,23,23,23,24,24,24,24,25,25,25,25,26,26,26,26,27,27,27,27,28,28,28,28,29,29,29,29,30,30,30,30,31,31,31,31,32,32,32,
32,33,33,33,33,34,34,34,34,35,35,35,35,36,36,36,36,37,37,37,37,38,38,38,38,39,39,39,39,40,40,40,40,41,41,41,41,42,42,42,42,43,43,43,43,44,44,44,44,45,45,45,45,46,46,46,46,47,47,47,47,48,48,48,
48,49,49,49,49,50,50,50,50,51,51,51,51,52,52,52,52,53,53,53,53,54,54,54,54,55,55,55,55,56,56,56,56,57,57,57,57,58,58,58,58,59,59,59,59,60,60,60,60,61,61,61,61,62,62,62,62,63,63,63,63,64,64,64,
64,65,65,65,65,66,66,66,66,67,67,67,67,68,68,68,68,69,69,69,69,70,70,70,70,71,71,71,71,72,72,72,72,73,73,73,73,74,74,74,74,75,75,75,75,76,76,76,76,77,77,77,77,78,78,78,78,79,79,79,79,80,80,80,
80,81,81,81,81,82,82,82,82,83,83,83,83,84,84,84,84,85,85,85,85,86,86,86,86,87,87,87,87,88,88,88,88,89,89,89,89,90,90,90,90,91,91,91,91,92,92,92,92,93,93,93,93,94,94,94,94,95,95,95,95,96,96,96,
96,97,97,97,97,98,98,98,98,99,99,99,99,100,100,100,100,101,101,101,101,102,102,102,102,103,103,103,103,104,104,104,104,105,105,105,105,106,106,106,106,107,107,107,107,108,108,108,108,109,109,109,109,110,110,110,110,111,111,111,111,112,112,112,
112,113,113,113,113,114,114,114,114,115,115,115,115,116,116,116,116,117,117,117,117,118,118,118,118,119,119,119,119,120,120,120,120,121,121,121,121,122,122,122,122,123,123,123,123,124,124,124,124,125,125,125,125,126,126,126,126,127,127,127,127,128,128,128,
128,128,127,127,127,127,126,126,126,126,125,125,125,125,124,124,124,124,123,123,123,123,122,122,122,122,121,121,121,121,120,120,120,120,119,119,119,119,118,118,118,118,117,117,117,117,116,116,116,116,115,115,115,115,114,114,114,114,113,113,113,113,112,112,
112,112,111,111,111,111,110,110,110,110,109,109,109,109,108,108,108,108,107,107,107,107,106,106,106,106,105,105,105,105,104,104,104,104,103,103,103,103,102,102,102,102,101,101,101,101,100,100,100,100,99,99,99,99,98,98,98,98,97,97,97,97,96,96,
96,96,95,95,95,95,94,94,94,94,93,93,93,93,92,92,92,92,91,91,91,91,90,90,90,90,89,89,89,89,88,88,88,88,87,87,87,87,86,86,86,86,85,85,85,85,84,84,84,84,83,83,83,83,82,82,82,82,81,81,81,81,80,80,
80,80,79,79,79,79,78,78,78,78,77,77,77,77,76,76,76,76,75,75,75,75,74,74,74,74,73,73,73,73,72,72,72,72,71,71,71,71,70,70,70,70,69,69,69,69,68,68,68,68,67,67,67,67,66,66,66,66,65,65,65,65,64,64,
64,64,63,63,63,63,62,62,62,62,61,61,61,61,60,60,60,60,59,59,59,59,58,58,58,58,57,57,57,57,56,56,56,56,55,55,55,55,54,54,54,54,53,53,53,53,52,52,52,52,51,51,51,51,50,50,50,50,49,49,49,49,48,48,
48,48,47,47,47,47,46,46,46,46,45,45,45,45,44,44,44,44,43,43,43,43,42,42,42,42,41,41,41,41,40,40,40,40,39,39,39,39,38,38,38,38,37,37,37,37,36,36,36,36,35,35,35,35,34,34,34,34,33,33,33,33,32,32,
32,32,31,31,31,31,30,30,30,30,29,29,29,29,28,28,28,28,27,27,27,27,26,26,26,26,25,25,25,25,24,24,24,24,23,23,23,23,22,22,22,22,21,21,21,21,20,20,20,20,19,19,19,19,18,18,18,18,17,17,17,17,16,16,
16,16,15,15,15,15,14,14,14,14,13,13,13,13,12,12,12,12,11,11,11,11,10,10,10,10,9,9,9,9,8,8,8,8,7,7,7,7,6,6,6,6,5,5,5,5,4,4,4,4,3,3,3,3,2,2,2,2,1,1,1,1,0,0,]