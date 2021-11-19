from CSV_funcs import read_from_csv
from CSV_funcs import write_to_csv
from Building import Building
from Elevator import Elevator
from CallForElevator import CallForElevator
import sys


class OfflineV2:
    up = 1
    down = -1

    def __init__(self, csv: str, json: str):
        self.csv_name = csv
        self.json = json
        self.calls = read_from_csv(csv)
        self.b = Building(json)

    def allocate(self):
        # when we only have one elevator
        if len(self.b.dict_elev) < 2:
            self.special_allocate(self)
        sum_speed = 0
        for i in self.b.dict_elev.values():
            sum_speed += i.speed
        count_mult = 0
        while sum_speed % 1 != 0:
            sum_speed = sum_speed * 2
            count_mult = count_mult + 1
        count = 0
        for i in range(0, len(self.calls), sum_speed):
            for j in self.b.dict_elev.values():
                for k in range(count, i.speed * count_mult, 1):
                    self.calls[k].allocate_elev = j.id
                count = count + j.speed * count_mult

    def return_update_csv(self):
        new_csv_name = self.csv_name.strip(".csv") + "_out" + self.json.strip(".json") + ".csv"
        write_to_csv(self.calls, new_csv_name)
        return new_csv_name

    # in case we have only one elevator she should get all the calls
    def special_allocate(self):
        for i in self.calls:
            i.allocate_elev = 0


"""

if __name__ == "__main   __":
    x = Elevator(1, 1, 1, 1, 1, 1, 1, 1)
    print(x.max_floor)
    x.max_floor = 5;
    print(x.max_floor)

"""
