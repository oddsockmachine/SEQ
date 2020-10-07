if __name__ == '__main__':
    from mido import open_output
    from time import sleep
    from pprint import pprint
    from button_grid import ButtonGrid
    from midiout import MidiOut, MidiClock
    from encoder import Encoder
    from trellis import Trellis
    from conductor import Conductor
    from actors import ActorThread, bus_registry, actor_registry, post, receive

    m = MidiOut(open_output('seq_out', autoreset=True, virtual=True)).start()
    c = MidiClock(120).start()
    e0 = Encoder(0).start()
    e1 = Encoder(1).start()
    e2 = Encoder(2).start()
    e3 = Encoder(3).start()
    c = Conductor().start()
    b = ButtonGrid().start()
    t = Trellis('i2cbusgoeshere').start()
