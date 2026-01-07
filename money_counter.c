#include <stdio.h>
#include <stdlib.h>

int main() {
    int numCoins, i;
    
    // Ask user how many coin/bill types
    printf("Enter the number of coin/bill types: ");
    if (scanf("%d", &numCoins) != 1 || numCoins <= 0) {
        printf("Invalid input!\n");
        return 1;
    }

    int *values = (int*)malloc(numCoins * sizeof(int));   // value of each type in cents
    int *counts = (int*)malloc(numCoins * sizeof(int));   // quantity of each type

    if (values == NULL || counts == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    // Input values (in cents) and counts
    for (i = 0; i < numCoins; i++) {
        printf("Enter value (in cents) of coin/bill type %d: ", i+1);
        scanf("%d", &values[i]);
        if (values[i] <= 0) {
            printf("Coin/bill value must be positive.\n");
            return 1;
        }

        printf("Enter number of coins/bills of this type: ");
        scanf("%d", &counts[i]);
        if (counts[i] < 0) {
            printf("Count cannot be negative.\n");
            return 1;
        }
    }

    // Compute total in cents
    int total_cents = 0;
    for (i = 0; i < numCoins; i++) {
        total_cents += values[i] * counts[i];
    }

    // Convert to "major" currency unit (dollars, euros, etc.) and minor (cents)
    int major = total_cents / 100;
    int minor = total_cents % 100;

    printf("Total amount: %d.%02d\n", major, minor);

    free(values);
    free(counts);

    return 0;
}