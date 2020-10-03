from constants import debug
from actors import ActorThread, bus_registry, actor_registry, post, receive
from datetime import datetime
from note_grid import NoteGrid

class Instrument(ActorThread):
    """"""
    def __init__(self, ins_num):
        super().__init__()
        self.id = ins_num
        self.grid = NoteGrid()
        self.beat = 0
        self.playing = False
        self.selected_note = None

    def event_loop(self):
        msg = receive(f"instrument{self.id}")
        event = msg.get('event')
        cb_name = f"cb_{event}"
        result = getattr(self, cb_name, self.cb_none)(msg)

    def cb_ctl_play(self, msg):
        self.playing = True
        return
    def cb_ctl_step(self, msg):
        if self.playing:
            self.beat += 1
            post("midi_out", {})
        return
    def cb_ctl_stop(self, msg):
        self.playing = False
        print("stop")
        return
    def cb_touch(self, msg):
        self.selected_note = None
        return
    def cb_short_click(self, msg):
        self.selected_note = None
        x = msg.get('x')
        y = msg.get('y')
        self.grid.flip(x, y, 99)
        # Select note x,y, save in self, allow manipulation by dials
        return
    def cb_long_click(self, msg):
        self.selected_note = (msg.get('x'), msg.get('y'))
        # Select note x,y, save in self, allow manipulation by dials
        return
    def cb_dial_turn(self, msg):
        if not self.selected_note:
            return
        dir = msg.get('dir')
        x, y = self.selected_note
        if dir == '+':
            self.grid.set_velocity(x,y,1)
        elif dir == '-':
            self.grid.set_velocity(x,y,-1)
        return
    def cb_dial_click(self, msg):
        return
    
if __name__ == '__main__':
    from time import sleep
    i = Instrument(0).start()
    post('instrument0', {'event': 'ctl_stop', 'foo': 'bar'})
    post('instrument0', {'event': 'foo', 'foo': 'bar'})
    post('instrument0', {'event': 'touch_click', 'x': 0, 'y': 1})
    post('instrument0', {'event': 'ctl_step'})
    sleep(1)
    print(i.grid.display())
    sleep(1)