

class CallForElevator:
    def __init__(self, id, time, src, dest, state, allocate_elev):
        self.time = float(time)
        self.src = int(src)
        self.dest = int(dest)
        self.state = int(state)  # state GOING2SRC=1, GOING2DEST=2, DONE=3;
        self.allocate_elev = int(allocate_elev)
        self.id = id  # id is the index of Call at the List (parallel to csv file)

        if self.dest - self.src > 0:  # type UP=1, DOWN=-1;
            self.type = 1
        else:
            self.type = -1

    def get_distance(self):
        return abs(self.dest - self.src)

    def __str__(self):
        return "Elevator call" + "," + str(self.time) + "," + str(self.src) \
               + "," + str(self.dest) + "," + str(self.state) + "," + str(self.allocate_elev)

