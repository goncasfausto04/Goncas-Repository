#exercicio 3 e 4

while True:
    inputnumFI = input("Input a number:")
    if inputnumFI.isdigit():
        print("It is a non negative Int.")
        break
    else:
        if "-" in inputnumFI:
            inputnumFI = inputnumFI.replace("-", "")
            if "." in inputnumFI:
                inputnumFI = inputnumFI.replace(".","")
                if inputnumFI.isdigit():
                    print("That is a negative float.")
                    break
                else:
                    print("That is a positive float.")
                    break
            else:
                print("That is a negative int.")
                break
        if "." in inputnumFI:
            inputnumFI = inputnumFI.replace(".", "")
            if inputnumFI.isdigit():
                print("That is a positive float.")
                break
        else:
            print("Try Again.")

