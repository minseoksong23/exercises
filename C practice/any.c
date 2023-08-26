#include <stdio.h>
#include <string.h>
// Ex 2-5

void counter(char p[], char q[]);

int main(){
    char stra[100];
    char strb[100];
    
    scanf("%99s", stra);
    scanf("%99s", strb);
    counter(stra, strb);
    return 0;
}

void counter(char p[], char q[]) {
    int s;
    for (s=0;s<strlen(p);s++){
        for (int t=0;t<strlen(q);t++){
            if (p[s] == q[t]){
                printf("%d", s);
                return;
            }
        }
    } if (s==strlen(p)){
        printf("-1");
        return;
        }
}