import datetime
import pprint
import time
import random

from influxdb import InfluxDBClient

client = InfluxDBClient('localhost', 8086, 'admin', 'Password1', 'mydb')


def start_sensor():
    while True:
        time.sleep(1)
        payload = {
            "measurement": "sensor",
            "time": datetime.datetime.now(),
            "fields": {
                "humedad": random.random() * 100,
                "presion": random.random() * 100,
                "temperatura": random.random() * 100

            }
        }
        client.write_points([payload])
        pprint.pprint(payload)


if __name__ == '__main__':
    start_sensor()
