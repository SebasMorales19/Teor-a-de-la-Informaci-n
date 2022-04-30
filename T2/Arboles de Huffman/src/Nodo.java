public class Nodo {
    Character ch;   // Caractér
    int codif;    // 0 si va a la izquierda y 1 si va a la derecha
    double frec;   // Frecuencia
    Nodo izq;
    Nodo der;
    String codifArbol;

    public Nodo() {}

    public Nodo(Character ch, int codif, double frec, Nodo izq, Nodo der) {
        this.ch = ch;
        this.codif = codif;
        this.frec = frec;
        this.izq = izq;
        this.der = der;
        this.codifArbol = "";
    }
}
