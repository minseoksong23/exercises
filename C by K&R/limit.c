#include <stdio.h>
#include <limits.h>
#include <float.h>
// Exercise 2-1

int main() {
    // Signed types
    printf("Range of signed char: %d to %d\n", SCHAR_MIN, SCHAR_MAX);
    printf("Range of int: %d to %d\n", INT_MIN, INT_MAX);
    printf("Range of long: %ld to %ld\n", LONG_MIN, LONG_MAX);
    printf("Range of short: %d to %d\n", SHRT_MIN, SHRT_MAX);

    // Unsigned types
    printf("Range of unsigned char: 0 to %u\n", UCHAR_MAX);
    printf("Range of unsigned int: 0 to %u\n", UINT_MAX);
    printf("Range of unsigned long: 0 to %lu\n", ULONG_MAX);
    printf("Range of unsigned short: 0 to %u\n", USHRT_MAX);

    // Floating point types
    printf("Minimum double: %e\n", DBL_MIN);
    printf("Maximum double: %e\n", DBL_MAX);

    return 0;
}
