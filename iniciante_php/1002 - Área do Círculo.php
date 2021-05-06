<?php

// Criando a função que retorna a área do círculo.
function area_circulo($raio)
{
    // Definindo uma constante chamada pi.
    define("pi", 3.14159);

    return pi * $raio* $raio;
}

// Atribuindo um input FLOAT a variável Raio.
$raio = (float)fgets(STDIN);

// Dando output da área do círculo usando a função.
// O number_format limita as casas decimáis, arredondando aonde deve.
// Esses argumentos '.' e '' são para definir os separadores.
echo "A=", number_format(area_circulo($raio), 4, '.', ''),"\n"; 
?>