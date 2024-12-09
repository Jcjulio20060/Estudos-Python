def volume_paralelepipedo(comprimento, largura, altura):
    """Calcula o volume de um paralelepipedo
    Args:
        comprimento(float): O comprimento do paralelepipedo
        largura(float): A largura do paralelepipedo
        altura(float): A altura do paralelepipedo
    """
    if comprimento <= 0 or largura <= 0 or altura <= 0:
        raise ValueError("As dimensões devem ser positivas.")

    volume = comprimento * largura * altura
    return volume

x = float(input("Olá! Por favor! Digite o comprimento do paralelepipedo: "))
y = float(input("Agora digite a largura do paralelepipedo: "))
z = float(input("E por fim, a altura do paralelepipedo: "))
volume = volume_paralelepipedo(x, y, z)
print(f"O volume do paralelepipedo deu: {volume:.2f}")