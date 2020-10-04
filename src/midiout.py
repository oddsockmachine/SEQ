from constants import debug
from actors import ActorThread, bus_registry, actor_registry, post, receive
from datetime import datetime

from time import sleep
import mido


class MidiClock(ActorThread):
    """Creates a regular Midi clock beat for internal and external sync"""
    def __init__(self, bpm):
        super().__init__()
        self.bpm = bpm
        self.delay_s = 60 / bpm / 4

    def event_loop(self):
        # Custom event loop
        sleep(self.delay_s)
        post("midiout", {'event': "tick"})
        post("conductor", {'event': "midi_tick"})

class MidiOut(ActorThread):
    """Handle sending Midi messages to external devices"""
    def __init__(self):
        super().__init__()
        self.notes_on = {}
        self.internal_clock = 0

    def cb_tick(self, msg):
        self.internal_clock += 1
        off_notes = [note_id for note_id, off_time in self.notes_on.items() if off_time <= self.internal_clock] 
        for off_note in off_notes:
            channel, note = off_note.split('.')
            print(mido.Message('note_off', note=int(note), channel=int(channel)))
            self.notes_on.pop(off_note)
        return
    def cb_note_on(self, msg):
        if msg.get('event') == 'note_on':
            for n in msg.get('notes'):
                print(n)
                print(mido.Message('note_on', note=n.note, channel=msg.get('channel'), velocity=n.velocity))
                # TODO Send MIDO MSG
                id = f"{msg.get('channel')}.{n.note}"
                self.notes_on[id] = self.internal_clock + n.duration
        return

if __name__ == "__main__":
    midi_bus = bus_registry.bus('midi_out')
    m = MidiOut().start()
    c = MidiClock(120).start()
    # midi_bus.put(mido.Message('note_on', note=55, channel=1, velocity=99, duration=3))
    midi_bus.put({'event': 'note_on', 'note': 33, 'channel': 1, 'velocity': 99, 'duration': 5})
    midi_bus.put({'event': 'note_on', 'note': 22, 'channel': 1, 'velocity': 99, 'duration': 4})
    sleep(1)
    midi_bus.put({'event': 'note_on', 'note': 22, 'channel': 2, 'velocity': 99, 'duration': 6})
    midi_bus.put({'event': 'note_on', 'note': 22, 'channel': 1, 'velocity': 99, 'duration': 1})
    sleep(0.2)
    midi_bus.put({'event': 'note_on', 'note': 22, 'channel': 2, 'velocity': 99, 'duration': 1})
    midi_bus.put({'event': 'note_on', 'note': 22, 'channel': 1, 'velocity': 99, 'duration': 3})
    
    sleep(1)
