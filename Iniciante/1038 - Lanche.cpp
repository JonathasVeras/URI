/*
Algoritmo feito por Jonathas Veras, 03/2018, UFRN-CERES
*/

#include <bits/stdc++.h>

int main(){
    float c1 = 4.00, c2 = 4.50, c3 = 5.00, c4 = 2.00, c5 = 1.50;
    int codigo, quantidade;
    scanf("%d %d", &codigo, &quantidade);
    if(codigo == 1){
        printf("Total: R$ %.2f\n", (c1 * quantidade) );
    }
    else if(codigo == 2){
        printf("Total: R$ %.2f\n", (c2 * quantidade) );
    }
    else if(codigo == 3){
        printf("Total: R$ %.2f\n", (c3 * quantidade) );
    }
    else if(codigo == 4){
        printf("Total: R$ %.2f\n", (c4 * quantidade) );
    }
    else if(codigo == 5){
        printf("Total: R$ %.2f\n", (c5 * quantidade) );
    }
    return 0;
}
