package Konkurens.gy.gy2;

public class Second {
    public static void main(String[] args) {
        String tomb[] = new String[] { "Elso", "Masodik", "Harmadik", "Negyedik", "Otodik" };
        for (var elem : tomb) {
            Runnable task = () -> {
                System.out.print(elem);
            };
            new Thread(task).start();
        }
    }
}