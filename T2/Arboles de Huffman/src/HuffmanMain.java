import java.util.Locale;
import java.util.Scanner;

public class HuffmanMain {

    public static void main(String[] args) {
        String texto;

        Scanner leer = new Scanner(System.in);
        System.out.print("Ingrese un texto -> ");
        texto = leer.nextLine();

        Huffman huff = new Huffman();
        huff.print(texto.toUpperCase(Locale.ROOT));
    }
}
