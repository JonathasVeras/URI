<?php
//Recebendo o valor que será dividido em notas e moedas:
$valor = (float)fgets(STDIN);

//Criando variável que é igual ao valor, mas que será modificada:
$valor_c = $valor;

//Crio uma array para guardar informações da nota, uma array com uma array para guardar informação de cada
//nota, tipo, a nota 100, contem o valor sem e possui, até então, 0 notas
$notas = array('100'=> array(100, 0), '50'=> array(50, 0), '20'=> array(20, 0), '10'=> array(10, 0), '5'=> array(5, 0), '2'=> array(2, 0), '1'=> array(1, 0));

//Percorro cada array na array notas aquele & é para passar por referência e eu poder modificar os valores
foreach ($notas as &$nota) 
{
    //Sempre que me referir a nota[0] será o valor da nota.
    //E sempre que me referir a nota[1] será a quantidade de notas.
    $nota[1] = (int)($valor_c / $nota[0]);
    $valor_c = $valor_c - $nota[1]*$nota[0];
}

// Convertendo o valor para não trabalhar com reais
$valor_c = round($valor_c * 100);

$moedas = array('0.50'=> array(50, 0), '0.25'=> array(25, 0), '0.10'=> array(10, 0), '0.05'=> array(05, 0), '0.01'=> array(01, 0));

//Percorro cada array na array moedas aquele & é para passar por referência e eu poder modificar os valores
foreach ($moedas as &$moeda) 
{
    //Sempre que me referir a moeda[0] será o valor da moeda.
    //E sempre que me referir a moeda[1] será a quantidade de moeda.
    $moeda[1] = (int)($valor_c / $moeda[0]);
    $valor_c = $valor_c - $moeda[1]*$moeda[0];
}

//Imprimindo como esse dinheiro ficaria diluido entre essas notas
echo "NOTAS:\n";
echo $notas['100'][1], " nota(s) de R$ 100.00\n";
echo $notas['50'][1], " nota(s) de R$ 50.00\n";
echo $notas['20'][1], " nota(s) de R$ 20.00\n";
echo $notas['10'][1], " nota(s) de R$ 10.00\n";
echo $notas['5'][1], " nota(s) de R$ 5.00\n";
echo $notas['2'][1], " nota(s) de R$ 2.00\n";

echo "MOEDAS:\n";
echo $notas['1'][1], " moeda(s) de R$ 1.00\n";
echo $moedas['0.50'][1], " moeda(s) de R$ 0.50\n";
echo $moedas['0.25'][1], " moeda(s) de R$ 0.25\n";
echo $moedas['0.10'][1], " moeda(s) de R$ 0.10\n";
echo $moedas['0.05'][1], " moeda(s) de R$ 0.05\n";
echo $moedas['0.01'][1], " moeda(s) de R$ 0.01\n";
?>