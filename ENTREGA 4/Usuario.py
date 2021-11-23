import mysql.connector
mysqlcnx = mysql.connector.connect(user='root', password='Daviddegea22.',
                              host='127.0.0.1',
                              database='pricar',
                              autocommit=True)
mysqlcursor=mysqlcnx.cursor()
mysqlcursor.execute("select * from empleados;")
mysqlresultado = mysqlcursor.fetchall()
"""
Pensar en como esto se va a relacionar con la api, por lo tanto varios metodos y atributos van a llamar directamente a la api
Tambien, varios
"""

class Usuario():
    #metodo para ver perfil

    def __init__(self):
        self.code ="code"
        self.name="name"
        self.mail="mail"
        self.cellphone="cellphone"
        self.address="address"
        self.placa="placa"
        self.carcap=0
        self.points=0

    def setName(self,nombre):
        self.name=nombre
    def setCode(self,codigo):
        self.code=codigo
    def setMail(self,correo):
        self.mail=correo
    def setCellphone(self,celular):
        self.cellphone=celular
    def setAddres(self,direccion):
        #creo que esta es la de geolocalizacion de googlemaps
        self.address=direccion
    def setPlaca(self,placa):
        self.placa=placa
    def setCarcap(self,cap):
        self.carcap=cap
    def setPoints(self,puntos):
        self.points=puntos
    def getName(self):
        print(self.name)
        return self.name
    def getCode(self):
        print(self.code )
        return self.code
    def getMail(self):
        print(self.mail )
        return self.mail
    def getCellphone(self):
        print(self.cellphone )
        return self.cellphone
    def getAddress(self):
        print(self.address)
        return self.address
    def getPlaca(self):
        print(self.placa)
        return self.placa
    def getCarcap(self):
        print(self.carcap)
        return self.carcap
    def getPoints(self):
        print(self.points)
        return self.points
    def seePerfil(self,code):
        perfil=[self.code,self.name,self.mail,self.cellphone,self.address]
        print (perfil)
        return perfil

    def editName(self,nombre):
        self.name=nombre
        mysqlcursor.execute('update empleados set Nombre= "'+nombre+'" where empleados.CodigoTrabajador='+self.code)
    def editMail(self,email):
        self.mail=email
        mysqlcursor.execute('update empleados set Correo= "' + email + '" where empleados.CodigoTrabajador=' + self.code)
    def editAddress(self,direccion):
        self.address=direccion
        mysqlcursor.execute('update empleados set Direccion= "' + direccion + '" where empleados.CodigoTrabajador=' + self.code)
    def editCellphone(self,celular):
        self.cellphone=celular
        mysqlcursor.execute('update empleados set Celular= "' + celular + '" where empleados.CodigoTrabajador=' + self.code)
    def editPlaca(self,placa):
        self.placa=placa
        mysqlcursor.execute('update empleados set PlacaVehiculo= "' + placa + '" where empleados.CodigoTrabajador=' + self.code)
    def editCarcap(self,cap):
        self.carcap=cap
        mysqlcursor.execute('update empleados set CapacidadVehiculo= "' + cap + '" where empleados.CodigoTrabajador=' + self.code)

    #metodo para crear la ubicacion predeterminada(?)
    def parada(self):
        pass

    #beneficios que se obtiene al momento de llevar a las personas en el carro
    def beneficios(self):
        pass
    #metodo para cancelar ruta(por que este metodo esta aca, deberia estar en ruta
    def cancelarRuta(self):
        pass
