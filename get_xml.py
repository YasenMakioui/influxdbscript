import xml.etree.cElementTree as ET
from influxdb import InfluxDBClient
import xml.dom.minidom
import sys

client = InfluxDBClient('localhost', 8086, 'admin', 'Password1', 'mydb')


def get_xml():
    result = client.query("select * from sensor")

    data = ET.Element("data")

    for set in result:
        for dict in set:
            doc = ET.SubElement(data, "mesura", nom="sensor")
            for field in dict:
                ET.SubElement(doc, field).text = str(dict[field])

    archivo = ET.ElementTree(data)

    file = ""

    if len(sys.argv) > 1:
        file = sys.argv[1]
    else:
        file = "sensor_data.xml"

    archivo.write(file)

    dom = xml.dom.minidom.parse(file)
    pretty_xml_as_string = dom.toprettyxml()

    with open(file, "w") as f:
        f.write(pretty_xml_as_string)


if __name__ == '__main__':
    get_xml()
