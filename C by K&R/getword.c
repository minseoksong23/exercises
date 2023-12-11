// Ex6.1; version of getword incorporating underscores and string constants

#include <stdio.h>
#include <ctype.h>

int getword(char *word, int lim)
{
    int c, getch(void);
    void ungetch(int);
    char *w = word;

    while (isspace(c = getch()))
        ;
    if (c != EOF)
        *w++ = c;
    
    if (c == '"') { // Starting a quoted word
        while (--lim > 0 && (c = getch()) != '"') {
            if (c == EOF || c == '\n') break; // End of file or line terminates the quote
            *w++ = c;
        }
        *w++ = '"';
        *w = '\0'; // Terminate the word
        return word[0]; // Return the first character
    } else {
        // Handle regular words
        if (!isalpha(c) && c != '_') {
            *w = '\0';
            return c;
        }
        for ( ; --lim > 0; w++)
            if (!isalnum(*w = getch()) && *w != '_') {
                ungetch(*w);
                break;
            }
        *w = '\0';
        return word[0];
    }
}

#define BUFSIZE 100

char buf[BUFSIZE];
int bufp = 0;

int getch(void)
{
    return (bufp > 0) ? buf[--bufp] : getchar();
}

void ungetch(int c)
{
    if (bufp >= BUFSIZE)
        printf("ungetch: too many characters\n");
    else
        buf[bufp++] = c;
}

int main() {
    char word[BUFSIZE];
    while (getword(word, BUFSIZE) != EOF) {
        printf("Got word: %s\n", word);
    }
    return 0;
}

