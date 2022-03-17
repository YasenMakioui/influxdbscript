import xml.etree.cElementTree as ET
from influxdb import InfluxDBClient
import xml.dom.minidom

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
    archivo.write("prueba.xml")

    dom = xml.dom.minidom.parse("prueba.xml")
    pretty_xml_as_string = dom.toprettyxml()

    with open("prueba.xml", "w") as file:
        file.write(pretty_xml_as_string)


if __name__ == '__main__':
    get_xml()