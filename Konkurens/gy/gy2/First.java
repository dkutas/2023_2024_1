package Konkurens.gy.gy2;

public class First {
    public static void main(String[] args) {
        Thread firstThread = new SequenceProducer();
        firstThread.start();

        Runnable task = () -> {
            for (int i = 0; i < 30; i++) {
                System.out.print(i + "," + -i + ", ");
            }
        };
        try {
            firstThread.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        new Thread(task).start();

    }

}

class SequenceProducer extends Thread {
    @Override
    public void run() {
        for (int i = 0; i < 10000; i++) {
            System.out.print((i + ","));
        }
    }
}
