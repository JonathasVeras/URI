#include <bits/stdc++.h>

int main(){
  float A, B, C, P, M, m, h, areaTrapezio;


  scanf("%f %f %f", &A, &B, &C);
  P = A + B + C;
  areaTrapezio = ((A + B) * C) / 2.0;
  if (A < (B+C) && A > (B-C) ){
    printf("Perimetro = %.1f\n", P);
  }
  else{
    printf("Area = %.1f\n", areaTrapezio);
  }
}
