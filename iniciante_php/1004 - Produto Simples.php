<?php
//Criação da função prod que faz o produto entre dois elementos
function prod($elemento1, $elemento2)
{
    return $elemento1 * $elemento2;
}
//Input dos elementos A e B
$a = (int)fgets(STDIN);
$b = (int)fgets(STDIN);

//Saída da multiplicação entre A e B
echo "PROD = ", prod($a, $b), "\n";
?>