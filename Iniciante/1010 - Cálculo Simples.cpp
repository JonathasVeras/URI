#include <bits/stdc++.h>

int main()
{

	int codiP1, numeroP1, codiP2, numeroP2;
	float valorP1, valorP2, valoraPagar;

	scanf("%d %d %f\n", &codiP1, &numeroP1, &valorP1);
	scanf("%d %d %f\n", &codiP2, &numeroP2, &valorP2);
	valoraPagar = (valorP1 * numeroP1) + (valorP2 * numeroP2);
	printf("VALOR A PAGAR: R$ %.2f\n", valoraPagar);
	return 0;
}
