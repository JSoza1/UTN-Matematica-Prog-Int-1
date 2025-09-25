
###################################################
#MENU
while True:
    print("\n=== Bienvenido al Conversor de números ===")
    print("1. Decimal a Binario")
    print("2. Binario a Decimal")
    print("0. Salir")

    opt = input("Elija una opcion: ")

    if opt == "1":
        # pedir número hasta que sea válido
        while True:
            numero = input("Ingrese un numero decimal positivo: ")
            es_valido = True #Bandera de validación

            if numero == "":   #Si el user no ingresa ningun valor
                es_valido = False #Bandera cambia a FALSO
            else:
                for caracter in numero: #recorriendo caracteres ingresados
                    if caracter < "0" or caracter > "9":
                        es_valido = False

            if es_valido: #Si esta bandera sigue estando en True...
                numero = int(numero) #Se convierte el input original a entero para que pueda ser usado en la división
                break
            else:
                print("Error: debe ingresar solo números enteros positivos.")
            #Retorna para que lo intentes nuevamente

        ############### Decimal a Binario #################
        if numero == 0:
            print("El numero binario es 0")
        else:
            binario = ""
            while numero > 0:
                resto = numero % 2 #calculo del resto
                binario = str(resto) + binario #colocamos cada nuevo resto al inicio de la cadena
                numero = numero // 2
            print("El numero en binario es:", binario)

            #Retorna al menu despues de dar el resultado

    elif opt == "2":
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
            decimal += int(digitos[i]) * 2 ** i

        print(decimal)  # Muestra el resultado en decimal

        #Retorna al menu despues de dar el resultado

    elif opt == "0":
        print("Ejecución finalizada")
        break
    else:
        print("Opcion inválida. Intente de nuevo")
###################################################

