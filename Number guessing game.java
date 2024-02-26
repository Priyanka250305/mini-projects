import java.util.Scanner;
import java.util.Random;

public class priii {
    public static void main(String[] args) {
        Random rand = new Random();
        int c = rand.nextInt(100) + 1;
        int guesses = 0;
        Scanner keyboard = new Scanner(System.in);

        while (true) {
            int a;
            a = keyboard.nextInt();
            if (a > c) {
                System.out.println("too high");
                guesses++;
            } else if (a < c) {
                System.out.println("too low");
                guesses++;
            } else {
                System.out.println("congratulations!");
                guesses++;
                System.out.println("no. of guesses taken: " + guesses);
                break;
            }

        }

    }
}
