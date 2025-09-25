# Variable de control(flag) para repetir el ingreso hasta que sea válido
invalid = True

# Bucle para validar que el número ingresado sea binario
while invalid:
    numero = input("Ingrese un número binario: ")
    # Convierte el número ingresado en una lista de caracteres
    digitos = list(numero)

    if len(numero) == 0:  # Chequea que la cadena no esté vacía
        print("No ingresaste nada. Intentá de nuevo.")
        continue

    for i in range(len(digitos)):
        # Verifica que cada dígito sea '0' o '1'
        if digitos[i] != '1':
            if digitos[i] != '0':
                print("El número ingresado no es un binario válido.")
                break
    else:
        # Si todos los dígitos son válidos, sale del bucle
        invalid = False

# Invierte la lista para que la posición 0 sea el dígito menos significativo
digitos.reverse()
decimal = 0

# Recorre la lista y suma el valor decimal correspondiente a cada dígito
for i in range(len(digitos)):
    decimal += int(digitos[i]) * 2**i

print(decimal)  # Muestra el resultado en decimal

# volver al menú, vincular con lógica de hernan
