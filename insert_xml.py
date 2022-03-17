import pprint
import xml.etree.ElementTree as ET
import datetime
from influxdb import InfluxDBClient
import sys
import calendar

client = InfluxDBClient('localhost', 8086, 'admin', 'Password1', 'mydb')


def get_data_types():
    data_types = {
        "time": "",
        "humedad": "",
        "presion": "",
        "temperatura": ""
    }

    for data_set in client.query("SHOW FIELD KEYS"):
        for data_dict in data_set:
            if data_dict["fieldKey"] == "humedad":
                data_types["humedad"] = data_dict["fieldType"]
            elif data_dict["fieldKey"] == "presion":
                data_types["presion"] = data_dict["fieldType"]
            elif data_dict["fieldKey"] == "temperatura":
                data_types["temperatura"] = data_dict["fieldType"]
            elif data_dict["fieldKey"] == "time":
                data_types["time"] = data_dict["fieldType"]
    pprint.pprint(data_types)
    return data_types


def generate_dict():
    json_payload = []

    data = ET.parse(sys.argv[1])
    root = data.getroot()

    data_types = get_data_types()

    # asignar tipos de datos en caso de no haber recuperado nada de la medida
    if data_types["humedad"] == '' or data_types["presion"] or data_types["temperatura"]:
        data_types["humedad"] = "float"
        data_types["presion"] = "float"
        data_types["temperatura"] = "float"
    time = 0
    humedad = 0
    presion = 0
    temperatura = 0

    for child in root:

        dict_data = {
            'measurement': 'sensor',
            'time': time,
            'fields': {
                'humedad': humedad,
                'presion': presion,
                'temperatura': temperatura
            }
        }

        for items in child:

            # Comprobar si el campo es none y convertirlo en un dato int o float
            if items.text == "None":
                if items.tag == "humedad":
                    items.text = 0.0 if data_types["humedad"] == "float" else 0
                elif items.tag == "presion":
                    items.text = 0.0 if data_types["presion"] == "float" else 0
                elif items.tag == "temperatura":
                    items.text = 0.0 if data_types["temperatura"] == "float" else 0

            # Convertir tipo de dato acorde a los datos ya insertados en influx
            if items.tag == "time":
                time = datetime.datetime.now() if items.text == 'None' else items.text
            elif items.tag == "humedad":
                humedad = 0 if items.text == 'None' else items.text
                dict_data["fields"]["humedad"] = float(humedad) if data_types["humedad"] == "float" else int(humedad)
            elif items.tag == "presion":
                presion = 0 if items.text == 'None' else items.text
                dict_data["fields"]["presion"] = float(presion) if data_types["presion"] == "float" else int(presion)
            elif items.tag == "temperatura":
                temperatura = 0 if items.text == 'None' else items.text
                dict_data["fields"]["temperatura"] = float(temperatura) if data_types[
                                                                               "temperatura"] == "float" else int(
                    temperatura)

        json_payload.append(dict_data)

    return json_payload


def insert_data(payload):
    for data in payload:
        client.write_points([data])


if __name__ == '__main__':
    payload = generate_dict()
    insert_data(payload)
    pprint.pprint(payload)
