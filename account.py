class Account:
    id = int;
    ubicacionTiempoReal= str;
    nombre = str;
    contrasena = str;
    email = str;
    direccion = str;
    celular = int;
    usuario = str; 

    def __init__(self, id,ubicacionTiempoReal, nombre, direccion, contrasena, email, celular, usuario):
        self.ubicacionTiempoReal=ubicacionTiempoReal;
        self.nombre = nombre;
        self.cireccion = direccion;
        self.contrasena = contrasena;
        self.email = email;
        self.id = id;
        self.celular = celular;
        self.usuario = usuario;
