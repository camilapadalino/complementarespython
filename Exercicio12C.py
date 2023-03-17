comprimento = int(input("Insira o tamanho do comprimento da largura: "))
largura = int(input("Insira o número da largura da cozinha:"))
altura = int(input("Insira o número da altura da cozinha:"))
azuleijo = 1.5
compxazul = comprimento * azuleijo
largxazul = largura * azuleijo
altxazul = altura * azuleijo
totalazul = compxazul + largxazul + altxazul
print (f'O número total de azuleijos vai ser de: {totalazul}')