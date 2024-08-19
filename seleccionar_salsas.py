def seleccionar_salsa():
    print("Tipos de Salsa:")
    for i, salsa in enumerate(SALSAS, 1):
        print(f"{i}. {salsa}")
    while True:
        try:
            opcion = int(input("Seleccione el tipo de salsa: "))
            if 1 <= opcion <= len(SALSAS):
                return SALSAS[opcion - 1]
            else:
                print("Por favor, seleccione una opción válida.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")


SALSAS = ["Tomate", "Alfredo", "Barbecue", "Pesto"]
