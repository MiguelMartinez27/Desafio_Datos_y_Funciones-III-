def seleccionar_masa():
    print("Tipos de Masa:")
    for i, masa in enumerate(MASAS, 1):
        print(f"{i}. {masa}")
    while True:
        try:
            opcion = int(input("Seleccione el tipo de masa: "))
            if 1 <= opcion <= len(MASAS):
                return MASAS[opcion - 1]
            else:
                print("Por favor, seleccione una opción válida.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")


MASAS = ["Tradicional", "Delgada", "Bordes de Queso"]
