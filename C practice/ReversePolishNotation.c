// Ex 4.3

#include <stdio.h>
#include <stdlib.h> // for atof()

#define MAXOP 100  // max size of operand or operator
#define NUMBER '0' // signal that a number was found

int getop(char[]);
void push(double);
double pop(void);

int main()
{
    int type;
    double op1;
    double op2;
    char s[MAXOP];

    while ((type = getop(s)) != EOF) {
        switch (type) {
            case NUMBER:
                push(atof(s));
                break;
            case '+':
                push(pop() + pop());
                break;
            case '*':
                push(pop() * pop());
                break;
            case '-':
                op2 = pop();
                push(pop() - op2);
                break;
            case '%':
                op2 = pop();
                op1 = pop();
                if (op2 == 0.0){
                    printf("error: zero divisor\n");}
                else if ((int)op2 != op2 || (int)op1 != op1) { // Check if both are integers
                    printf("error: %% operator used on non-integer\n");}
                else
                    push((int)op1 % (int)op2);
                break;
            case '/':
                op2 = pop();
                if (op2 != 0.0)
                    push(pop() / op2);
                else
                    printf("error: zero divisor\n");
                break;
            case '\n':
                printf("\t%.8g\n", pop());
                break;
            default:
                printf("error: unknown command %s\n", s);
                break;
        }
    }
    return 0;
}

#define MAXVAL 100  // maximum depth of val stack

int sp = 0;         // next free stack position
double val[MAXVAL]; // value stack

// push: push f onto value stack
void push(double f)
{
    if (sp < MAXVAL)
        val[sp++] = f;
    else
        printf("error: stack full, can't push %g\n", f);
}

// pop: pop and return top value from stack
double pop(void)
{
    if (sp > 0)
        return val[--sp];
    else {
        printf("error: stack empty\n");
        return 0.0;
    }
}

#include <ctype.h>

int getch(void);
void ungetch(int);

// getop: get next character or numeric operand
int getop(char s[])
{
    int i, c;

    while ((s[0] = c = getch()) == ' ' || c == '\t')
        ;
    s[1] = '\0';
    i=0;
    if (c == '-') {
        // Look ahead to the next character.
        if (isdigit(s[++i] = c = getch()) || c == '.') {
            // It's a negative number.
            s[0] = '-';
        } else {
            ungetch(c);
            return '-';  // It's just a subtraction operator.
        }
    }

    if (!isdigit(c) && c != '.')
        return c;

    if (isdigit(c))     // collect integer part
        while (isdigit(s[++i] = c = getch()))
            ;
    if (c == '.')       // collect fraction part
        while (isdigit(s[++i] = c = getch()))
            ;
    s[i] = '\0';
    if (c != EOF)
        ungetch(c);
    return NUMBER;
}

char buf[100];  // buffer for ungetch
int bufp = 0;   // next free position in buf

int getch(void)  // get a (possibly pushed-back) character
{
    return (bufp > 0) ? buf[--bufp] : getchar();
}

void ungetch(int c)   // push character back on input
{
    if (bufp >= 100)
        printf("ungetch: too many characters\n");
    else
        buf[bufp++] = c;
}


/* Modularization and readability at the level of main function are highly important.
We could also use incremental development. */
