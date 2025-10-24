def dividir_numeros():
    try:
        # Solicitar al usuario que introduzca dos números
        num1 = input("Introduce el primer número: ")
        num2 = input("Introduce el segundo número: ")

        # Convertir las entradas a números enteros
        num1 = int(num1)
        num2 = int(num2)

        # Realizar la división del primer número entre el segundo
        resultado = num1 / num2

        # Devolver el resultado de la división
        print(f"El resultado de la división es: {resultado}")

    except ValueError:
        # Si el usuario introduce algo que no es un número
        print("Error: Debes introducir un número válido")

    except ZeroDivisionError:
        # Si el usuario intenta dividir entre cero
        print("Error: No es posible dividir entre cero")

    finally:
        # Mensaje final siempre mostrado
        print("Operación finalizada.")


# Llamada a la función
dividir_numeros()
