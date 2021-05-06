<?php
//Criando função do produto entre dois elementos
function produto($num1, $num2)
{
    return $num1 * $num2;
}


//Criando função da diferença entre dois elementos
function dif($num1, $num2)
{
    return $num1 - $num2;
}

//Lendo os elementos A, B, C e D:
$a = (int)fgets(STDIN);
$b = (int)fgets(STDIN);
$c = (int)fgets(STDIN);
$d = (int)fgets(STDIN);

//Output da diferença entre o produto de A com B e C com D:
echo "DIFERENCA = ", dif(produto($a, $b), produto($c, $d)), "\n";
?>