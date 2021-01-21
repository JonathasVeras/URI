#include <bits/stdc++.h>
using namespace std;
int main()
{

	int A, B, C, Ab, maiorNumero;

	cin>>A>>B>>C;

	Ab = ((A + B + abs(A - B))/2 );
	maiorNumero = ((Ab + C + abs(Ab - C))/2);
	cout<<maiorNumero<<" eh o maior"<<endl;
	return 0;
}
