<?php
//Criação da função que soma dois elementos
function soma($num1, $num2)
{
    return $num1 + $num2;
}

//Entrada das variáveis A e B
$a = (int)fgets(STDIN);
$b = (int)fgets(STDIN);

//Saída do programa, onde é mostrado a soma de A e B pela função soma
echo "SOMA = " ,soma($a, $b), "\n";
?>