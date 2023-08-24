#include <stdio.h>

/*
Exercise 1-22
*/

int main() {
    int c;
    int i = 0; // spacecount is initialized as 0
    int j = 0;
    char l[100];
    int n=10;
    int p=0;

    while ((c = getchar()) != EOF) {
        if (((i==n-2) && (c==' ')) || ((i>n-5) && (c=='\t'))){
            printf("%s\n", l);
            i=0;
            j=0;
        } else if (i<n-1 && c==' '){
            l[j] = '\0';
            printf("%s ", l);
            i = i+1;
            j = 0;
        } else if ((i < n-4) && (c == '\t')){
            l[j] = '\0';
            printf("%s\t", l);
            i = i+3;
            j = 0;
        } else {
            l[j]=c;
            if (i==n){
                printf("%s\n", l);
                i=0;
                j=0;
            } else{
                printf("%s", l);
                i=i+1;
                j=0;
            }
        }
    }
}
