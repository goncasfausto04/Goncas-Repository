import sys

print("Olá Solzi, digite 'começar' para começar.")

while True:
    x = input("->")

    if x == 'começar':
        print("Olá Solzi Bem-Vinda ao teu jogo fofis")
        print("Este jogo é muito fixe e bacano e foi criado por mim (Gonçalo).")
        print("Queres continuar a jogar?")
        break
    else:
        print("Por favor, digite 'começar' para começar novamente")

while True:

    y = input("Sim ou não:")

    if y == "sim":
        print("Quanto me amas de 0-10?")
        break
    else:
        print("Cocó Gay")
        print("Tenta de novo:")

while True:
    z = input(":")

    if z == "10":
        print("OH YEAH!!!!!!")
        print("Obrigado por jogares e volte sempre!")
        sys.exit(1)

    elif z != 10:
        print("ERRADO")
        print("Tenta de novo!!")