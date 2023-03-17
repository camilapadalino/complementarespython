pessoas = int(input("Insira o número de pessoas votantes:"))
validos = int(input("Insira o número total de votos válidos:"))
nulo = int(input("Insira o número de votos nulos:"))
branco = int(input("Insira o número de votos em branco:"))
validototal = validos/pessoas*100
nulototal = nulo/pessoas*100
brancototal = branco/pessoas*100
print(f"A porcentagem total é de: \n Votos Válidos: {validototal}% \n Votos Nulos: {nulototal}% \n Votos em Branco: {brancototal}%")
