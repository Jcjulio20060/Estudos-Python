import math

def area_circulo(raio):
    """Calcula a área de um círculo.

    Args:
        raio (float): O raio do círculo.

    Returns:
        float: A área do círculo.
    """
    if raio <= 0:
        raise ValueError("O raio deve ser um número positivo.")
    area = math.pi * math.pow(raio, 2)
    return area

raio = float(input("Olá! Por favor! Digite o valor do raio para descobrir a área: "))
try:
    result = area_circulo(raio)
    print("A área deste círculo é: {0:.2f}".format(result))
except ValueError as e:
    print(e)