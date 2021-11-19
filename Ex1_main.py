import sys
from offline_v1 import OfflineV2

if __name__=="__main__":

    offline=OfflineV2("data/Calls/Calls_a.csv", "data/Building/B1.json")
    print(offline.return_update_csv())
