// K & R Ex 4-2

#include <ctype.h>
#include <stdio.h>
#include <math.h>
#define MAXLINE 100

int main(){
    double sum, atof(char []);
    char line[MAXLINE];
    int my_getline(char line[], int max);

    sum=0;
    while (my_getline(line, MAXLINE) > 0)
        printf("\t%g\n", sum += atof(line));
    return 0;
}

/* atof: convert string s to double */
double atof(char s[]) {
    double val, power;
    int i, sign, exp_sgn;
    
    for (i = 0; isspace(s[i]); i++);  /* skip white space */
    
    sign = (s[i] == '-') ? -1 : 1;
    
    if (s[i] == '+' || s[i] == '-')
        i++;

    for (val = 0.0; isdigit(s[i]); i++) {
        val = 10.0 * val + (s[i] - '0');
    }
    
    if (s[i] == '.') {
        i++;
    }

    for (power = 1.0; isdigit(s[i]); i++) {
        val = 10.0 * val + (s[i] - '0');
        power *= 10.0;
    }

    int t = 0;
    if (s[i] == 'e'){
        i = i + 1;
        exp_sgn = (s[i] == '-' ? -1 : 1);

        if (s[i] == '+' || s[i] == '-')
            i++;

        while(isdigit(s[i]) || s[i] == '0'){
            if (s[i] == '0'){
                i++;
                continue;
            }
            t = 10 * t + (s[i] - '0');
            i++;
        }
    }

    return sign * val / power * pow(10, exp_sgn * t);
}

int my_getline(char s[], int lim){
    int c, i;

    i=0;
    while (--lim >0 && (c=getchar()) != EOF && c != '\n')
        s[i++] = c;
    if (c == '\n')
        s[i++] = c;
    s[i] = '\0';
    return i;
}

