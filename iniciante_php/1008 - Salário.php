<?php
//Criando função que retorna o salário pela hora trabalhada
function salario($hora_trabalhada, $recebe_hora)
{
    return $hora_trabalhada * $recebe_hora;
}


//Recebendo o número do funcionário, quanto ele recebe por hora e quanto trabalhou.
$numero_func = (int)fgets(STDIN);
$money_por_hora = (float)fgets(STDIN);
$hora_trabalhada = (float)fgets(STDIN);

//Imprimindo o número do funcionário e o seu salário:
echo "NUMBER = $numero_func\nSALARY = U$ ", number_format(salario($hora_trabalhada, $money_por_hora), 2, '.', ''), "\n";
?>