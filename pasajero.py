from account import Account

class Pasajero(Account):

    def __init__(self, id, ubicacionTiempoReal, nombre, contrasena, email, direccion, celular, usuario):
       super().__init__(id, ubicacionTiempoReal, nombre, contrasena, email, direccion, celular, usuario);
      
