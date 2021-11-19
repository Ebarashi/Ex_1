from Elevator import Elevator
import json


class Building:

    def __init__(self, json_b: str):
        self.dict_elev = {}
        self.max_floor = 0
        self.min_floor = 0
        self.read_from_json(json_b)

    def __str__(self) -> str:
        ans = F" minFloor: {self.min_floor}, maxFloor: {self.max_floor}"
        for i in range(0, len(self.dict_elev), 1):
            ans += F" Elev {i}: " + str(self.dict_elev[i])
        return ans

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
                        self.dict_elev[j['_id']] = elev

        except IOError as e:
            print(e)

        #self.dict_elev = sorted(self.dict_elev, key=lambda x: x.time)

    def get_num_of_elev(self) -> int:
        return len(self.dict_elev)

    def get_elev(self, elev_id) -> Elevator:
        return self.dict_elev[elev_id]




