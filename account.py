class Account:
    id = int;
    nombre = str;
    contrasena = str;
    documento = str;
    email = str;

    def __init__(self, id, nombre, documento, contrasena, email):
        self.name = nombre;
        self.document = documento;
        self.password = contrasena;
        self.email = email;
        self.id = id;
