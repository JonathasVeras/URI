#include <bits/stdc++.h>

int main (){
    int A, B, C;
    scanf("%d %d %d", &A, &B, &C);
    if (A>B && B>C){
        printf("%d\n%d\n%d\n", C, B, A);
    }
    else if(B>A && A>C){
        printf("%d\n%d\n%d\n", C, A, B);
    }
    else if(C>A && A>B){
        printf("%d\n%d\n%d\n", B, A, C);
    }
    else if(C>B && B>A){
        printf("%d\n%d\n%d\n", A, B, C);
    }
    else if(A>C && C>B){
        printf("%d\n%d\n%d\n", B, C, A);
    }
    else if(B>C && C>A){
        printf("%d\n%d\n%d\n", A, C, B);
    }
    printf("\n%d\n%d\n%d\n", A, B, C);
}
