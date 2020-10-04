from constants import debug
from actors import ActorThread, bus_registry, actor_registry, post, receive
from datetime import datetime
from config import trellis_addresses, H, W
# from adafruit_neotrellis.neotrellis import NeoTrellis
# from adafruit_neotrellis.multitrellis import MultiTrellis
from time import sleep
debug("Imported hardware connections")
AUTO_WRITE = False
BLANK = (0, 0, 0)

def coord_to_board(x,y):
    tX = int(x/4)
    tY = int(y/4)
    b = (4*tX) + tY
    return tX, tY, b

def boards_to_update(diffs):
    boards = set()
    for d in diffs:
        x,y,b = coord_to_board(d[0], d[1])
        boards.add((x,y))
    return list(boards)

class Trellis(ActorThread):
    """Physical Trellis hardware"""
    def __init__(self, i2c_bus):
        super().__init__()
        self.led_matrix = [[BLANK for x in range(W)] for y in range(H)]
        self.old_led_matrix = [[BLANK for x in range(W)] for y in range(H)]
        self.trelli = [[] for i in range(int(H/4))]  # [[],[]]
        debug("Creating Trelli")
        for x, slice in enumerate(trellis_addresses):
            for y, addr in enumerate(slice):
                # t = NeoTrellis(i2c_bus, False, addr=addr)
                # t.pixels.auto_write = False
                # self.trelli[x].append(t)
                # sleep(0.1)
                pass
        debug("Linking Trelli")
        # self.trellis = MultiTrellis(trelli)
        debug("Trelli linked")
        button_cb = self.make_button_cb()
        debug("Initializing Trelli inputs")
        for y in range(H):
            for x in range(W):
                pass
                # sleep(0.01)
                # self.trellis.activate_key(x, y, NeoTrellis.EDGE_RISING)
                # sleep(0.01)
                # self.trellis.activate_key(x, y, NeoTrellis.EDGE_FALLING)
                # self.trellis.set_callback(x, y, button_cb)
        debug("Inputs initialized")
        self.blank_screen()

    def make_button_cb(self):
        def button_cb(xcoord, ycoord, edge):
            # if edge == NeoTrellis.EDGE_RISING:
            #     post('button_grid', {'event': 'press', 'x': xcoord, 'y': H-1-ycoord})
            # elif edge == NeoTrellis.EDGE_FALLING:
            #     post('button_grid', {'event': 'release', 'x': xcoord, 'y': H-1-ycoord})
            return
        return button_cb

    def blank_screen(self):
        self.cb_draw_grid({'led_grid': [[BLANK for x in range(W)] for y in range(H)]})

    def cb_draw_grid(self, msg):
        led_grid = msg['led_grid']
        diffs = []
        for x in range(len(self.old_led_matrix)):
            for y in range(len(self.old_led_matrix[x])):
                if led_grid[x][y] != self.old_led_matrix[x][y]:
                    col = led_grid[x][y]
                    diffs.append((x, y, col))
                    self.old_led_matrix[x][y] = col 
                    # self.trellis.color(diff[0], diff[1], diff[2])
                    sleep(0.001)
                                    # for diff in diffs:
                                        # self.trellis.color(diff[0], diff[1], diff[2])
                                        # sleep(0.001)
        if len(diffs) > 0:
            if not AUTO_WRITE:
                for x, y in boards_to_update(diffs):
                    pass
                    # self.trellis._trelli[x][y].pixels.show()
                                        # for ts in self.trellis._trelli:
                                        #     for t in ts:
                                        #         t.pixels.show()
        return


    def cb_anymsg(self, msg):
        self.cb_draw_grid(msg)
        return

    # def event_loop(self):
    # Custom event loop because of call to draw?
    #     # [x][y] = (r,g,b)
    #     msg = receive('trellis')
    #     print(msg)
    #     event = msg.get('event')
    #     cb_name = f"cb_{event}"
    #     result = getattr(self, cb_name, self.post_to_ins)(msg)
        # self.cb_draw_grid(led_grid)


if __name__ == "__main__":
    t = Trellis(None)
