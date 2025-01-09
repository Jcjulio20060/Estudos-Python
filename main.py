# Simple Login

def simple_login(user, password):
    if user == "admin" and password == "admin":
        return True
    else:
        return False

user = str(input("Olá! Qual é seu usuário? "))
password = str(input("Qual é sua senha? "))
if simple_login(user, password):
    print("Login efetuado com sucesso!")