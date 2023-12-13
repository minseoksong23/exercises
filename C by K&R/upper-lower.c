#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(int argc, char *argv[]){
    int c;
    // Check if the program name (in argv[0]) includes 'lower' to convert to lowercase
    // or 'upper' to convert to uppercase. The strstr function checks for a substring.
    if (strstr(argv[0], "lower")) {
        while ((c = getchar()) != EOF)
            putchar(tolower(c));
    } else if (strstr(argv[0], "upper")) {
        while ((c = getchar()) != EOF)
            putchar(toupper(c));
    } else {
        // If the program name does not include 'lower' or 'upper', print an error message.
        fprintf(stderr, "Error: Program name must include 'lower' or 'upper'.\n");
        return 1; // Return a non-zero value to indicate error.
    }
    return 0; // Return zero to indicate success.
}
