#include <stdio.h>
#include <string.h>

typedef struct {
    char state[30];
    double taxRate;
} TaxInfo;

int main() {
    // Define some sample state tax rates
    TaxInfo taxes[] = {
        {"CA", 0.075},  // California 7.5%
        {"NY", 0.088},  // New York 8.8%
        {"TX", 0.0625}, // Texas 6.25%
        {"FL", 0.06},   // Florida 6%
        {"WA", 0.065}   // Washington 6.5%
    };
    int numStates = sizeof(taxes)/sizeof(taxes[0]);

    double price, total;
    char state[30];
    double taxRate = 0;

    printf("Enter the state abbreviation (e.g., CA, NY): ");
    scanf("%s", state);

    printf("Enter the price of the item: ");
    scanf("%lf", &price);

    if (price < 0) {
        printf("Price cannot be negative.\n");
        return 1;
    }

    // Look up the tax rate automatically
    int found = 0;
    for (int i = 0; i < numStates; i++) {
        if (strcmp(state, taxes[i].state) == 0) {
            taxRate = taxes[i].taxRate;
            found = 1;
            break;
        }
    }

    if (!found) {
        printf("State not found! Using default tax rate of 7%%.\n");
        taxRate = 0.07;
    }

    total = price * (1 + taxRate);

    printf("Total price including %.2lf%% tax in %s: $%.2lf\n", taxRate*100, state, total);

    return 0;
}