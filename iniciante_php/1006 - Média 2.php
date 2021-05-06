<?php
//Criando a função de média das notas A, B e C:
function media($nota1, $nota2, $nota3)
{
    return (($nota1 * 2.0) + ($nota2 * 3.0) + ($nota3 * 5.0)) / 10.0;
}

//Input das 3 notas:
$nota_a = (float)fgets(STDIN);
$nota_b = (float)fgets(STDIN);
$nota_c = (float)fgets(STDIN);

//Saída da média das notas:
//Lembrando que o number_format formada as casas decimáis dos números
//---Nesse caso ficará com uma casa após a virgula, sendo separada pelo '.'
echo "MEDIA = ", number_format(media($nota_a, $nota_b, $nota_c), 1, '.', ''), "\n";
?>