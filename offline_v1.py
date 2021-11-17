from CSV_funcs import read_from_csv
from CSV_funcs import write_to_csv
from Building import Building
from Elevator import Elevator


class Offline:

    def __init__(self, cvs: str, json: str):
        self.calls = read_from_csv(cvs)
        self.b = Building(json)

if __name__ == "__main__":
    x=Elevator(1,1,1,1,1,1,1,1)
    print(x.max_floor)
    x.max_floor=5;
    print(x.max_floor)

