#include <stdio.h>
// Exercise 1.23

int main() {
    int p=0; // if inside quotation marks
    int q=0; // if after /
    int r=0; // if inside a single-line comment
    int s=0; // if * is read after /*
    int c;
    char list[100]; // Buffer to hold characters within a comment
    int k=0;        // Index for list

    while ((c = getchar()) != EOF) {
        if (p == 0 && c != '"') {
            // not in quotation marks
            if (q == 1 && s == 1) { // if / is read then we complete the comment
                if (c == '/') {
                    q = 0;
                    s = 0;
                    k = 0;
                } else {
                    s = 0;
                    list[k++] = c;
                }
            } else if (q == 1 && s == 0) { // inside /* comment
                if (c == '*') {
                    s = 1;
                    list[k++] = c;
                } else {
                    list[k++] = c;
                }
            } else if ((q == 0 && s == 0) && r == 0) { // not in comments
                if (c == '/') {
                    s = 1;
                    list[k++] = c;
                } else {
                    printf("%c", c);
                }
            } else if (q == 0 && s == 1) { // / is read but not enter into comment yet
                if (c != '*' && c != '/') {
                    s = 0;
                    k = 0;
                } else if (c == '*') {
                    s = 0;
                    q = 1;
                    list[k++] = c;
                } else if (c == '/') {
                    s = 0;
                    r = 1;
                    list[k++] = c;
                }
            } else if (r == 1) { // inside a single comment mode
                if (c == '\n') {
                    printf("\n");
                    r = 0;
                }
            }
        } else if (p == 0 && c == '"') { // inside quotation marks
            printf("\"");
            p = 1;
        } else if (p == 1 && c != '"') { // did not exit the quotation marks
            printf("%c", c);
        } else if (p == 1 && c == '"') { // exit the quotation marks
            printf("\"");
            p = 0;
        }
    }

    if (q == 1) {
        list[k] = '\0';
        printf("%s", list);
    }

    return 0;
}
