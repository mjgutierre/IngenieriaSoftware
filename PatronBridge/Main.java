public class Main {
    public static void main (String [] args) {
    

    Rectangulo rectangulo = new Rectangulo (new DibujandoPunteado(),1,1,2,2);
    rectangulo.dibuja ();
    
    Circulo circulo = new Circulo (new DibujandoNormal(),2,2,3);
    circulo.dibuja();
    }
    }