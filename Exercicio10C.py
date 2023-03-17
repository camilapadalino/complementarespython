totaldias = int(input("Insira o número total de dias trabalhados pelo encanador:"))
dia = 80
quantia = totaldias*dia
desconto = quantia*0.08
imposto = quantia - desconto
print(f'A quantia líquida do pagamento do encanador, junto com os 8% descontados é de R${imposto}')
