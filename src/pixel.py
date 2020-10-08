from recordclass import recordclass
Pixel = recordclass('Pixel', 'R G B')

BLANK = -1
NOTE = -2
SELECTED = -3
BEAT = -4
BEAT_ON = -8
TAIL = -5
GRID_4 = -6
GRID_8 = -7

g_from = (1,21,1)
g_to = (1,1,21)

brightness = 1/1

pallette = {
  BLANK: (1, 1, 1),
  NOTE: (150, 150, 150),
  SELECTED: (200, 200, 200),
  BEAT: (50, 50, 50),
  BEAT_ON: (150, 150, 150),
  TAIL: (100, 100, 100),
  GRID_4: (10, 10, 10),
  GRID_8: (20, 20, 20),
}

def color_scheme(_type, x, y):
    return pallette.get(_type, (_type, _type, _type))
