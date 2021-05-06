<?php
//Fazendo a função que calcula a média do aluno
function media($nota1, $nota2)
{
    //Esses valores "3.5" e "7.5" são os pesos
    return (($nota1 * 3.5) + ($nota2 * 7.5)) / 11;
}


//Input da nota1 e nota2 em FLOAT.
$nota_a = (float)fgets(STDIN);
$nota_b = (float)fgets(STDIN);

//Imprimindo a média:
echo "MEDIA = ", number_format(media($nota_a, $nota_b), 5, '.', ''), "\n";
?>