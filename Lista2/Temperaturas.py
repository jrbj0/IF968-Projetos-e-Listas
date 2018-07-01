print("Bem vindo ao conversor de temperaturas")
print("As escalas aceitáveis são:")
print('Celsius como "c"')
print('Kelvin como "k"')
print('Fahrenheit como "f"')


temperatura = float(input("\nDigite uma temperatura: "))

escala1 = input("\nDigite a escala inicial: ").lower()

escala2 = input("\nDigite a escala para qual você deseja converter: ").lower()


if escala1 == escala2:
    print("\n\nAs escalas já são iguais!")
else:
    
    if escala1 == 'c':
        if escala2 == 'k':
            temperatura = temperatura + 273.15
        if escala2 == 'f':
            temperatura = (temperatura * 1.8) + 32.0

    if escala1 == 'k':
        temperatura = temperatura - 273.15
        if escala2 == 'f':
            temperatura = (temperatura * 1.8) + 32.0

    if escala1 == 'f':
        temperatura = (temperatura - 32)/ 1.8
        if escala2 == 'k':
            temperatura = temperatura + 273.15
            

print("A temperatura é", temperatura, escala2.upper())        
