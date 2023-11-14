import sys

inputnumFI = input("Input a number:")

if "-" in inputnumFI:
    inputnumFI = inputnumFI.replace("-", "")
    if "." in inputnumFI:
        inputnumFI = inputnumFI.replace(".","")
        if inputnumFI.isdigit():
            print("Negative Float!")
            sys.exit()
    if inputnumFI.isdigit():
        print("Negative Int")
        sys.exit()
if "." in inputnumFI:
    inputnumFI = inputnumFI.replace(".", "")
    if inputnumFI.isdigit():
        print("Positive Float")
        sys.exit()
if inputnumFI.isdigit():
    print("Positive int!")
    sys.exit()
else:
    print("Boolean or String Perhaps??")
