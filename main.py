# =================== Menú ====================
# Menu principal con bucle while de 3 opciones:
# Decimal a binario
# Binario a Decimal
# Salida

# Bucle principal
while True:
    # Mensajes del menu
    print("\n=== Bienvenido al Conversor de números ===")
    print("1. Decimal a Binario")
    print("2. Binario a Decimal")
    print("0. Salir")

    # Se pide opcion al usuario y se almacena en variable 
    opt = input("Elija una opcion: ")

    ######################################## Decimal a Binario ########################################
    # Inicio de condicional dentro del bucle while principal - se evalua si el usuario ingreso "1"
    if opt == "1":

        # Nuevo bucle while de validaciones - se evaluan posibles ingresos erroneos 
        while True:
            # Primer ingreso de numero - se almacena en variable para posteriormente ser validado
            numero = input("Ingrese un numero decimal positivo: ")
            es_valido = True #Bandera de validación

            # Validación de usuario que no ingresa nada
            if numero == "":   
                es_valido = False #Bandera cambia a FALSO

            # Validación de usuario que no ingresa un numero decimal positivo
            else:
                for caracter in numero: #recorriendo caracteres ingresados
                    if caracter < "0" or caracter > "9":
                        es_valido = False
            
            # Si el caracter ingresado es valido y la bandera es True
            if es_valido: # <----- (Bandera en True)

                # Se convierte el input original a entero para que pueda ser utilizado luego en una division
                numero = int(numero) 

                # Se sale del bucle while de validaciones
                break

            # Mensaje de error, en caso de no pasar validaciones
            else:
                print("ERROR. Debe ingresar solo números enteros positivos. Intente nuevamente")

            #Se repite el bucle de ingreso de número y validaciones (dentro de la opción Decimal a Binario)

        ############### Calculo de Decimal a Binario #################
        # Primera validación dentro de los calculos
        if numero == 0:
            print("El numero binario es 0") #Si el numero decimal ingresado es 0, en binario tambien es 0
        
        # Si el numero ingresado es distinto de 0
        else:
            # Se inicializa un string vacio para ir armando el número binario
            binario = ""
            
            # Mientras el número sea mayor que cero, se hacen divisiones
            while numero > 0:
                # Se calcula el resto de dividir el número por 2 (será 0 o 1)
                resto = numero % 2 
                # Se convierte el resto a texto y se lo agrega al principio del string "binario"
                binario = str(resto) + binario
                # Se actualiza el número dividiéndolo por 2 (división entera)
                numero = numero // 2
            # Se muestra el resultado final en binario
            print("El numero en binario es: ", binario)

            #Se retorna al menú principal despues de dar el resultado

    ######################################## Binario a Decimal ########################################
    # Se evalua si el usuario ingreso "2"
    elif opt == "2":

        # Se inicia con una variable de control(flag) para repetir el ingreso hasta que sea válido
        invalid = True

        # Bucle para validar que el número ingresado sea binario
        while invalid:
            # Primer ingreso de numero - se almacena en variable para posteriormente ser validado
            numero = input("Ingrese un número binario: ")
    
            # Condicional para validar que el ingreso no este vacio
            if len(numero) == 0: 
                print("No ingresaste nada. Intentá de nuevo.")
                continue

            # El el caso de ingresar un número se convierte en una lista de caracteres
            digitos = list(numero) 

            # Bucle for para validar que cada digito ingresado sea "0" o "1"
            for i in range(len(digitos)):
                if digitos[i] != '1':
                    if digitos[i] != '0':
                        # En el caso de que haya digitos que no sean "0" o "1", se muestra mensaje de error
                        print("ERROR. Lo ingresado no corresponde a numeros binarios. Intente nuevamente")
                        # Posteriormente se sale del bucle, para volver a ingresar números
                        break

            # Si todos los digitos son validos, se sale del bucle de validaciones
            else:
                # Se modifica el valor booleano de la bandera invalid a False
                invalid = False

        ############### Calculo de Decimal a Binario #################

        # Se invierte la lista previamente creada para que el índice 0 corresponda al bit menos significativo (el de la derecha)
        digitos.reverse()

        # Se inicializa una variable que almacenará el resultado en decimal
        decimal = 0

        # Bucle for para recorrer la lista de dígitos binarios ya invertida previamente

        # Recorre la lista y suma el valor decimal correspondiente a cada dígito
        for i in range(len(digitos)):
            # Se convierte el dígito a entero y se multiplica por 2 elevado a su posición
            # Esto aplica la fórmula del sistema binario: dígito × 2 ^ posición
            decimal += int(digitos[i]) * 2 ** i

        # Mensaje final con número decimal
        print(decimal)  

        #Se retorna al menú principal despues de dar el resultado

######################################## Cierre del Programa ########################################
    # se evalua si el usuario ingreso "0"
    elif opt == "0":
        # Mensaje final de cierre
        print("Ejecución finalizada")
        # Cierre del programa
        break

    else:
        # Mensaje de error
        print("Opcion inválida. Intente de nuevo")
        # Se retorna al menú principal