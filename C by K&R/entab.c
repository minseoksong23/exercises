#define TAB 3
#include <stdio.h>

/*
Exercise 1-21
*/

int main() {
    int c;
    int i = 0; // spacecount is initialized as 0

    while ((c = getchar()) != EOF) {
        if (c != ' ' && i == 0) {
            printf("%c", c);
        } else if (c == ' ') {
            if (i < 2) {
                i += 1;
            } else if (i == 2) {
                printf("\t");
                i = 0;
            }
        } else {
            if (c == '\t') {
                printf("\t");
            } else {
                for (int j = 0; j < i; j += 1) {
                    printf(" ");
                }
                i = 0;
                printf("%c", c);
            }
        }
    }

    while (i > 0) {
        printf(" ");
        i--;
    }

    return 0;
}
