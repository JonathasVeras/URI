#include <bits/stdc++.h>
#define pi 3.14159

int main()
{

	double A, B, C, hipotenusa,
	triangulo		,
	circulo  		,
	trapezio 		,
	quadrado 		,
	retangulo		;

	scanf("%lf %lf %lf", &A, &B, &C);

	triangulo = (A * C / 2.0);
	circulo = (pi * (C * C)) ;
	trapezio = (C*(A + B)/2.0) ;
	quadrado = (B * B)	 ;
	retangulo = (A * B)	 ;

	printf("TRIANGULO: %.3lf\nCIRCULO: %.3lf\nTRAPEZIO: %.3lf\nQUADRADO: %.3lf\nRETANGULO: %.3lf\n", triangulo, circulo, trapezio, quadrado, retangulo);
	return 0;
}
