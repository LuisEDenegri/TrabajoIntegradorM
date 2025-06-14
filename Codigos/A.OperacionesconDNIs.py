def ingresar_dnis():
    dnis = []
    cantidad = int(input("¿Cuántos DNIs quiere ingresar? "))
    for i in range(cantidad):
        while True:
            dni = input(f"Ingrese el DNI número {i + 1} (8 dígitos): ")
            if dni.isdigit() and len(dni) == 8:
                dnis.append(dni)
                break
            else:
                print("Entrada inválida. El DNI debe tener exactamente 8 dígitos numéricos.")
    return dnis

def obtener_conjuntos_digitos(dnis):
    conjuntos = []
    for dni in dnis:
        conjuntos.append(set(dni))
    return conjuntos

def mostrar_operaciones_conjuntos(conjuntos):
    union_total = set.union(*conjuntos)
    interseccion_total = set.intersection(*conjuntos)
    diferencia_simetrica = set.symmetric_difference(*conjuntos)

    print("\nOperaciones entre todos los conjuntos (dígitos ordenados):")
    print("Unión de todos los dígitos:", sorted(union_total))
    print("Intersección de todos los dígitos:", sorted(interseccion_total))
    print("Diferencia simétrica entre todos:", sorted(diferencia_simetrica))

    # Evaluación de condiciones lógicas:
    if interseccion_total:
        for digito in sorted(interseccion_total, key=int):
            print(f"Dígito compartido: {digito}")

    for idx, conjunto in enumerate(conjuntos):
        if len(conjunto) > 6:
            print(f"Diversidad numérica alta en DNI {idx + 1}")

def contar_frecuencias(dnis):
    print("\nFrecuencia de dígitos por DNI:")
    for idx, dni in enumerate(dnis):
        print(f"\nDNI {idx + 1}: {dni}")
        for digito in sorted(set(dni), key=int):
            print(f"El dígito {digito} aparece {dni.count(digito)} veces")

def sumar_digitos(dnis):
    print("\nSuma total de dígitos por DNI:")
    for idx, dni in enumerate(dnis):
        suma = sum(int(d) for d in dni)
        print(f"DNI {idx + 1}: {dni} -> Suma: {suma}")

def main():
    print("=== PROCESADOR DE DNIs ===")
    dnis = ingresar_dnis()
    conjuntos = obtener_conjuntos_digitos(dnis)

    print("\nConjuntos de dígitos únicos por DNI (ordenados):")
    for i, conjunto in enumerate(conjuntos):
        print(f"DNI {i + 1}: {sorted(conjunto, key=int)}")

    mostrar_operaciones_conjuntos(conjuntos)
    contar_frecuencias(dnis)
    sumar_digitos(dnis)

# Ejecutar el programa
main()
