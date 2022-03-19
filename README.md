# influxdbscript
## Paquetes requeridos
````bash
$ pip install influxdb
````
## Iniciar el entorno con docker
````bash
$ docker-compose up
````
Comprobamos si se esta ejecutando
````bash
$ docker ps
````
Los datos de usuario, contraseña, etc... estan en archivo docker-compose.yml
### En otros entornos

Aplicar cambios de usuario, contraseña y base de datos en los scripts 
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
$ python3 get_xml.py data.xml
```
o
```bash
$ python3 get_xml.py
```
## Pruebas
Para simular un sensor y comenzar a usar los scripts simplemente hay que ejecutar sensor.py
````bash
$ python3 sensor.py
````
Una vez iniciado el script, este enviara datos cada 1s. Se puede cambiar el valor para simular una cantidad de datos mas alta
