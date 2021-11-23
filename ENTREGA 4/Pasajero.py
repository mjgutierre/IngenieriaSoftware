from Usuario import Usuario
import mysql.connector
mysqlcnx = mysql.connector.connect(user='root', password='Daviddegea22.',
                              host='127.0.0.1',
                              database='pricar',
                              autocommit=True)
#conexion google maps
api_file = open("Interfaz/API/aappii.txt", "r")
api_key = api_file.read()
#conexion base de datos
mysqlcursor=mysqlcnx.cursor()
mysqlcursor.execute("select * from empleados;")
mysqlresultado = mysqlcursor.fetchall()
#el metodo encontrar carro deberia ser mejor un atributo

class Pasajero():
    #metoodo para pedir carro
    def pedirCarro(self):
        pass
    #metodo para seleccionar parada
    def seleccionarParadaAc(self,codigo):
        mysqlcursor.execute("update empleados set BuscandoViajePasajero=True where empleados.CodigoTrabajador="+codigo+";")
        mysqlcursor.execute("update empleados set BuscandoViajeConductor=False where empleados.CodigoTrabajador="+codigo+";")
        mysqlcursor.execute("update empleados set ViajeEncontradoP=False where empleados.CodigoTrabajador="+codigo+";")
        mysqlcursor.execute("update empleados set ViajeEncontradoC=False where empleados.CodigoTrabajador="+codigo+";")
    def seleccionarParadaPred(self,codigo,direccion):
        mysqlcursor.execute("update empleados set BuscandoViajePasajero=True where empleados.CodigoTrabajador="+codigo+";")
        mysqlcursor.execute("update empleados set BuscandoViajeConductor=False where empleados.CodigoTrabajador=" + codigo + ";")
        mysqlcursor.execute("update empleados set ViajeEncontradoP=False where empleados.CodigoTrabajador=" + codigo + ";")
        mysqlcursor.execute("update empleados set ViajeEncontradoC=False where empleados.CodigoTrabajador=" + codigo + ";")


    #metodo para ver acompañantes
    def verAcompanante(self):
        pass

