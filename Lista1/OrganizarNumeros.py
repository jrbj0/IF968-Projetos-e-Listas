#João Rafael

num1 = int(input("Primeiro Número:  "))
num2 = int(input("Segundo Número:   "))
num3 = int(input("Terceiro Número:  "))

numreserva = 0


if (num1 > num2):
   numreserva = num1
   num1 = num2
   num2 = numreserva

if (num2 > num3):
    numreserva = num2
    num2 = num3
    num3 = numreserva

if (num1 > num2):
   numreserva = num1
   num1 = num2
   num2 = numreserva


print(num1)
print(num2)
print(num3)
