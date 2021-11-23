from Usuario import Usuario

import mysql.connector
mysqlcnx = mysql.connector.connect(user='root', password='Daviddegea22.',
                              host='127.0.0.1',
                              database='pricar',
                              autocommit=True)
mysqlcursor=mysqlcnx.cursor()

class Conductor():
    #constructor
    def __init__(self):
        self.parada="parada"
        self.licencia="xxxxxx"
        self.horario="00:00"

    #setter de la parada
    def setParada(self):
        #la api es la que le pregunta a donde ir
        #retorna string
        pass

    #setter del horario
    def setHorario(self,horario):
        self.horario=horario

    #getter del horario
    def getHorario(self):
        return self.horario

    #numero de cupos
    def numeroCupos(self):
        # este metodo deberia llamar a la capacidad del vehiculo e ir calculando
        #retona entero
        pass
    def aceptarViaje(self,codigo,nombreP):
        mysqlcursor.execute(
            "update empleados set BuscandoViajeConductor=False where empleados.CodigoTrabajador=" + codigo + ";")
        mysqlcursor.execute(
            "update empleados set BuscandoViajePasajero=False where empleados.Nombre=" + nombreP + ";")
        mysqlcursor.execute(
            "update empleados set ViajeEncontradoP=True where empleados.Nombre=" + nombreP + ";")
        mysqlcursor.execute(
            "update empleados set ViajeEncontradoC=True where empleados.CodigoTrabajador=" + codigo + ";")

    def seleccionarParadaAc(self,codigo):
        mysqlcursor.execute("update empleados set BuscandoViajeConductor=True where empleados.CodigoTrabajador="+codigo+";")
        mysqlcursor.execute("update empleados set BuscandoViajePasajero=False where empleados.CodigoTrabajador=" + codigo + ";")
        mysqlcursor.execute("update empleados set ViajeEncontradoP=False where empleados.CodigoTrabajador=" + codigo + ";")
        mysqlcursor.execute("update empleados set ViajeEncontradoC=False where empleados.CodigoTrabajador=" + codigo + ";")
        print("ubicacion actual ")
    def seleccionarParadaPred(self,codigo,direccion):
        mysqlcursor.execute("update empleados set BuscandoViajeConductor=True where empleados.CodigoTrabajador=" + codigo + ";")
        mysqlcursor.execute("update empleados set BuscandoViajePasajero=False where empleados.CodigoTrabajador=" + codigo + ";")
        mysqlcursor.execute("update empleados set ViajeEncontradoP=False where empleados.CodigoTrabajador=" + codigo + ";")
        mysqlcursor.execute("update empleados set ViajeEncontradoC=False where empleados.CodigoTrabajador=" + codigo + ";")
        print("ubicacion predeterminada en la ubicacion: ", direccion)
#redundante lo de numero de cupos() y capacidad, no?
