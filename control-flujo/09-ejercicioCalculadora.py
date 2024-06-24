print("######BIENVENIDO A LA CALCULADORA######")


while True:
    print("""
            Operaciones 
          suma              s
          resta             r
          divicion          d
          multiplicacion    m
          salir             salir 
          """)
    operacion = input("Que operacion te gustaria realizar?: ")
    if operacion.lower() == "salir":
        break
    valor1 =input("Ingresa valor 1: ")
    if valor1.lower() == "salir":
        break
    valor2  =input("Ingresa valor 2: ")
    if valor2.lower() == "salir":
        break
    suma = valor1 + valor2
    resta = valor1 - valor2
    divicion = valor1 / valor2
    multiplicacion = valor1 * valor2

    if operacion.lower() == "s":
        print(f"{valor1} + {valor2} = {suma}")
    elif operacion.lower() == "r":
        print(f"{valor1} - {valor2} = {resta}")
    elif operacion.lower() == "d":
        print(f"{valor1} / {valor2} = {divicion}")
    elif operacion.lower() == "m":
        print(f"{valor1} x {valor2} = {multiplicacion}")

    else:
        print("Operación no válida. Inténtalo de nuevo.")
    


    

