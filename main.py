import json
import sys
from influxdb import InfluxDBClient


client = InfluxDBClient('localhost', 8086, 'admin', 'Password1', 'mydb')


data = {}


def handler():
    if sys.argv[1] == "insert_json":
        print("1")
    elif sys.argv[1] == "insert_xml":
        print("2")
    elif sys.argv[1] == "get_json":
        print("3")
    elif sys.argv[1] == "get_xml":
        print("4")
    else:
        print("invalid operation")


def get_json():
    result = client.query("select * from sensor")
    for set in result:
        data["data"] = set
        json_data = json.dumps(data, indent=4)
        with open(sys.argv[2], 'w') as json_file:
            json_file.write(json_data)


def get_xml():
    print("get_xml")


def insert_json(data, mode):
    print("insert_json")


def insert_xml():
    print("insert_xml")