
quantpao = int(input("Insira a quantidade de pães vendidos no dia:"))
quantbroa = int(input("Insira a quantidade de broas vendidas no dia:"))
pao = 0.38*quantpao
broa = 4.50*quantbroa
arrecadado = pao + broa
poupanca = arrecadado*0.10
total = arrecadado - poupanca
print(f'A quantidade de pães vendidos foram de: {quantpao} \n A quantidade de broas vendidas foram de: {quantbroa} \n O valor que eles terão de guardar para a poupança é de R${poupanca} \n E o total arrecadado descontados a porcentagem da poupança é de R${total}')
