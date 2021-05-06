<?php
// Função que checa se o valor está dentro do intervalo.
function is_in($valor, $init_intervavo = 10, $end_intervalo = 20)
{
    if($valor>=$init_intervavo && $valor <= $end_intervalo)
    {
        return True;
    }
    return False;
}

// Função que adciona no contador mais um sempre que o valor estiver no intervalo.
function count_in($valor)
{
    static $count;
    if (is_in($valor))
    {
        $count++;
    }
    return $count;
}


// Pegando o número de números a serem checados.
$tamanho_vetor = (int)(fgets(STDIN));
// Vetor que ficará os números
$vetor_inteiros = [];
// Variável que terá o número de elementos dentro.
$how_many_in = 0;

// Esse for serve para colocarmos os números inseridos pelo input no vetor.
// Também serve para iniciar nosso conjuto de funções que farão nossa conta.
for($i=0; $i<$tamanho_vetor; $i++)
{
    $vetor_inteiros[] = (int)(fgets(STDIN));
    $how_many_in = count_in($vetor_inteiros[$i]);
}
echo "$how_many_in in\n";
// Uso a função sizeof para pegar o tamanho do vetor e descontar os que não estão "dentro"
echo sizeof($vetor_inteiros) - $how_many_in, " out\n";
?>