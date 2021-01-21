#include <bits/stdc++.h>
#define pi 3.14159

int main()
{

	double raio	,volume;

	scanf("%lf", &raio);
	volume = (4/3.0) * pi * (raio * raio * raio);
	printf("VOLUME = %.3f\n", volume);

	return 0;
}
