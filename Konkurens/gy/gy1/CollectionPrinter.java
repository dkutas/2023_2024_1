package Konkurens.gy.gy1;

import java.util.ArrayList;
import java.util.Arrays;

public class CollectionPrinter<T> {

    public static <T> void print(java.util.Collection<T> coll) {
        for (var elem : coll) {
            System.out.println(elem);
        }

    }

    public static void main(String[] args) {
        ArrayList<String> stringList = new ArrayList<>(Arrays.asList("Cordo", "Lista"));
        print(stringList);
    }
}