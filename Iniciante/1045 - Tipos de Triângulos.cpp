#include <bits/stdc++.h>
using namespace std;

int main (){
  double A, B, C, maior, meio, ultimo;
  scanf("%lf %lf %lf", &A, &B, &C);

  maior = max(A, max(B, C));
  ultimo = min(A, min(B, C));
  meio = A+B+C-maior-ultimo;

  if (maior >= meio+ultimo){
    printf("NAO FORMA TRIANGULO\n");
  }
  else if  ( (maior*maior) == (meio*meio) + (ultimo*ultimo) ){
    printf("TRIANGULO RETANGULO\n");
  }
  else if ( (maior*maior) > ((meio*meio) + (ultimo*ultimo)) ) {
    printf("TRIANGULO OBTUSANGULO\n");
  }
  else if ( (maior*maior) < ((meio*meio) + (ultimo*ultimo)) ){
    printf("TRIANGULO ACUTANGULO\n");
  }
  if (maior == meio && meio == ultimo){
    printf("TRIANGULO EQUILATERO\n");
  }
  else if (maior==meio || meio==ultimo) {
    printf("TRIANGULO ISOSCELES\n");
  }
}
