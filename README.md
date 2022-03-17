# influxdbscript

## Como se usa

### insert_json

Ejecutar el script y pasar como parametro el nombre del archivo que contiene los datos
```bash
$ python3 insert_json.py data.json
```
Se puede insertar en dos formatos, ambos se pueden ver en los .json de ejemplo "data.json" y uniquedata.json

### insert_xml

Ejecutar el script y pasar como parametro el nombre del archivo que contiene los datos
```bash
$ python3 insert_xml.py data.xml
```

### get_json
Ejecutar el script y pasar como parametro el nombre donde se guardaran los datos. En caso de no especificarse se guardan en sensor_data.json
```bash
$ python3 get_json.py prueba.json
```
o
```bash
$ python3 get_json.py
```

### get_xml
Ejecutar el script y pasar como parametro el nombre donde se guardan los datos. En caso de no especificarse se guardan en sensor_data.xml
```bash
$ python3 get_xml.py prueba.xml
```
o
```bash
$ python3 get_xml.py
```