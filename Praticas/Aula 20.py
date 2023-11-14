#exercicio 2

while True:
    inputnuM = input("Input a number:")
    if inputnuM.isdigit():
        if int(inputnuM) > 0 :
            print("Good!")
            break
        else:
            print("Try again!")
    else:
        print("Try again!")

#exercicio 3

while True:
    inputnumFI = input("Input a number:")
    if inputnumFI.isdigit():
        print("Good! It is an Int.")
        break
    else:
        if "." in inputnumFI:
            inputnumFI = inputnumFI.replace(".","0")
            if inputnumFI.isdigit():
                print("Good! It is a Float.")
        else:
            print("Try Again.")

