import csv
from CallForElevator import CallForElevator


def read_from_csv(csv_name: str):
    """ return list of Calls from csv file """
    calls_list = list()
    with open(csv_name, "r") as csv_file:
        calls_reader = csv.reader(csv_file)
        i = 0  # an id for a call
        for line in calls_reader:
            calls_list.append(
                CallForElevator(i, line[1], line[2], line[3], line[4], line[5]))
            i = i + 1
    return calls_list


def write_to_csv(calls_list, csv_name):
    """ write a new csv file, with updated allocated elev column """
    f = open(csv_name, "w")
    for i in range(0, len(calls_list) - 1):
        c = str(calls_list[i])
        f.write(c + "\n")
    c = str(calls_list[len(calls_list) - 1])
    f.write(c)
    f.close()


