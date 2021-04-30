#include <bits/stdc++.h>

int main ()
{

	int ageInDay, ageInDayV, year, months, days;

	scanf ("%d", &ageInDay);
	ageInDayV = ageInDay;

	year = ageInDayV / 365;
	ageInDayV = ageInDayV - (year * 365);

	months = ageInDayV / 30;
	ageInDayV = ageInDayV - (months * 30);

	days = ageInDayV;

	printf ("%d ano(s)\n%d mes(es)\n%d dia(s)\n", year, months, days);
	return 0;
}
