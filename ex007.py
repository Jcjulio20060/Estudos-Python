import random

def imprimir(texto, cor):
    cores = {
        'Verde': '\033[32m',
        'Amarelo': '\033[33m',
        'Vermelho': '\033[31m',
        'Azul': '\033[34m'
    }
    print(f"{cores[cor]}{texto}\033[m")

secret_number = random.randint(1, 100)
tentativa = 0

while True:
    try:
        chute = int(input("Digite um número entre 1 e 100: "))
        tentativa += 1

        if chute < secret_number:
            imprimir("É mais!", "Amarelo")
        elif chute > secret_number:
            imprimir("É menos!", "Amarelo")
        else:
            imprimir(f"Parabéns! Você acertou! O número secréto é: {secret_number}", "Verde")
            imprimir(f"Você acertou em {tentativa} tentativas!", "Azul")
            break
    except ValueError:
        imprimir("Digite um número válido", "Vermelho")