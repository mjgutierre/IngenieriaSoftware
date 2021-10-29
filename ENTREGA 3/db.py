#base de datos conexion
import mysql.connector

conexion1=mysql.connector.connect(host="localhost",
                                  user="root",
                                  passwd="hola",
                                  database="empresa1")
cursor1=conexion1.cursor()
cursor1.execute("show tables")
for tabla in cursor1:
    print(tabla)


#insert en tablas
#sql="insert into vehiculo( licencia, capacidad,vehiculoPlaca) values (%s,%s,%s)"
#datos= ("122356727788" , 4 , "HHG432");
#cursor1.execute(sql, datos)
#datos=("1098829011123" , 2 , "JKO999");
#cursor1.execute(sql, datos)
#datos=("1413266687665" , 1 , "SSC311");
#cursor1.execute(sql, datos)

#consultas en base de datos
cursor1.execute("select licencia, capacidad, vehiculoPlaca from vehiculo")
for fila in cursor1:
    print(fila)

cursor1.execute("select nombre, vehiculoPlaca from trabajadores")
for fila in cursor1:
    print(fila)

cursor1.execute("SELECT trabajadores.nombre,trabajadores.vehiculoPlaca,trabajadores.codigoTrabajadores, trabajadores.celular FROM trabajadores INNER JOIN vehiculo ON vehiculo.vehiculoPlaca=trabajadores.vehiculoPlaca;")
for fila in cursor1:
    print(fila)


conexion1.commit()
conexion1.close()

