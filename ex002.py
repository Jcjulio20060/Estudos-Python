num = int(input("Olá! Por favor! Digite um número para saber sua tabuada: "))
for i in range(10):
    print("{0} x {1} = {2}".format(num, i + 1, num * (i + 1)))
print("\nFim da Tabuada!")