#include <bits/stdc++.h>

int main()
{
	int velocidadeMedia, tempoDeViagem;
	float litros, qAndados;

	scanf("%d %d", &tempoDeViagem, &velocidadeMedia);
	qAndados = velocidadeMedia * tempoDeViagem;
	litros = qAndados / 12;
	printf ("%.3f\n", litros);
	return 0;
}
