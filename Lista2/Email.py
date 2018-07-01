print("Digite 0 para deixar as letras minúsculas e 1 para letras maiúsculas")

while True:
    comando = int(input("Comando: "))
    if (comando == 0 or comando == 1):
        break

print("\n\nCerto, agora digite sua mensagem")
mensagem = input("Mensagem: ")

if(comando):
    mensagem = mensagem.upper()
else:
    mensagem = mensagem.lower()

print("\n\n" + mensagem)
