from account import Account

class usuario(Account):
    def __init__(self, id, nombre, documento, contrasena, email):
       super().__init__(id, nombre, documento, contrasena, email);
