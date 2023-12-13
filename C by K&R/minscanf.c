#include <stdio.h>
#include <stdarg.h>

void minscanf(char *fmt, ...) {
    va_list ap;
    char *p;
    void *pval;

    va_start(ap, fmt);
    for (p = fmt; *p; p++) {
        if (*p != '%') {
            continue; // Skip non-format characters
        }

        pval = va_arg(ap, void*); // Get the next argument as a generic pointer

        switch (*++p) {
        case 'd': // Integer
            scanf("%d", (int*)pval);
            break;
        case 'f': // Floating-point number
            scanf("%lf", (double*)pval);
            break;
        case 's': // String
            scanf("%s", (char*)pval);
            break;
        // Handle other specifiers as needed
        default:
            // Handle unexpected format specifiers
            break;
        }
    }
    va_end(ap); // Clean up the va_list
}
