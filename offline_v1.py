from CSV_funcs import read_from_csv
from CSV_funcs import write_to_csv
from Building import Building


class Offline:

    def __init__(self, cvs: str, json: str):
        self.calls = read_from_csv(cvs)
        self.b = Building(json)

