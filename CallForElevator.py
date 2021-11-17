import csv


class CallForElevator:
    def __init__(self, id: int, time: float, src: int, dest: int, state: int, allocate_elev: int):
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

    def get_start_time(self):
        return self.time

    def get_state(self):
        return self.state

    def set_state(self, new_state):
        if 0 < new_state <= 3:
            self.state = new_state

    def get_src(self):
        return self.src

    def get_dest(self):
        return self.dest

    def get_type(self):
        return self.type

    def get_allocate(self):
        return self.allocate_elev

    def set_allocated_to(self, elev_id):
        self.allocate_elev = elev_id

    def get_id(self):
        return int(self.id)

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


def read_from_csv(csv_name:  str):
    """ return list of Calls from csv file """
    calls_list = list()
    with open(csv_name, "r") as csv_file:
        calls_reader = csv.reader(csv_file)
        i = 0    # an id for a call
        for line in calls_reader:
            calls_list.append(
                CallForElevator(i, line[1], line[2], line[3], line[4], line[5]))
            i = i + 1
    return calls_list


def write_to_csv(calls_list, csv_name):
    """ write a new csv file, with updated allocated elev column """
    f = open(csv_name, "w")
    for i in range(0, len(calls_list) - 1):
        c = str(calls_list[i])
        f.write(c + "\n")
    c = str(calls_list[len(calls_list) - 1])
    f.write(c)
    f.close()
