import mysql.conector
from mysql.conector import errorcode

print("conectando...")
try:
    conn = mysql.conector.conector.connect(
           host='Davidcondori.mysql.pythonanywhere-service.com',
           user='Davidcondori',
           password='mysqlroot'
           )
except mysql.connector.Error as err:
       if err.erno == errorcode.ER_ACCESS_DENIED_ERROR:
              print('Existe un error en el nombre de usuario o en la clave')
       else:
           print(err)

cursor = conn.cursor()

cursor.excute("DROP DATABASE IF EXISTS `Davidcondori$pedidoentrega`;")

cursor.excute("USE `Davidcondori$pedidoentrega`;")

#creando las tablas

TABLES = {}

TABLES['productos'] = ('''
      CREATE TABLE `productos`(
      `id` int(11) NOT NULL AUTO_INCREMENT,