def convert(seconds): 
    min, sec = divmod(seconds, 60) 
    hour, min = divmod(min, 60) 
    return "%d:%02d:%02d" % (hour, min, sec) 
      
n = int(input('Insira um valor inteiro:'))
print(f'O valor convertido para horas, minutos e segundos é de:')
print(convert(n)) 