n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
n3 = float(input('Digite a terceira nota:'))
f = int(input('Digite a porcentagem de frequência às aulas:'))
media = (n1 + n2 + n3) / 3
if f>=75 and media>=7:
    print('Parabéns, você foi aprovado, sua média é de:', media)
else:
    print('Infelizmente você não foi aprovado.')
