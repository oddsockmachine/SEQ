from constants import debug
from actors import ActorThread, bus_registry, actor_registry, post, receive
from datetime import datetime


class ButtonGrid(ActorThread):
    """Listen to button presses, forward different click events"""
    def __init__(self):
        super().__init__()
        self.button_states = {}
        self.long_click_us = 500000

    def event_loop(self):
        # {'event': 'press/release', 'x': 0-31, 'y': 0-31}
        msg = receive('button_grid')
        # print(msg)
        event = msg.get('event')
        x = msg.get('x')
        y = msg.get('y')
        k_id = f"{x}.{y}"
        if event == "release":
            if k_id in self.button_states:
                hold_time = datetime.now() - self.button_states.get(k_id)
                self.button_states.pop(k_id)
                if int(hold_time.microseconds) > self.long_click_us:
                    msg['event'] = "long_click"
                else:
                    msg['event'] = "short_click"
                # print(msg)
                post('conductor', msg)
        if event == "press":
            self.button_states[k_id] = datetime.now()
            msg['event'] = "touch"
            post('conductor', msg)
            # print(msg)


if __name__ == "__main__":
    # trellis_bus = bus_registry.bus('trellis')
    conductor_bus = bus_registry.bus('conductor')
    t = ButtonGrid().start()
    print(t)
    from time import sleep
    post('button_grid', {'event': 'press', 'x': 1, 'y': 1})
    sleep(0.1)
    post('button_grid', {'event': 'release', 'x': 1, 'y': 1})
    sleep(0.1)

    post('button_grid', {'event': 'press', 'x': 1, 'y': 1})
    sleep(0.3)
    post('button_grid', {'event': 'release', 'x': 1, 'y': 1})
    sleep(0.1)

    post('button_grid', {'event': 'press', 'x': 1, 'y': 1})
    sleep(0.5)
    post('button_grid', {'event': 'release', 'x': 1, 'y': 1})
    sleep(0.1)

    post('button_grid', {'event': 'press', 'x': 2, 'y': 3})
    post('button_grid', {'event': 'press', 'x': 7, 'y': 8})
    sleep(0.4)
    post('button_grid', {'event': 'release', 'x': 7, 'y': 8})
    sleep(0.2)
    post('button_grid', {'event': 'release', 'x': 2, 'y': 3})
    sleep(0.2)
    post('button_grid', {'event': 'release', 'x': 99, 'y': 99})

    actor_registry.kill_all()
    sleep(0.5)

    for msg in conductor_bus.queue:
        print(msg)