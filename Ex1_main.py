import Building
from offline_v2 import Offline2
from CSV_funcs import write_to_csv

if __name__ == '__main__':
    Offline2("Calls_d", "B1.json")
    write_to_csv()
