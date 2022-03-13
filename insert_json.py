import sys
import json
from influxdb import InfluxDBClient

client = InfluxDBClient('localhost', 8086, 'admin', 'Password1', 'mydb')


def insert_data(data, mode):
    if mode == "unique":
        client.write_points([data])
    elif mode == "compound":
        for records in data['data']:
            client.write_points([records])


def get_data():
    with open(sys.argv[1]) as json_file:
        data = json.load(json_file)
        if "data" in data.keys():
            insert_data(data, "compound")
        else:
            insert_data(data, "unique")


if __name__ == '__main__':
    get_data()
