#include <stdio.h>

unsigned int setbits(unsigned int x, int p, int n, unsigned int y);

int main() {
    unsigned int x, y;
    int p, n;

    printf("Enter x: ");
    scanf("%u", &x);

    printf("Enter p: ");
    scanf("%d", &p);

    printf("Enter n: ");
    scanf("%d", &n);

    printf("Enter y: ");
    scanf("%u", &y);

    printf("Result: %u\n", setbits(x, p, n, y));
    return 0;
}

unsigned int setbits(unsigned int x, int p, int n, unsigned int y) {
    return ((((x>>p)<<n) + (y & ~((~0)<<n)))<<(p-n)) + (x & ~(~0<<(p-n)));
}
