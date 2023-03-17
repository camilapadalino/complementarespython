fabrica = float(input("Insira o valor do custo de fábrica do carro:"))
distribuidor = fabrica*0.28
impostos = fabrica*0.45
consumidor = fabrica+distribuidor+impostos
print(f"O custo ao consumidor vai ser de R${consumidor}")