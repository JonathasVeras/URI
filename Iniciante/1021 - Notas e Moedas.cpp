#include <stdio.h>
#include "math.h"
int main ()
{
	double N, vN;
	int cem, cinquenta, vinte, dez, cinco, dois, umRealM, cinquentaM, vinteCincoM,
	dezM, cincoM, umCentavoM;

	scanf ("%lf", &N);
	vN = N;

	cem = vN / 100;
	vN = vN - (cem * 100);

	cinquenta = vN / 50;
	vN = vN - (cinquenta * 50);

	vinte = vN / 20;
	vN = vN - (vinte * 20);

	dez = vN / 10;
	vN = vN - (dez * 10);

	cinco = vN / 5;
	vN = vN - (cinco * 5);

	dois = vN / 2;
	vN = vN - (dois * 2);

	umRealM = vN / 1;
	vN = vN - (umRealM * 1);

	vN = vN * 100;

	cinquentaM = vN / 50;
	vN = vN - (cinquentaM * 50);

	vinteCincoM = vN / 25;
	vN = vN - (vinteCincoM * 25);

	dezM = vN / 10;
	vN = vN - (dezM * 10);

	cincoM = vN / 5;
	vN = vN - (cincoM * 5);

	umCentavoM = vN / 1;
	vN = vN - (umCentavoM * 1);

	printf ("NOTAS:\n");
	printf ("%d nota(s) de R$ 100.00\n", cem);
	printf ("%d nota(s) de R$ 50.00\n", cinquenta);
	printf ("%d nota(s) de R$ 20.00\n", vinte);
	printf ("%d nota(s) de R$ 10.00\n", dez);
	printf ("%d nota(s) de R$ 5.00\n", cinco);
	printf ("%d nota(s) de R$ 2.00\n", dois);
	printf ("MOEDAS:\n");
	printf ("%d moeda(s) de R$ 1.00\n", umRealM);
	printf ("%d moeda(s) de R$ 0.50\n", cinquentaM);
	printf ("%d moeda(s) de R$ 0.25\n", vinteCincoM);
	printf ("%d moeda(s) de R$ 0.10\n", dezM);
	printf ("%d moeda(s) de R$ 0.05\n", cincoM);
	printf ("%d moeda(s) de R$ 0.01\n", umCentavoM);
	return 0;
}
