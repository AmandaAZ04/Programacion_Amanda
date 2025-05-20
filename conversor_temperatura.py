# Sistema de conversión de temperatura entre distintas escalas, Celsius, Fahrenheit y Kelvin.
# 1.- Contruir Menu
# 2.- Definir funciones de conversión
# 3.- Pedir datos al usuario
# 4.- Realizar conversión
# 5.- Mostrar el resultado

# Celsius a Kelvin: K = C + 273.15
# Celsius a Fahrenheit: F = (9/5) * C + 32
# Kelvin a Celsius: C = K - 273.15
# Kelvin a Fahrenheit: F = (9/5) * (K - 273.15) + 32
# Fahrenheit a Celsius: C = (5/9) * (F - 32)
# Fahrenheit a Kelvin: K = (5/9) * (F - 32) + 273.15

def cargar_menu():
    print("[1] Convertir °C a K.")
    print("[2] Convertir °C a °F.")
    print("[3] Convertir K a °C.")
    print("[4] Convertir K a °F.")
    print("[5] Convertir °F a °C.")
    print("[6] Convertir °F a K.")
    print("[0] Salir.")

def convertir_celsius_kelvin(temperatura_inicial):
    temperatura = temperatura_inicial + 273.15
    return temperatura

def convertir_celcius_fahrenheit(temperatura_inicial):
    temperatura = (9/5) * temperatura_inicial + 32
    return temperatura

def convertir_kelvin_celsius(temperatura_inicial):
    temperatura = temperatura_inicial - 273.15
    return temperatura

def convertir_kelvin_fahrenheit(temperatura_inicial):
    temperatura = (9/5) * (convertir_kelvin_celsius(temperatura_inicial)) + 32
    return temperatura

def convertir_fahrenheit_celsius(temperatura_inicial):
    temperatura = (5/9) * (temperatura_inicial - 32)
    return temperatura

def convertir_fahrenheit_kelvin(temperatura_inicial):
    temperatura = convertir_fahrenheit_celsius(temperatura_inicial) + 273.15
    return temperatura

def solicitar_datos():
    temperatura_usuario = float(input("Ingrese su temperatura inicial: "))
    return temperatura_usuario


def programa_principal():
    print()
    print("Súper Conversor de Temperaturas!!")
    print("==================================")
    
    while True:
        cargar_menu()
        print()
        opcion = input("Seleccione su opción [0-6]: ")
        resultado = 0
        temperatura_inicial = 0
        escala_inicial = ""
        escala_final = ""

        if opcion == "1":
            escala_inicial = "°C"
            escala_final = " K"
            temperatura_inicial = solicitar_datos()
            resultado = convertir_celsius_kelvin(temperatura_inicial)

        elif opcion == "2":
            escala_inicial = "°C"
            escala_final = "°F"
            temperatura_inicial = solicitar_datos()
            resultado = convertir_celcius_fahrenheit(temperatura_inicial)

        elif opcion == "3":
            escala_inicial = " K"
            escala_final = "°C"
            temperatura_inicial = solicitar_datos()
            resultado = convertir_kelvin_celsius(temperatura_inicial)

        elif opcion == "4":
            escala_inicial = " K"
            escala_final = "°F"
            temperatura_inicial = solicitar_datos()
            resultado = convertir_kelvin_fahrenheit(temperatura_inicial)

        elif opcion == "5":
            escala_inicial = "°F"
            escala_final = "°C"
            temperatura_inicial = solicitar_datos()
            resultado = convertir_fahrenheit_celsius(temperatura_inicial)

        elif opcion == "6":
            escala_inicial = "°F"
            escala_final = " K"
            temperatura_inicial = solicitar_datos()
            resultado = convertir_fahrenheit_kelvin(temperatura_inicial)

        elif opcion == "0":
            print("Saliendo de Sistema...")
            break
        else:
            print("Opción Inválida.")
            print()
            pass
        print()
        print(f"{temperatura_inicial}{escala_inicial} = {resultado}{escala_final}")
        print()
        
programa_principal()