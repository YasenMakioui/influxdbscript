# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import json
from influxdb import InfluxDBClient
from datetime import datetime

client = InfluxDBClient('localhost', 8086, 'admin', 'Password1', 'mydb')


def insert_data(data, mode):
    if mode == "unique":
        client.write_points([data])
    elif mode == "compound":
        for i in data['data']:
            client.write_points([i])


def get_data():
    with open(sys.argv[1]) as json_file:
        data = json.load(json_file)
        if "data" in data.keys():
            insert_data(data, "compound")
        else:
            insert_data(data, "unique")


def main():
    get_data()


if __name__ == '__main__':
    main()
