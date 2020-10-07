from recordclass import recordclass
Pixel = recordclass('Pixel', 'R G B type')

BLANK = -1
NOTE = -2
SELECTED = -3
BEAT = -4
TAIL = -5