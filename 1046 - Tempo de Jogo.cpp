#include <bits/stdc++.h>

int main()
{
    int H1, H2, D, contador;
    scanf("%d %d", &H1, &H2);
    if (H1>H2)
    {
        if(H1 < 24)
        {
            while(H1 < 24)
            {
                contador += 1;
                H1 += 1;
            }
            H2 = H2 + contador;
            D = H2;
            printf("O JOGO DUROU %d HORA(S)\n", D);
            return 0;
        }
        else
        {
            D = H2;
            printf("O JOGO DUROU %d HORA(S)\n", D);
            return 0;
        }
    }
    else if (H1 == H2)
    {
        printf("O JOGO DUROU %d HORA(S)\n", 24);
        return 0;
    }
    else
    {
        D = H2 - H1;
        printf("O JOGO DUROU %d HORA(S)\n", D);
    }
}
