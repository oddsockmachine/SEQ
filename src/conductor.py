from constants import debug
from actors import ActorThread, bus_registry, actor_registry, post, receive
from instrument import Instrument
from config import H, W


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
        led_grid = self.instruments[self.current_instrument].grid.display()
        led_grid = self.add_gridlines(led_grid)
        post('trellis', {'event': 'draw_grid', 'led_grid': led_grid})

    def add_gridlines(self, led_grid):
        print(self.beat)
        for y in range(H):
            led_grid[y][self.beat] = -1
        return led_grid

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
