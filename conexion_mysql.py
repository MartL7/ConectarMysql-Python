#Conectar Python a Base de Datos MySQL
#By: Geovas Or MartL7
#Importante instalar mysql-connector-python desde la consola con los siguientes comandos:
      #pip install mysql-connector-python

import mysql.connector

conexion = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = "root",
        password = "",
        db = "fichas"
    )

if conexion.is_connected():
        print("Estas Conectdo")
else:
        print("No Estas Conectado")

conexion.close()