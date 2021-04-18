"""
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.
"""
# Definindo os conjuntos

# Odens
onivoro = ('minhoca', 'homem', 'pomba')
carnivoro = ('aguia',)
herbivoro = ('vaca', 'lagarta')
hematofago = ('sanguessuga', 'pulga')

#geral
subfilo = {
'vertebrado':{
    'ave':{carnivoro, onivoro},
    'mamifero':{onivoro, herbivoro}
    },
'invertebrado':{
    'inseto':{hematofago, herbivoro},
    'anelideo':{hematofago, onivoro}}
}
#input do usuário
subfilo = input()
classe = input()
odrem = input()
print(subfilo[subfilo][classe][ordem])
