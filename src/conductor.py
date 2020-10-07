from constants import debug
from actors import ActorThread, bus_registry, actor_registry, post, receive
from instrument import Instrument
from config import H


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
        post('trellis', {'event': 'draw_grid', 'led_grid': led_grid})

    def cb_midi_tick(self, msg):
        self.beat += 1
        # self.post_to_ins(msg)
        # Send tick to all instruments
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
        dir = 1 if action == "inc" else -1
        self.current_instrument = (self.current_instrument + dir) % H
        print(self.current_instrument)
        return

    # def cb_touch(self, msg):
    #     self.post_to_ins(msg)
    # def cb_short_click(self, msg):
    #     self.post_to_ins(msg)
    # def cb_long_click(self, msg):
    #     self.post_to_ins(msg)
    def event_loop(self):
        # Not using default, because fall-through behaviour is to delegate to current instrument
        msg = receive("conductor")
        event = msg.get('event')
        cb_name = f"cb_{event}"
        result = getattr(self, cb_name, self.post_to_ins)(msg)

if __name__ == '__main__':
    from time import sleep
    from pprint import pprint
    from button_grid import ButtonGrid
    from midiout import MidiOut, MidiClock
    from encoder import Encoder
    from trellis import Trellis
    m = MidiOut().start()
    c = MidiClock(120).start()
    e = Encoder(0).start()
    c = Conductor().start()
    b = ButtonGrid().start()
    t = Trellis('i2cbusgoeshere').start()
    post('button_grid', {'event': 'press', 'x': 1, 'y': 1})
    sleep(0.001)
    post('button_grid', {'event': 'release', 'x': 1, 'y': 1})
    sleep(0.001)


    post('button_grid', {'event': 'press', 'x': 3, 'y': 3})
    sleep(0.001)
    post('button_grid', {'event': 'release', 'x': 3, 'y': 3})
    sleep(0.001)
    post('button_grid', {'event': 'press', 'x': 5, 'y': 5})
    sleep(0.001)
    post('button_grid', {'event': 'release', 'x': 5, 'y': 5})
    sleep(0.001)
    post('button_grid', {'event': 'press', 'x': 7, 'y': 7})
    sleep(0.001)
    post('button_grid', {'event': 'release', 'x': 7, 'y': 7})
    sleep(0.001)
    post('button_grid', {'event': 'press', 'x': 4, 'y': 4})
    sleep(0.001)
    post('button_grid', {'event': 'release', 'x': 4, 'y': 4})
    sleep(0.001)


    post('button_grid', {'event': 'press', 'x': 1, 'y': 1})
    sleep(0.3)
    post('button_grid', {'event': 'release', 'x': 1, 'y': 1})
    sleep(0.1)

    post('button_grid', {'event': 'press', 'x': 1, 'y': 2})
    sleep(0.3)
    post('button_grid', {'event': 'release', 'x': 1, 'y': 2})
    sleep(0.1)

    post('button_grid', {'event': 'press', 'x': 1, 'y': 1})
    sleep(0.5)
    post('button_grid', {'event': 'release', 'x': 1, 'y': 1})
    sleep(0.1)

    post('button_grid', {'event': 'press', 'x': 2, 'y': 3})
    post('button_grid', {'event': 'press', 'x': 7, 'y': 7})
    sleep(0.4)
    post('button_grid', {'event': 'release', 'x': 7, 'y': 7})
    sleep(0.2)
    post('button_grid', {'event': 'release', 'x': 2, 'y': 3})
    sleep(0.2)
    post('button_grid', {'event': 'release', 'x': 5, 'y': 6})
    post('conductor', {'event': 'select_ins', 'instrument': 1})
    post('conductor', {'event': 'select_ins', 'instrument': '-'})
    post('conductor', {'event': 'select_ins', 'instrument': '-'})
    post('conductor', {'event': 'select_ins', 'instrument': '+'})
    sleep(0.1)
    pprint(c.instruments[c.current_instrument].grid)
    
    post('encoder0', {'event': 'set_color'})
    post('encoder0', {'event': 'foo'})
    e.on_dec()
    e.on_dec()
    e.on_dec()
    e.on_inc()
    sleep(1)
    bus_registry.purge()
