import java.util.Scanner;

public class priiii {
    public static void main(String[] args) {
        int row;
        int i, j;
        Scanner keyboard = new Scanner(System.in);
        row = keyboard.nextInt();
        for (i = 0; i < row; i++) {
            for (j = 0; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();

        }

    }
}
