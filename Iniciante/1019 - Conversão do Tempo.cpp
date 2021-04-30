#include <bits/stdc++.h>
int main()
{

	int N, vN, horas, minutos, segundos;

	scanf ("%d", &N);
	vN = N;

	horas = vN / 3600;
	vN = vN - (horas * 3600);

	minutos = vN / 60;
	vN = vN -(minutos * 60);

	printf ("%d:%d:%d\n", horas, minutos, vN);
	return 0;
}
