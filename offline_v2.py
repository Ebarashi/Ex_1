from CSV_funcs import write_to_csv
from Elevator import Elevator
from CSV_funcs import read_from_csv
from Building import Building
from CallForElevator import CallForElevator


class Offline2:
    def __init__(self, csv: str, json: str):
        self.calls = read_from_csv(csv)
        self.b = Building(json)
        self.max_path = 0
        for call in self.calls:
            path = abs(call.dest - call.src)
            if path > self.max_path:
                self.max_path = path
        for call in self.calls:
            find_elev_to_call(self.b, self.calls[call], self.max_path)


def find_elev_to_call(building: Building, call: CallForElevator, road):
    area = int(road / (building.get_num_of_elev())) + 1
    curr_path = abs(call.dest - call.src)
    elev_id = int(curr_path / area)
    if elev_id >= building.get_num_of_elev():
        elev_id = building.get_num_of_elev() - 1
    call.allocate_elev = building.get_elev(building.get_elev(elev_id)).id
