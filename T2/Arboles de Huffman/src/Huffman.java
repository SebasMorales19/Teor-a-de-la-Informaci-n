import java.util.*;

public class Huffman {
    LinkedList<Nodo> nodePrint = new LinkedList<Nodo>();
    int elementos;

    // Construye un árbol binario basado en la cadena, s: la cadena fuente a codificar
    public Nodo constructTree(String s) {
        if (s == null || s.equals("")) {// s = nulo, es decir, dirección no asignada; s = "", espacio de dirección asignado, pero ocupando 0 bytes, los dos son diferentes
            return null;
        }
        // Calcula el número de apariciones de cada letra y ponla en el Mapa
        Map<Character, Integer> dataMap = new HashMap<Character, Integer>();// Dos tipos, hay un montón de elementos en la colección Map, cada elemento contiene un objeto clave y un objeto de valor
        // Es decir, cada carácter en la cadena correspondiente + su peso correspondiente
        elementos = s.length();
        for (int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);// Devuelve el carácter en el índice especificado
            if (dataMap.containsKey(c)) {// Determinar si se incluye el nombre de clave especificado
                int count = dataMap.get(c);// Devuelve el valor correspondiente al nombre de la clave (es decir, peso / veces)
                dataMap.put(c, count + 1);// Reescribe elementos existentes (pares clave-valor)
            } else {
                dataMap.put(c, 1);// Agregar elementos que no han aparecido en la colección Map (pares clave-valor)
            }
        }
        // Recorrer el DataMap, inicializar los nodos del árbol binario y colocar todos los nodos inicializados en nodeList y ordenarlos
        LinkedList<Nodo> nodeList = new LinkedList<Nodo>();
        for (Map.Entry<Character, Integer> entry : dataMap.entrySet()) {//Map.Entry contiene métodos getKey () y getValue (), formato fijo
            Character ch = entry.getKey();
            int cant = entry.getValue();
            int val = 0;
            double frec = (double)cant/elementos;
            Nodo tmp = new Nodo(ch,val,cant,null,null);
            nodePrint.add(new Nodo(ch,val,frec,null,null));
            nodeList.add(tmp);
        }
        // Ordenar la lista vinculada de nodos de almacenamiento para facilitar la combinación posterior
        Collections.sort(nodeList, new Comparator<Nodo>() {// Para ordenar los objetos de colección de cualquier tipo en su conjunto, pase la implementación de esta interfaz al método Collections.sort al ordenar
            public int compare(Nodo t1, Nodo t2) {
                return (int)(t1.frec-t2.frec);// De pequeño a grande (si el anverso menos el reverso, se ordena de pequeño a grande)
            }
        });
        // size == 1, lo que significa que la cadena contiene solo un tipo de letra
        if(nodeList.size()==1){
            Nodo t = nodeList.get(0);
            return new Nodo(null,0,nodeList.get(0).frec,t,null);
        }
        // Use nodos ordenados para construir un árbol binario, la raíz es el nodo raíz inicial
        Nodo root = null;
        while(nodeList.size()>0){
            // Debido a que nodeList ha sido ordenado al frente, entonces saque los dos primeros nodos directamente, su suma debe ser la más pequeña
            Nodo t1 = nodeList.removeFirst();// método removeFirst (), elimina y devuelve el primer elemento de esta lista.
            Nodo t2 = nodeList.removeFirst();
            // El valor del subárbol izquierdo es 0, y el valor del subárbol derecho es 1.
            t1.codif = 0;
            t2.codif = 1;
            // Combina los dos nodos extraídos
            if(nodeList.size()==0){
                // En este momento, todos los nodos se han fusionado y se devuelve el resultado.
                root = new Nodo(null,0,t1.frec+t2.frec,t1,t2);
            }else {
                // En este momento, todavía hay nodos que pueden fusionarse
                Nodo tmp = new Nodo(null,0,t1.frec+t2.frec,t1,t2);
                // Después de fusionar t1 y t2, debe agregar el nuevo nodo obtenido a la lista vinculada original y continuar fusionándose con otros nodos.
                // En este momento, se debe garantizar el orden de la lista vinculada original, y se debe ordenar
                if(tmp.frec>nodeList.getLast().frec){// Si el peso del nodo tmp es mayor que el peso del último nodo de la lista vinculada, conecte el nodo tmp al final de la lista vinculada
                    nodeList.addLast(tmp);
                }else {
                    for(int i=0;i<nodeList.size();i++){
                        double tmpFreq = tmp.frec;
                        if(tmpFreq<= nodeList.get(i).frec){// Recorre la lista vinculada para encontrar un nodo con un peso mayor que el peso del nodo tmp e inserta el nodo tmp en la posición del nodo
                            nodeList.add(i,tmp);
                            break;
                        }
                    }
                }
            }
        }
        // Regresar al nodo raíz del árbol binario establecido
        return root;
    }
    // Método de codificación, devuelve Object [], el tamaño es 2, Object [0] es la cadena codificada y Object [1] es la tabla de códigos correspondiente a la codificación
    public Object[] encode(String s){// Tipo de matriz
        Object[]res= new Object[2];
        Map<Character,String> encodeMap = new HashMap<Character, String>();
        Nodo tree = constructTree(s);
        findPath(tree, encodeMap, new StringBuilder());// Llamar al método findPath
        StringBuilder sb = new StringBuilder();
        for(int i=0;i<s.length();i++){
            String tmp = encodeMap.get(s.charAt(i));// Obtenga el valor, que es el código (número)
            sb.append(tmp);
        }
        res[0]=sb.toString();// La cadena binaria (número) cosida después de la codificación
        res[1] = encodeMap;// tabla de códigos
        return res;
    }
    // Atraviesa el árbol binario establecido para obtener la codificación de cada carácter
    private void findPath(Nodo root, Map<Character,String> encodeMap, StringBuilder path) {// StringBuilder es una secuencia de caracteres variable
        if (root.izq == null && root.der == null) {
            path.append(root.codif);// El método append de StringBuilder se usa para empalmar caracteres
            encodeMap.put(root.ch,path.substring(1));// Construir conjunto MAP (caracteres, codificación binaria), subString (1) es la cadena completa de longitud 1
            path.deleteCharAt(path.length() - 1);// Eliminar el último número binario de ruta
            return;
        }
        path.append(root.codif);
        if (root.izq != null) findPath(root.izq, encodeMap, path);
        if (root.der != null) findPath(root.der, encodeMap, path);
        path.deleteCharAt(path.length() - 1);// Debido a que el valor de la ruta después de completar el recorrido será 0/1 más que el estado teórico, por lo que debe eliminar el último (es decir, la longitud menos un número desconocido)
    }

    public void print(String s){
        Object[] encodeRes = encode(s);
        Map<Character,String> encodeMap = (Map<Character, String>)encodeRes[1];
        System.out.println("\nTabla de códigos:");

        int i = 0;
        for(Map.Entry<Character,String> e:encodeMap.entrySet()){
            nodePrint.get(i).codifArbol = e.getValue();
            i++;
        }

        double LMS = 0;
        System.out.println("Caracter\tFrecuencia\tCodificacion\tLongitud");
        for(i=0; i<nodePrint.size(); i++) {
            System.out.println(nodePrint.get(i).ch + "\t\t\t" + String.format("%.3f", nodePrint.get(i).frec) + "\t\t" + nodePrint.get(i).codifArbol + "\t\t\t\t" + nodePrint.get(i).codifArbol.length());
            LMS += nodePrint.get(i).frec * nodePrint.get(i).codifArbol.length();
        }
        System.out.println("\t\t\t\t\t\t\t\tLMS:\t" + LMS);
        System.out.println("\t\t\t\tRadio de Compresion:\t" + (8/LMS));

        char caracter;
        double frecuencia;
        double entropia;
        double sumaEntropia = 0;
        System.out.println("\nInformacion Mutua");
        System.out.println("Caracter\tFrecuencia\tInf.");
        for(i=0; i<nodePrint.size(); i++) {
            caracter = nodePrint.get(i).ch;
            frecuencia = nodePrint.get(i).frec;
            entropia = -frecuencia*(Math.log(frecuencia)/Math.log(2));
            sumaEntropia += entropia;
            System.out.println(caracter + "\t\t\t" + String.format("%.3f", frecuencia) + "\t\t" + String.format("%.5f", entropia));
        }
        System.out.println(" Entropia de entrada:\t" + String.format("%.5f", sumaEntropia));
    }

}

