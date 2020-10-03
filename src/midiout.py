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
        sleep(self.delay_s)
        post("midi_out", {'type': "tick"})

class MidiOut(ActorThread):
    """Handle sending Midi messages to external devices"""
    def __init__(self):
        super().__init__()
        self.notes_on = {}
        self.internal_clock = 0

    def event_loop(self):
        # {'type': 'note_on', 'note': 22, 'channel': 1, 'velocity': 99, 'duration': 1}
        msg = receive('midi_out')
        if msg.get('type') == 'tick':
            self.cb_tick(msg)
        if msg.get('type') == 'note_on':
           self.cb_note_on(msg)
        return

    def cb_tick(self, msg):
        self.internal_clock += 1
        off_notes = [note_id for note_id, off_time in self.notes_on.items() if off_time <= self.internal_clock] 
        for off_note in off_notes:
            channel, note = off_note.split('.')
            print(mido.Message('note_off', note=int(note), channel=int(channel)))
            self.notes_on.pop(off_note)
        return
    def cb_note_on(self, msg):
        if msg.get('type') == 'note_on':
            print(mido.Message('note_on', note=msg['note'], channel=msg['channel'], velocity=msg['velocity']))
            # Send
            id = f"{msg['channel']}.{msg['note']}"
            self.notes_on[id] = self.internal_clock + msg['duration']
        return

if __name__ == "__main__":
    midi_bus = bus_registry.bus('midi_out')
    m = MidiOut().start()
    c = MidiClock(120).start()
    # midi_bus.put(mido.Message('note_on', note=55, channel=1, velocity=99, duration=3))
    midi_bus.put({'type': 'note_on', 'note': 33, 'channel': 1, 'velocity': 99, 'duration': 5})
    midi_bus.put({'type': 'note_on', 'note': 22, 'channel': 1, 'velocity': 99, 'duration': 4})
    sleep(1)
    midi_bus.put({'type': 'note_on', 'note': 22, 'channel': 2, 'velocity': 99, 'duration': 6})
    midi_bus.put({'type': 'note_on', 'note': 22, 'channel': 1, 'velocity': 99, 'duration': 1})
    sleep(0.2)
    midi_bus.put({'type': 'note_on', 'note': 22, 'channel': 2, 'velocity': 99, 'duration': 1})
    midi_bus.put({'type': 'note_on', 'note': 22, 'channel': 1, 'velocity': 99, 'duration': 3})
    
    sleep(1)
