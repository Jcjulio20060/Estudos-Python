# Escreva uma função que me diga se um número é par ou ímpar

def par_impar(n):
    if type(n) != int:
        print("Não é um número inteiro!")
    elif n % 2 == 0:
        return True
    else:
        return False

number = input('Digite um número: ')
if par_impar(number):
    print('O número é par')
else:
    print('Erro!')