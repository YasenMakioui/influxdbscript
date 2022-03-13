import sys
import json
from influxdb import InfluxDBClient
from datetime import datetime

json_payload = [{
    "measurement": "sensor",
    "fields": {
        "pressio": 1.5,
        "humitat": 440.2,
    }
    },
    {
        "measurement": "sensor",
        "fields": {
            "pressio": 444.6,
            "humitat": 4402.2,
        }
    },
    {
        "measurement": "sensor",
        "fields": {
            "pressio": 1.3,
            "humitat": 44440.2,
        }
    }

]

client = InfluxDBClient('localhost', 8086, 'admin', 'Password1', 'mydb')
client.switch_database('mydb')
client.write_points(json_payload)
