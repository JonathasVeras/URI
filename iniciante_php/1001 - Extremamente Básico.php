<?php
//Entrada dos dados, que são convertidos para inteiro.
$a = (int)fgets(STDIN);
$b = (int)fgets(STDIN);

// Operação com as variáveis A e B sendo atribuidas a variável X.
$x = $a + $b;

//Saída da variável X para o HTML
echo "X = $x\n";
?>