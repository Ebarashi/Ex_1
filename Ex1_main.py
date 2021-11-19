import sys
from offline_v2 import Offline2

# the main assumes the input is legal
if __name__ == "__main__":
    func_input = sys.argv
    if len(func_input)>=3:
        building = func_input[1]
        call = func_input[2]
        out = func_input[3]
    else:
        building = input("enter a file name of building.json including path(ex: data/Building/B5.json): ")
        call = input("enter a file name of calls.csv including path(ex: data/Calls/Calls_d.csv): ")
        out = input("enter a file name for the result file(ex: out_b1_a.csv): ")
    Offline2(call, building, out)

