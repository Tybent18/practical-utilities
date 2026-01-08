#include <stdio.h>
#include <stdlib.h>

/* RGB extraction macros */
#define GET_RED(x)   (((x) >> 16) & 0xFF)
#define GET_GREEN(x) (((x) >> 8)  & 0xFF)
#define GET_BLUE(x)  ((x) & 0xFF)

int main(int argc, char *argv[]) {
    unsigned int value = 0;
    unsigned int red, green, blue;

    printf("Enter an RGB hex value (e.g. FF8040): ");
    if (scanf("%x", &value) != 1) {
        printf("Invalid input\n");
        return 1;
    }

    red   = GET_RED(value);
    green = GET_GREEN(value);
    blue  = GET_BLUE(value);

    printf(
        "Red:   %02X (%u)\n"
        "Green: %02X (%u)\n"
        "Blue:  %02X (%u)\n",
        red, red,
        green, green,
        blue, blue
    );

    /*
    --------------------------------------------------------------------
    Educational bit-manipulation example (cleaned-up version of original)
    --------------------------------------------------------------------

    unsigned int value = 0;
    unsigned int result = 0;
    int position;

    printf("Enter hex value: ");
    scanf("%x", &value);

    printf("Enter nibble position (1–4, from left): ");
    scanf("%d", &position);

    if (position >= 1 && position <= 4) {
        result = value & ~(0xF << ((4 - position) * 4));
        printf("The result is %08X\n", result);
    } else {
        printf("Invalid position\n");
    }
    */

    return 0;
}