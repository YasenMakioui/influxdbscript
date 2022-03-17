import json
import sys

from influxdb import InfluxDBClient

client = InfluxDBClient('localhost', 8086, 'admin', 'Password1', 'mydb')

data = {

}


def get_data():
    result = client.query("select * from sensor")
    for data_set in result:
        data["data"] = data_set
        json_data = json.dumps(data, indent=4)

        if len(sys.argv) > 1:
            file = sys.argv[1]
        else:
            file = "sensor_data.json"
        with open(file, 'w') as json_file:
            json_file.write(json_data)


if __name__ == '__main__':
    get_data()
