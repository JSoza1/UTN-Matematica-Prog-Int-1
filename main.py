
###################################################


############### Binario a Decimal #################

invalid = True  # Variable de control(flag) para repetir el ingreso hasta que sea válido

# Bucle para validar que el número ingresado sea binario
while invalid:
    numero = input("Ingrese un número binario: ")
    digitos = list(numero)  # Convierte el número ingresado en una lista de caracteres
    for i in range(len(digitos)):
        # Verifica que cada dígito sea '0' o '1'
        if digitos[i] != '1':
            if digitos[i] != '0':
                print("El número ingresado no es un binario válido.")
                break
    else:
        # Si todos los dígitos son válidos, sale del bucle
        invalid = False

digitos.reverse()  # Invierte la lista para que la posición 0 sea el dígito menos significativo
decimal = 0
print(digitos)  # Muestra la lista invertida (opcional, para depuración)

# Recorre la lista y suma el valor decimal correspondiente a cada dígito
for i in range(len(digitos)):
    decimal += int(digitos[i]) * 2**i

print(decimal)  # Muestra el resultado en decimal

# volver al menú, vincular con lógica de hernan