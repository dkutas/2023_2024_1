package Konkurens.gy.gy3;

public class First {

    public static void main(String[] args) {
        // RunnableImplements1 run1 = new RunnableImplements1();
        // RunnableImplements2 run2 = new RunnableImplements2();

        Runnable task1 = () -> {

            for (int i = 0; i < 1000; i++) {
                if (i % 2 == 0) {
                    try {
                        Thread.sleep(200);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
                System.out.print(i + ",");
            }
        };

        Runnable task2 = () -> {

            for (int i = 0; i < 1000; i++) {
                if (i % 2 == 0) {
                    try {
                        Thread.sleep(200);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
                System.out.print(i + "," + -i + ", ");
            }
        };

        Thread thread1 = new Thread(task1);
        Thread thread2 = new Thread(task2);

        thread1.start();
        try {
            thread1.join();
            thread2.start();
            thread2.join();
            System.out.print(("Done"));
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

    }

}

// class RunnableImplements1 implements Runnable {

// public void run() {

// for (int i = 0; i < 1000; i++) {
// System.out.print(i + ",");
// }
// }

// }

// class RunnableImplements2 implements Runnable {

// public void run() {

// for (int i = 0; i < 1000; i++) {
// System.out.print(i + "," + -i + ", ");
// }
// }

// }
