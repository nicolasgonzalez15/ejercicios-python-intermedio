# Práctica excepciones
# Ejercicio 1
# -----------------------------
def division(a,b):

    try:
        resultado = a/b
        print(f"El resultado de la división es: {resultado}")
    except ZeroDivisionError:
        print("No se puede dividir por 0.")


nro1 = float(input("Ingrese primer número: "))
nro2 = float(input("Ingrese segundo número: "))

# Llamar a función división
division(nro1,nro2)

# Ejercicio 2
# -----------------------------

def sumando(a,b):
    try:
        resultado = a+b
        print(f"Resultado: {resultado}")
    except TypeError:
        print("No se pueden sumar o concatenar números con cadenas.")

sumando(1,2)

# Ejercicio 3
# -----------------------------

def acceder_clave(diccionario,clave):
    try:
        print(f"El contenido de la clave {clave} es: {diccionario[clave]}")
    except KeyError:
        print("No existe la clave de valor ingresada para el diccionario.")

diccionario = {
    "nombre":"Nino",
    "edad":34,
    "pais":"Argentina",
    "casado":False
}

acceder_clave(diccionario,"deporte")

# Ejercicio 4
# -----------------------------

def lecturarchivo():

    try:
        with open("files/hola.txt","r") as archivo:
            contenido = archivo.read()
            print(contenido)
            archivo.close()
    except FileNotFoundError:
        print("No existe el archivo seleccionado")
        with open("files/archivo.txt","w") as archivo:
            archivo.write("Línea 1\n")
            archivo.close()

lecturarchivo()

# Ejercicio 5
# -----------------------------

def dividimos(a,b):

    try:
        resultado = a/b
        print(f"El resultado de la división es: {resultado}")
    except ZeroDivisionError:
        print("No se puede dividir por 0.")
    except TypeError:
        print("No se pueden dividir números y strings.")