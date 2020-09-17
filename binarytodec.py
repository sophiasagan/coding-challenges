while True:
    print("Enter 'x' for exit.")
    binary = input("Enter number in Binary Format: ")
    if binary == 'x':
        break
    else:
        decimal = int(binary, 2)
        print(binary,"in Decimal =",decimal,"\n")
        print(binary, "in Hex =", hex(decimal), "\n")