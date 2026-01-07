import java.util.Scanner;

public class Program {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a string: ");
        String text = scanner.nextLine();

        // Use StringBuilder for efficient reversal
        StringBuilder reversed = new StringBuilder(text).reverse();

        System.out.println("Reversed string: " + reversed);
    }
}