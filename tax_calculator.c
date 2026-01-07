#include <stdio.h>
#include <string.h>

typedef struct {
    char state[30];
    double taxRate;
} TaxInfo;

int main() {
    // Example state tax rates
    TaxInfo taxes[] = {
        {"CA", 0.0825},
        {"NY", 0.088},
        {"TX", 0.0625},
        {"FL", 0.06},
        {"WA", 0.065}
    };
    int numStates = sizeof(taxes)/sizeof(taxes[0]);

    double original_price, sale_percent, price_with_tax;
    double final_price;
    char state[30];
    double taxRate = 0;

    // Input
    printf("Enter state abbreviation (e.g., CA, NY): ");
    scanf("%s", state);
    printf("Enter original price of the item: ");
    scanf("%lf", &original_price);
    printf("Enter sale percentage (0 if none): ");
    scanf("%lf", &sale_percent);

    if (original_price < 0 || sale_percent < 0) {
        printf("Price and sale percentage must be non-negative.\n");
        return 1;
    }

    // Lookup tax rate
    int found = 0;
    for (int i = 0; i < numStates; i++) {
        if (strcmp(state, taxes[i].state) == 0) {
            taxRate = taxes[i].taxRate;
            found = 1;
            break;
        }
    }
    if (!found) {
        printf("State not found, using default tax rate 8%%.\n");
        taxRate = 0.08;
    }

    // Apply tax
    price_with_tax = original_price * (1 + taxRate);

    // Apply sale
    if (sale_percent != 0) {
        final_price = price_with_tax * (1 - sale_percent/100.0);
    } else {
        final_price = price_with_tax;
    }

    printf("The final price of your item is: $%.2lf\n", final_price);

    return 0;
}