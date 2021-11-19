from CSV_funcs import read_from_csv
from CSV_funcs import write_to_csv
from Building import Building


class Offline1:
    def __init__(self, csv: str, json: str, out: str):
        self.calls = read_from_csv(csv)
        self.b = Building(json)
        self.csv_name = csv
        self.json = json
        self.out = out

        allocate(self.b, self.calls)
        write_to_csv(self.calls, self.out)


def allocate(b: Building, calls: list):
    # when we only have one elevator
    if len(b.dict_elev) < 2:
        special_allocate(calls, b)
    sum_speed = 0
    for i in b.dict_elev.values():
        sum_speed = sum_speed + i.speed
    count_mult = 1
    while sum_speed % 1 != 0:
        sum_speed = sum_speed * 2
        count_mult = count_mult + 1
    count = 0
    for i in range(0, len(calls), int(sum_speed)):
        for j in b.dict_elev.values():
            for k in range(count, count+int(j.speed * count_mult), 1):
                try:
                    calls[k].allocate_elev = j.id
                except Exception as e:
                    pass
            count = count + int(j.speed * count_mult)

# in case we have only one elevator she should get all the calls
def special_allocate(calls: list, b: Building):
    for i in calls:
        i.allocate_elev = 0


"""

if __name__ == "__main   __":
    x = Elevator(1, 1, 1, 1, 1, 1, 1, 1)
    print(x.max_floor)
    x.max_floor = 5;
    print(x.max_floor)

"""
