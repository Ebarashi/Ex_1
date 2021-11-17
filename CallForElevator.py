import csv


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

    def init(self, call) -> bool:
        """ True if the new call is between the src and dest of call """
        if self.get_type() == call.get_type() \
                and is_between(self.get_src(), self.get_dest(), call.get_src()) \
                and is_between(self.get_src(), self.get_dest(), call.get_dest()):
            return True
        return False


def is_between(src, dest, floor):
    """if floor between src and dest"""
    ans = False
    if dest <= floor <= src:
        ans = True
    elif dest >= floor >= src:
        ans = True
    return ans
