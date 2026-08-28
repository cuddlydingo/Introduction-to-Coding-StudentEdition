import java.util.Scanner;

public class SharedExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Name: ");
        String name = scanner.nextLine();

        for (int i = 1; i <= 3; i++) {
            System.out.println("Hello, " + name + "! Round " + i);
        }

        scanner.close();
    }
}
