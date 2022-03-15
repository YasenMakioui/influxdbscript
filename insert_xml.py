import json
import xml.etree.ElementTree as ET
from influxdb import InfluxDBClient
import sys

client = InfluxDBClient('localhost', 8086, 'admin', 'Password1', 'mydb')

def get_tag_names():
    xmlTree = ET.parse(sys.argv[1])
    element_list = []

    for elem in xmlTree.iter():
        if elem.tag in element_list:
            continue
        else:
            element_list.append(elem.tag)

    return element_list


def generate_dict(element_list):
    serial = 0
    root = element_list[0]
    measurement = element_list[1]
    fields = []
    for element in element_list:
        if serial == 0 or serial == 1:
            pass
        else:
            fields.append(element)
        serial += 1

    json_payload = []

    data = ET.parse(sys.argv[1])
    root = data.getroot()
    time = 0
    humitat = 0
    pressio = 0
    temperatura = 0
    for child in root:
        for items in child:
            if items.text == "None":
                items.text == 0.0
            ##control de si es float o int, usando string methods
            if items.tag == "time":
                time = 0 if items.text == 'None' else items.text
            elif items.tag == "humitat":
                humitat = 0 if items.text == 'None' else items.text
            elif items.tag == "pressio":
                pressio = 0 if items.text == 'None' else items.text
            elif items.tag == "temperatura":
                temperatura = 0 if items.text == 'None' else items.text

            json_payload.append({
                'measurement': 'sensor',
                'fields': {
                    'time': time,
                    'humitat': float(humitat),
                    'pressio': float(pressio),
                    'temperatura': float(temperatura)
                }
            })

    return json_payload


def insert_data(payload):
    for data in payload:
       client.write_points([data])




if __name__ == '__main__':
    element_list = get_tag_names()
    payload = generate_dict(element_list)
    insert_data(payload)

