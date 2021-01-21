#include <bits/stdc++.h>
#define number 40
int main()
{
	char name[number];
	double salarioFixo, dinheiroVendido, salarioReal;
	fgets(name, number, stdin);
	scanf("%lf %lf", &salarioFixo, &dinheiroVendido);
	salarioReal = (salarioFixo + (dinheiroVendido * 0.15));
	printf("TOTAL = R$ %.2lf\n", salarioReal);
	return 0;
}
