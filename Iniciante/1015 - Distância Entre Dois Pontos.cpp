#include <bits/stdc++.h>

int main()
{

	float x1, y1, x2, y2, z, distancia;
	scanf("%f %f\n",&x1, &y1);
	scanf("%f %f\n",&x2, &y2);
	z=((x2 - x1) * (x2 - x1))+((y2 - y1) * (y2 - y1));
	distancia =sqrt(z);
	printf("%.4f\n", distancia);
	return 0;
}
