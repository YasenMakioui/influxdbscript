# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import json
from influxdb import InfluxDBClient
from datetime import datetime


def data_payload():
    json_data = sys.argv[1]
    file = open(json_data, "r")
    content = file.read()
    payload = json.loads(content)
    for i in payload["data"]:
        i['time'] = datetime.now()
    file.close()
    return payload


def insert_data(payload):
    client = InfluxDBClient('localhost', 8086, 'admin', 'Password1', 'mydb')
    client.create_database('mydb')
    client.switch_database('mydb')
    client.write_points(payload)


def main():
    payload = data_payload()
    for i in payload['data']:
        insert_data([i])


if __name__ == '__main__':
    main()
