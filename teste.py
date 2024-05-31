print('=-=' * 20)
print('                   CALCULADORA SIMPLES  ')
print('=-=' * 20)
print('''ESCOLHA UMA DESSAS OPÇÕES
      [1]Adição
      [2]Subtração
      [3]Multiplicação
      [4]Divisão
      [5]Para fechar o programa''')
while True:
    num = int(input('Opção: '))
    if num == 1:
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite outro: '))
        nr = n1 + n2
        print(f'{n1} + {n2} = {nr}')
    elif num == 2:
        sub = int(input('Digite um numero: '))
        sub2 = int(input('Digite outro: '))
        subr = sub -  sub2
        print(f'{sub} - {sub2} = {subr}')
    elif num == 3:
        mult = int(input('Digite um numero: '))
        mult2 = int(input('Digite outro: '))
        multr = mult * mult2
        print(f'{mult} X {mult2} = {multr}')
    elif num == 4:
        div = float(input('Digite um numero: '))
        div2 = float(input('Digite outro: '))
        divr = div / div2
        print(f'{div} / {div2} = {divr:.1f}')
    elif num == 5:
        print('Volte sempre')
        break
    print('Tente novamente. ')
