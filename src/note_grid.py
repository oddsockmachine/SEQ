from constants import debug
from datetime import datetime
from pprint import pprint
from config import H, W, STARTING_NOTE

from pixel import BLANK

class NoteGrid():
    """DataStructure to store notes on a grid"""
    def __init__(self):
        self.h = H
        self.w = W
        self.grid = [[Note() for x in range(self.w)] for y in range(self.h)]
        # grid[y][x]
        # x x x x x x x x
        # x x x x x x x x
        # x x x x x x x x
        # x x x x x x x x
        return

    def __repr__(self):
        return "\n".join([" ".join([str(x).ljust(3) for x in row]) for row in self.display()])
 
    def notes_at(self, x):
        return [self.grid[y][x] for y in range(H) if self.grid[y][x].active]

    def get(self, x, y):
        return self.grid[y][x]
    
    def add(self, x, y, note, velocity=64, duration=1, modulation=0):
        self.grid[y][x].on(note, velocity, duration, modulation)
        return

    def flip(self, x, y, velocity=64, duration=1, modulation=0):
        note = self.grid[y][x]
        if note.active:
            note.off()
        else:
            note.on(STARTING_NOTE+y, velocity, duration, modulation)
            
    
    def off(self, x, y):
        self.grid[y][x].off()
        return

    def note_to_bridghtness(self, note):
        if note.active:
            v = note.velocity
            b = v/2+63
            return int(b)
        return 0

    def set_velocity(self, x,y,v):
        # TODO constrain
        if self.grid[y][x].active:
            self.grid[y][x].velocity += v
        return

    def set_duration(self, x,y,d):
        # TODO constrain
        if self.grid[y][x].active:
            self.grid[y][x].duration += d
        return
    
    def set_modulation(self, x,y,d):
        # TODO constrain
        if self.grid[y][x].active:
            self.grid[y][x].modulation += d
        return

    def display(self):
        """Return a grid representing Led brightnesses based on Note velocties/durations"""
        d = [[BLANK for x in range(self.w)] for y in range(self.h)]
        for y, row in enumerate(self.grid):
            for x, note in enumerate(row):
                if not note.active:  # Don't bother if note isn't active
                    continue
                b = self.note_to_bridghtness(note)
                # d[y][x].type = NOTE
                d[y][x] = b
                # print(d[y][x])
                if note.duration > 1:  # If there is a sustain tail
                    for s in range(1,note.duration):  # For each cell in the sustail tail
                        if not self.grid[y][x+s].active:  # Cutoff if other note here
                            d[y][x+s] = int(b/2)  # Tail is half brightness
                            # print(d[y][x+s])
                            # t = int(b/2)
                            # d[y][x+s] = Pixel(t,t,t,NOTE)
                        else:
                            break
        return d


class Note():
    """Type to represent a single note"""
    def __init__(self):
        self.note = None
        self.velocity = None
        self.duration = None
        self.modulation = None
        self.active = False
        # self.channel 

    def on(self, note, velocity, duration, modulation):
        # TODO constrain veloctiy, duration, mod values
        self.active = True
        self.note = note
        self.velocity = velocity
        self.duration = duration
        self.modulation = modulation
    
    def off(self):
        self.active = False
        self.note = None
        self.velocity = None
        self.duration = None
        self.modulation = None
    

    
    def __repr__(self):
        if self.active:
            return str(type(self.note))
            return f"♪{self.note} v{self.velocity} b{self.duration} ~{self.modulation}"
        else:
            return "Empty note"

if __name__ == '__main__':
    n = Note()
    print(n)
    n.on(33, 99, 4, 123)
    print(n)
    ng = NoteGrid()
    # Random notes
    ng.add(3,2, 99)
    ng.add(5,4, 99)
    ng.add(7,5, 99)
    ng.add(8,5, 99)
    ng.add(9,5, 99)
    # Velocity > Brightness
    ng.add(16,0, 99, 1)
    ng.add(16,1, 99, 32)
    ng.add(16,2, 99, 64)
    ng.add(16,3, 99, 96)
    ng.add(16,4, 99, 127)
    # Sustain length
    ng.add(20,1, 99, 64, duration=1)
    ng.add(20,2, 99, 64, duration=2)
    ng.add(20,3, 99, 64, duration=3)
    ng.add(20,4, 99, 64, duration=4)
    ng.add(20,5, 99, 64, duration=5)
    ng.add(20,6, 99, 64, duration=6)
    ng.add(20,7, 99, 64, duration=7)
    # and clipping
    ng.add(24,6, 99, 64, duration=1)
    ng.add(24,7, 99, 64, duration=1)


    print(ng)
    print()
    print(ng.display())