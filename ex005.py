import random

def filtrar_pares(numeros):
    """Filtra os números pares recebidos da lista enviada

    Args:
        numeros (list): Lista de números.

    Returns:
        list: Lista de números pares.
    """

    if not isinstance(numeros, list):
        raise TypeError("A entrada deve ser uma lista.")

    def e_par(numero):
        return numero % 2 == 0

    pares = [numero for numero in numeros if e_par(numero)]
    return pares

# Criar uma lista com números aleatórios, incluindo negativos
lista = [random.randint(-100, 100) for _ in range(20)]

pares = filtrar_pares(lista)
print(pares)