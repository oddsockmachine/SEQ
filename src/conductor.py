from constants import debug
from actors import ActorThread, bus_registry, actor_registry, post, receive
from instrument import Instrument
from config import H, W
from pixel import GRID_4, GRID_8, BEAT, BEAT_ON, SELECTED, NOTE, BLANK, color_scheme

class Conductor(ActorThread):
    """Multiplexor of instruments"""
    def __init__(self):
        super().__init__()
        self.instruments = [Instrument(i).start() for i in range(H)]
        self.current_instrument = 0
        self.beat = 0
        self.playing = False

    def post_to_ins(self, msg):
        post(f"instrument{self.current_instrument}", msg)

    def cb_display(self, msg):
        # Raw grid of notes, velocities and tails
        led_grid = self.instruments[self.current_instrument].grid.display()
        # Add ornamentation
        for y in range(H):
            # add_gridlines
            for x in range(3, W, 8):
                if led_grid[y][x] == BLANK:
                    led_grid[y][x] = GRID_4
                if led_grid[y][x+4] == BLANK:
                    led_grid[y][x+4] = GRID_8
            # add_beat_marker
            if led_grid[y][self.beat] == NOTE:
                led_grid[y][self.beat] = BEAT_ON
            else:
                led_grid[y][self.beat] = BEAT
        # add_selected_note
        s_n = self.instruments[self.current_instrument].selected_note
        if s_n:
            led_grid[s_n[1]][s_n[0]] = SELECTED
        # Convert according to color scheme
        for y in range(H):
            for x in range(W):
                led_grid[y][x] = color_scheme(led_grid[y][x], x, y)
        post('trellis', {'event': 'draw_grid', 'led_grid': led_grid})
        return
        



    def cb_midi_tick(self, msg):
        self.beat = (self.beat + 1) % W
        for i in range(len(self.instruments)):
            post(f"instrument{i}", msg)
        self.cb_display({})
    
    def cb_select_ins(self, msg):
        ins = msg['instrument']
        if ins == '+':
            self.current_instrument = (self.current_instrument + 1) % H
        elif ins == '-':
            self.current_instrument = (self.current_instrument - 1) % H
        elif type(ins) == int:
            self.current_instrument = ins
        return

    def cb_encoder_0(self, msg):
        action = msg['action']
        if action == 'push':
            print("Push not implemented yet")
            return
        dir = 1 if action == "inc" else -1
        self.current_instrument = (self.current_instrument + dir) % H
        return

    def cb_encoder_1(self, msg):
        return

    # def cb_encoder_2(self, msg):
    #     return

    def cb_encoder_3(self, msg):
        self.post_to_ins(msg)
        return

    def event_loop(self):
        # Not using default, because fall-through behaviour is to delegate to current instrument
        msg = receive("conductor")
        event = msg.get('event')
        cb_name = f"cb_{event}"
        getattr(self, cb_name, self.post_to_ins)(msg)
