from datetime import datetime
from itertools import product

# Función para verificar si un año es bisiesto
def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

# Ingreso de años de nacimiento
def ingresar_anios():
    anios = []
    cantidad = int(input("¿Cuántos integrantes hay en el grupo? "))
    for i in range(cantidad):
        while True:
            anio = input(f"Ingrese el año de nacimiento del integrante {i + 1}: ")
            if anio.isdigit() and len(anio) == 4:
                anios.append(int(anio))
                break
            else:
                print("Año inválido. Debe tener 4 dígitos numéricos.")
    return anios

# Contar años pares e impares
def contar_pares_impares(anios):
    pares = 0
    impares = 0
    for anio in anios:
        if anio % 2 == 0:
            pares += 1
        else:
            impares += 1
    print(f"\nCantidad de años pares: {pares}")
    print(f"Cantidad de años impares: {impares}")

# Evaluar condiciones del grupo
def evaluar_condiciones(anios):
    if all(anio > 2000 for anio in anios):
        print("Grupo Z")

    if any(es_bisiesto(anio) for anio in anios):
        print("Tenemos un año especial")

# Calcular edades actuales
def calcular_edades(anios):
    anio_actual = datetime.now().year
    return [anio_actual - anio for anio in anios]

# Producto cartesiano
def producto_cartesiano(anios, edades):
    conjunto_anios = set(anios)
    conjunto_edades = set(edades)
    #Usa product() (de itertools) para generar todas las combinaciones posibles entre un año y una edad (producto cartesiano)
    resultado = list(product(conjunto_anios, conjunto_edades))

    print("\nProducto cartesiano entre años y edades:")
    for par in resultado:
        print(par)

# Función principal
def main():
    print("=== ANÁLISIS DE AÑOS DE NACIMIENTO ===")
    anios = ingresar_anios()
    contar_pares_impares(anios)
    evaluar_condiciones(anios)
    edades = calcular_edades(anios)
    producto_cartesiano(anios, edades)

# Ejecutar programa
main()
