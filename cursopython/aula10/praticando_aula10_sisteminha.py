"""
Sisteminha basico
"""
print("=== Sistema básico de Login e senha ===")
print(f"Seu login é: Rogério123")
print(f"Sua senha é: ValdirValdir")
print()

login_salva = "Rogério123"
senha_salva = "ValdirValdir"

login = input("Login: ")
senha = input("Senha: ")

if login == login_salva and senha == senha_salva:
    print("Usuário logado com sucesso!")
else:
    print("Login ou Senha incorretos, tente novamente.")
