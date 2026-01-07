import java.util.Scanner;

public class Program {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the amount owed: ");
        double amount = scanner.nextDouble();

        System.out.print("Enter the monthly interest rate (in %): ");
        double interestRate = scanner.nextDouble();

        System.out.print("Enter the number of months: ");
        int months = scanner.nextInt();

        for (int i = 0; i < months; i++) {
            amount -= (amount * interestRate / 100.0);
        }

        System.out.printf("Amount owed after %d months: %.2f%n", months, amount);
    }
}