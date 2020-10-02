from threading import Thread
from queue import Queue
from constants import debug


def clear_queue(q):
    while not q.empty():
        q.get()
    return

class Bus_Registry(object):
    def __init__(self):
        self.registry = {}
    def get(self, name):
        return self.registry.get(name)
    def add(self, name, bus):
        self.registry[name] = bus
    def bus(self, name):
        if name not in self.registry:
            self.registry[name] = Queue(100)
        return self.registry.get(name)


class Actor_Registry(object):
    def __init__(self):
        self.registry = {}
    def get(self, name):
        return self.registry.get(name)
    def add(self, actor):
        name = actor.__class__.__name__
        self.registry[name] = actor

    def kill_all(self):
        for a in self.registry.values():
            a.kill()


class ActorThread(Thread):
    def __init__(self, bus=None):
        Thread.__init__(self, name=self.__class__.__name__)
        self.daemon = True
        self.keep_running = True
        self.bus = bus
        actor_registry.add(self)
        super().start()

    def run(self):
        debug(f"{self.__class__.__name__} started")
        while self.keep_running:
            self.event_loop()

        debug(f"{self.__class__.__name__} killed")
        return

    # def start(self):
    #     super().start()
    #     return self

    def kill(self):
        self.keep_running = False
    
    def cb_none(self, msg):
        debug(f"unknown callback triggered: {msg.get('event')}")

def post(bus_name, msg):
    b = bus_registry.bus(bus_name)
    b.put(msg)

def receive(bus_name):
    b = bus_registry.bus(bus_name)
    return b.get()

actor_registry = Actor_Registry()
bus_registry = Bus_Registry()
