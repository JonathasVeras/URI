#include <bits/stdc++.h>
int main()
{
	int numero, hr;
	double salario, valorPorHora;
	scanf("%d %d %lf", &numero, &hr, &valorPorHora);
	salario = hr * valorPorHora;
	printf("NUMBER = %d\nSALARY = U$ %.2lf\n", numero, salario);
	return 0;
}
