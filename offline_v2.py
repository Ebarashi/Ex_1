from CSV_funcs import write_to_csv
from CSV_funcs import read_from_csv
from Building import Building
from CallForElevator import CallForElevator


class Offline2:
    def __init__(self, csv: str, json: str,out:str):
        self.calls = read_from_csv(csv)
        self.b = Building(json)
        self.csv_name = csv
        self.json = json
        self.out=out
        self.max_path = 0

        for i in self.calls:
            path = i.get_distance()

            if path > self.max_path:
                self.max_path = path
        for i in self.calls:
            find_elev_to_call(self.b, self.calls[i.id], self.max_path)
        write_to_csv(self.calls, self.out)


def find_elev_to_call(building: Building, call: CallForElevator, road):
    area = int(road / (building.get_num_of_elev())) + 1
    curr_path = abs(call.dest - call.src)
    elev_id = int(curr_path / area)
    if elev_id >= building.get_num_of_elev():
        elev_id = building.get_num_of_elev() - 1
    call.allocate_elev = building.dict_elev[elev_id].id

