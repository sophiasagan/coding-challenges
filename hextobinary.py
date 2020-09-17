while True:
    print("Enter 'x' for exit.")
    hex = input("Enter number in hex Format: ")
    if hex == 'x':
        break
    else:
        decimal = int(hex, 16)

        print(hex,"in Binary =",bin(decimal),"\n")
        print(hex,"in Decimal =", decimal,"\n")