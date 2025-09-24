invalid = True

while invalid:
    numero = input("Ingrese un número binario: ")
    digitos = list(numero)
    for i in range(len(digitos)):
        if digitos[i] != '1':
            if digitos[i] != '0':
                print("El número ingresado no es un binario válido.")
                break
    else:
        invalid = False

digitos.reverse()
decimal = 0
print(digitos)

for i in range(len(digitos)):
    decimal += int(digitos[i]) * 2**i

print(decimal)

# volver al menú, vincular con lógica de hernan