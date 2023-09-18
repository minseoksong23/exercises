//Ex 5-3

#include <stdio.h>

char* my_strcat(char *s, char *t);

int main(){
    char s[100]="abcd";
    char t[] = "efgh"; 
    printf("%s\n", my_strcat(s,t));
    return 0;
}

char* my_strcat(char *s, char *t){
    char *original = s;
    while (*s){
        s++;
    }
    while (*t){
        *s = *t;
        s = s+1;
        t = t+1;
    }
    *s = '\0';
    return original;
}