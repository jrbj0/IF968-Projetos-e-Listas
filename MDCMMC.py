#João Rafael

def MMC(x, y):
    mdc = MDC(x, y)
    mmc = int((x * y) / mdc)
    
    return mdc, mmc

def MDC(x, y):
    x -= (y * (x // y))
    if x > 0:
        y = MDC(y, x)
    return y

##########################

while True:
    num1 = int(input("INSIRA O PRIMEIRO NUMERO:\n"))
    num2 = int(input("INSIRA O SEGUNDO NUMERO:\n"))
    if not num1 or not num2:
        break
    
    mdc, mmc = MMC(num1, num2)

    print("\nMDC:", mdc)
    if mdc == 1:
        print("Primos relativos!")
    print("\nMMC:", mmc)

    print("\n\nINSIRA 0 CASO DESEJE PARAR\n")

