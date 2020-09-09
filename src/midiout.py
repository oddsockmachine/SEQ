from constants import debug
from actors import ActorThread, bus_registry, actor_registry, post, receive
from datetime import datetime


class MidiOut(ActorThread):
    """Listen to button presses, forward different click events"""
    # event: press/release
    # x, y: 0-31.0-31
    def __init__(self):
        super().__init__()
        self.notes_on = {}

    def event_loop(self):
        msg = receive('midi_out')
        # TODO need regular midi clock here to trigger note off events
        note = msg.get('note')
        channel = msg.get('channel')
        vel = msg.get('velocity')
        duration = msg.get('duration')
        # midi.write(midi(channel, note, vel))
        n_id = f"{channel}.{note}"
        if n_id not in self.notes_on:  # TODO what about 2 same notes, different durations? Choke or sustain?
            msg['stop_time']
            self.notes_on[n_id] = msg
        
        for msg in self.notes_on:
            if msg.duration

        # k_id = f"{x}.{y}"
        # if event == "release":
        #     if k_id in self.button_states:
        #         hold_time = datetime.now() - self.button_states.get(k_id)
        #         self.button_states.pop(k_id)
        #         if int(hold_time.microseconds) > self.long_click_us:
        #             msg['event'] = "long_click"
        #         else:
        #             msg['event'] = "short_click"
        #         post('action', msg)
        # if event == "press":
        #     self.button_states[k_id] = datetime.now()
        #     msg['event'] = "touch"
        #     post('action', msg)
