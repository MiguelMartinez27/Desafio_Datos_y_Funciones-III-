def seleccionar_ingrediente():
    print("Ingredientes disponibles:")
    for i, ingrediente in enumerate(INGREDIENTES, 1):
        print(f"{i}. {ingrediente}")
    while True:
        try:
            opcion = int(input("Seleccione un ingrediente: "))
            if 1 <= opcion <= len(INGREDIENTES):
                return INGREDIENTES[opcion - 1]
            else:
                print("Por favor, seleccione una opción válida.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")


INGREDIENTES = [
    "Tomate",
    "Champiñones",
    "Aceituna",
    "Cebolla",
    "Pollo",
    "Jamón",
    "Carne",
    "Tocino",
    "Queso",
]
