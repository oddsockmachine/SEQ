if __name__ == '__main__':
    from time import sleep
    from pprint import pprint
    from button_grid import ButtonGrid
    from midiout import MidiOut, MidiClock
    from encoder import Encoder
    from trellis import Trellis
    from conductor import Conductor
    from actors import ActorThread, bus_registry, actor_registry, post, receive
    m = MidiOut().start()
    c = MidiClock(120).start()
    e0 = Encoder(0).start()
    e1 = Encoder(1).start()
    e2 = Encoder(2).start()
    e3 = Encoder(3).start()
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
    post('button_grid', {'event': 'press', 'x': 2, 'y': 2})
    sleep(0.001)
    post('button_grid', {'event': 'release', 'x': 2, 'y': 2})
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

    post('button_grid', {'event': 'press', 'x': 5, 'y': 5})
    sleep(0.5)
    post('button_grid', {'event': 'release', 'x': 5, 'y': 5})
    sleep(0.1)

    post('button_grid', {'event': 'press', 'x': 2, 'y': 3})
    post('button_grid', {'event': 'press', 'x': 5, 'y': 5})
    sleep(0.4)
    post('button_grid', {'event': 'release', 'x': 5, 'y': 5})
    sleep(0.2)
    post('button_grid', {'event': 'release', 'x': 2, 'y': 3})
    sleep(0.2)
    post('button_grid', {'event': 'release', 'x': 5, 'y': 6})
    post('conductor', {'event': 'select_ins', 'instrument': 1})
    post('conductor', {'event': 'select_ins', 'instrument': '-'})
    post('conductor', {'event': 'select_ins', 'instrument': '-'})
    post('conductor', {'event': 'select_ins', 'instrument': '+'})
    for i in range(20):
        e2.on_inc()
    for i in range(20):
        e3.on_inc()
    sleep(0.1)
    pprint(c.instruments[c.current_instrument].grid)
    
    post('encoder0', {'event': 'set_color'})
    post('encoder0', {'event': 'foo'})
    e0.on_dec()
    e0.on_dec()
    e0.on_dec()
    e0.on_inc()
    sleep(1)
    bus_registry.purge()
