/*
delta = -b²*4*a*c
bhaskara = -(b)+ou-sqrt(delta)/a*2
*/
#include <bits/stdc++.h>

int main(){
	double A, B, C;
	float delta, R1, R2;
	scanf("%lf %lf %lf", &A, &B, &C);
	delta = (B * B) - (4 * A * C);
	R1 = (-B + (sqrt (delta))) / (2 * A);
	R2 = (-B - (sqrt (delta))) / (2 * A);
	if (delta < 0 or A == 0){
		printf("Impossivel calcular\n");
	}
	else{
		printf("R1 = %.5lf\nR2 = %.5lf\n", R1, R2);
	}
	return 0;
}
