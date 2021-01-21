/*
###Algoritmo feito por Jonathas Veras, 02/03/2018
###Aluno da instituição UFRN-CERES
*/
#include <bits/stdc++.h>

int main(){
    float n1, n2, n3, n4, notaExame, mediaFinal;
    int p1=2, p2=3, p3=4, p4=1;
		float somaDosPesos=p1+p2+p3+p4;

    scanf("%f %f %f %f", &n1, &n2, &n3, &n4);
    float media = ((n1*p1)+(n2*p2)+(n3*p3)+(n4*p4)) / somaDosPesos;
    if(media >= 7.0){
        printf("Media: %.1f\nAluno aprovado.\n",media);
    }
    else if(media < 5){
        printf("Media: %.1f\nAluno reprovado.\n",media);
    }
    else if(5<= media <=6.9){
    	printf("Media: %.1f\nAluno em exame.\n", media);
			scanf("%f", &notaExame);
			mediaFinal = (notaExame + media) / 2 ;
			printf("Nota do exame: %.1f\n", notaExame);
				if(mediaFinal>= 5){
					printf("Aluno aprovado.\nMedia final: %.1f\n", mediaFinal);
	}
				else{
					printf("Aluno reprovado. \nMedia final: %.1f\n", mediaFinal);
				}
    }
    return 0;
}
