import java.util.Scanner;

class pri {
    public static void main(String[] args) {
        int a;
        int n, fact = 1;
        Scanner keyboard = new Scanner(System.in);
        a = keyboard.nextInt();
        for (n = 1; n <= a; n++) {
            fact = fact * n;

        }
        System.out.println(fact);
    }

}