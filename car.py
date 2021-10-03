from conductor import Conductor

class car:
    id = int;
    licencia = str;
    placa= str;
    capacidad= int;
    conductor = Conductor("","");
    pasajero = str;

    def __init__(self, licencia, conductor,pasajero, capacidad, placa):
        super().__init__();
        self.licencia = licencia;
        self.conductor = conductor;
        self.pasajero= pasajero;
        self.capacidad = capacidad;
        self.placa= placa;
        
   
