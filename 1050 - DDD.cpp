#include <iostream>
using namespace std;
#define MAX_STRING 100
#define MAX 100

int check_ddd(int ddd[MAX], int tamanho, int x);

int main()
{
    char nomes_cidades[8][MAX_STRING]= {"Brasilia", "Salvador", "Sao Paulo", "Rio de Janeiro", "Juiz de Fora", "Campinas", "Vitoria", "Belo Horizonte"};
    int ddd[8] = {61, 71, 11, 21, 32, 19, 27, 31};
    int x;
    cin >> x;
    if(check_ddd(ddd, 8, x) != 8)
    {
      cout << nomes_cidades[check_ddd(ddd, 8, x)] << endl;
    }
    else
    {
      cout <<"DDD nao cadastrado" << endl;
    }

    return 0;
}


int check_ddd(int ddd[MAX], int tamanho, int x)
{
  for (size_t i = 0; i < tamanho; i++)
  {
    if(x == ddd[i])
    {
      return i;
    }
  }
  return tamanho;
}
