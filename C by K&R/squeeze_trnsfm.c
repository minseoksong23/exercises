#include <stdio.h>
#include <string.h>
// Ex 2-4

void match_delete(char p[], char q[]);

int main(){
    char stra[100];
    char strb[100];
    
    scanf("%99s", stra);
    scanf("%99s", strb);
    match_delete(stra, strb);
    printf("%s\n", stra);
    return 0;
}

void match_delete(char p[], char q[]) {
    int i, j, k;
    int len = strlen(q);
    
    for (i = 0; p[i] != '\0'; ) {
        for (j = 0; j < len && p[i + j] == q[j]; j++);
        
        // If the substring is found
        if (j == len) {
            for (k = i; p[k + len] != '\0'; k++) {
                p[k] = p[k + len];
            }
            p[k] = '\0';
        } else {
            i++;
        }
    }
}