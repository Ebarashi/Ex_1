from Elevator import Elevator
import json


class Building:

    def __init__(self, json_b: str):
        self.dic_elev = {}
        self.max_floor = 0
        self.min_floor = 0
        self.read_from_json(json_b)

    def __str__(self) -> str:
        ans = F" minFloor: {self.min_floor}, maxFloor: {self.max_floor}"
        for i in range(0, len(self.dic_elev), 1):
            ans += F" Elev{i}: " + str(self.dic_elev[str(i)])
        return ans

    def __add__(self, other: Elevator):
        self.dic_elev['id'] = other
        return self.dic_elev

    def read_from_json(self, file_name: str) -> None:
        try:
            with open(file_name, "r") as f:
                data_dict = json.load(f)
                for k, v in data_dict.items():
                    if k == '_minFloor':
                        self.min_floor = v
                        continue
                    if k == '_maxFloor':
                        self.max_floor = v
                        continue
                    for j in v:
                        elev = Elevator(j['_id'], j['_speed'], j['_minFloor'], j['_maxFloor'], j['_closeTime'],
                                        j['_openTime'], j['_startTime'], j['_stopTime'])
                        self.dic_elev[j['_id']] = elev

        except IOError as e:
            print(e)

    def get_min_f(self) -> int:
        return self.min_floor

    def get_max_f(self) -> int:
        return self.max_floor

    def get_num_of_elev(self) -> int:
        return len(self.dic_elev)

    def get_elev(self, elev_id) -> Elevator:
        return self.dic_elev[elev_id]
