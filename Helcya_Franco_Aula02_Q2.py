v = float(input('Digite o preço do produto:'))
x = float(input('Digite a taxa:'))
t = float(input('Insira o tempo:'))
p = v + (v * (x / 100)) * t
print('O preço da prestação em atraso é de: ', p)
