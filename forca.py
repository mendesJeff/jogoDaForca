secret = "gabriel".upper()
digitadas = []
corretas = []
chances = 10

while True:

    if chances == 0:
        print(f"Você perdeu. Tente novamente!")
        break

    letter = input("Digite uma letra: ").upper()

    if len(letter) > 1 or letter.isdigit() or letter == "" or letter == " ":
        print("Você só pode escolher 1 letra.")
        continue

    # digitadas.append(letter)

    if letter in digitadas:
        print(f"A letra '{letter}' já foi digitado.")
    elif letter in secret:
        print(f"A letra digitada '{letter}' faz parte da palavra secreta.")
        print()
        digitadas.append(letter)
    else:
        print(f"A letra '{letter} NÃO faz parte da palavra secreta.")
        print()
        digitadas.append(letter)
        chances -= 1

    print(f"Você ainda tem: {chances} chance(s).")
    print()
    print("Já foram digitadas as letras:")
    print(digitadas)
    print()

    secret_temp = ""
    for secret_letter in secret:
        if secret_letter in digitadas:
            secret_temp += secret_letter
        else:
            secret_temp += "-"

    if secret_temp == secret:
        print(f"Você ganhou, a palavra era {secret_temp}")
        break
    else:
        print(f"A palavra secreta é: {secret_temp}")
