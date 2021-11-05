public abstract class Forma{
    private Dibujo dibujo;

    public Forma(Dibujo d){
        dibujo = d; 
    }
    public abstract void dibuja();

    public void dibujaRectangulo(double x1, double y1, double x2, double y2){
        dibujo.dibujaRectangulo(x1, y1, x2,y2);
    }
    public void dibujaCirculo(double x,double y,double r){
        dibujo.dibujaCirculo(x, y, r);
    }
}

