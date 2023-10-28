// Ex5-4

#include <stdio.h>

// Function Prototype
int strend(char* s, char t);

int main() {
    // Test the function and print the result
    printf("%d", strend("asdfas", 's'));
    return 0;
}

// Function to check if the string s ends with the character t
int strend(char* s, char t) {
    // Check for null pointer
    if (s == NULL) {
        return 0;
    }

    // Check for empty string
    if (*s == '\0') {
        return 0;
    }

    // Find the end of the string
    while (*s) {
        s++;
    }

    // Check the last character
    return (*(s - 1) == t);
}
