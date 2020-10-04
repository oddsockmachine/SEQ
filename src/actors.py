from threading import Thread
from queue import Queue
from constants import debug
import re
pattern = re.compile(r'(?<!^)(?=[A-Z])')

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
    def purge(self):
        for name, bus in self.registry.items():
            if not bus.empty():
                print(name)
                print(bus.qsize())


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
    def __init__(self, name=None):
        if not name:
            name=self.__class__.__name__.lower()
            # name = re.sub(r'(?<!^)(?=[A-Z])', '_', self.__class__.__name__).lower()
            # name = pattern.sub('_', self.__class__.__name__).lower()
        print(name)
        Thread.__init__(self, name=name)
        self.daemon = True
        self.keep_running = True
        actor_registry.add(self)
        self.name = name
    
    def start(self):
        super().start()
        return self

    def run(self):
        debug(f"{self.__class__.__name__} started")
        while self.keep_running:
            self.event_loop()
        debug(f"{self.__class__.__name__} killed")
        return

    def event_loop(self):
        msg = receive(self.name)
        self.cb_anymsg(msg)
        event = msg.get('event')
        cb_name = f"cb_{event}"
        result = getattr(self, cb_name, self.cb_none)(msg)


    # def start(self):
    #     super().start()
    #     return self

    def kill(self):
        self.keep_running = False
    
    def cb_none(self, msg):
        debug(f"unknown callback triggered: {msg.get('event')}")
        print(f"unknown callback triggered: {msg}")
    
    def cb_anymsg(self, msg):
        pass

def post(bus_name, msg):
    b = bus_registry.bus(bus_name)
    b.put(msg)

def receive(bus_name):
    b = bus_registry.bus(bus_name)
    return b.get()

actor_registry = Actor_Registry()
bus_registry = Bus_Registry()
