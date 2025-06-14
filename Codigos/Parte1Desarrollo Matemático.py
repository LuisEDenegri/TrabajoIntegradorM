#Pedir los DNIs al usuario
def pedir_dni(numero):
    dni = input(f"Ingrese el DNI #{numero} (8 dígitos): ")
    while len(dni) != 8 or not dni.isdigit():
        print("Entrada inválida. El DNI debe tener exactamente 8 números.")
        dni = input(f"Ingrese el DNI #{numero} nuevamente: ")
    return dni
#Se evalua cada digito de la lista y se quitan los numeros repetidos
def quitar_repetidos(lista):
    nueva_lista = []
    for digito in lista:
        if digito not in nueva_lista:
            nueva_lista.append(digito)
    return nueva_lista
#Lista con mayor cantidad de digitos
def mostrar_resultados(largos):
    mayor = max(largos)
    ganadores = [i+1 for i, largo in enumerate(largos) if largo == mayor]

    if len(ganadores) == 1:
        print(f"El DNI #{ganadores[0]} tiene más dígitos únicos: {mayor}")
    else:
        print(f"Hay un empate entre los DNIs con más dígitos únicos: {mayor}")
        print("DNIs empatados:", ", ".join(f"#{n}" for n in ganadores))
#Identifica los ceros en las listas
def verificar_ceros(listas):
    encontrados = []
    for i, lista in enumerate(listas, start=1):
        if '0' in lista:
            encontrados.append(i)
    if encontrados:
        for n in encontrados:
            print(f"El DNI #{n} contiene el dígito 0.")
    else:
        print("Ningún DNI contiene el dígito 0.")

def main():
    dnis = [pedir_dni(i) for i in range(1, 4)]
    listas = [list(dni) for dni in dnis]
    listas_sin_repe = [quitar_repetidos(lista) for lista in listas]

    print("\nDNI sin dígitos repetidos:")
    for i, sin_repe in enumerate(listas_sin_repe, start=1):
        print(f"DNI #{i}:", sin_repe)

    largos = [len(sin_repe) for sin_repe in listas_sin_repe]
    print("\nResultado:")
    mostrar_resultados(largos)

    print("\nVerificación de ceros:")
    verificar_ceros(listas)

if __name__ == "__main__":
    main()