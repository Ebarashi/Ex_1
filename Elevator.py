class Elevator:
    UP = 1
    LEVEL = 0
    DOWN = -1
    ERROR = -2

    def __init__(self, id, speed, min_floor, max_floor, close_time, open_time, start_time, stop_time):
        self.id = id
        self.speed = speed
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.close_time = close_time
        self.open_time = open_time
        self.start_time = start_time
        self.stop_time = stop_time
        self.curr_pos = 0
        self.state = 0  # state: UP=1 DOWN=-1 LEVEL=0
        self.curr_time = 0.0

    def _str_(self):
        return "" + str(self.id) + "," + str(self.speed) + "," + str(self.min_floor) + "," \
               + str(self.max_floor) + "," + str(self.close_time) + "," + str(self.open_time) \
               + "," + str(self.start_time) + "," + str(self.stop_time)

    def get_delay_time(self):
        return self.start_time + self.stop_time + self.open_time + self.close_time
