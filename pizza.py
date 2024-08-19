# importar funciones
from obtener_opc import seleccionar_opcion
from seleccionar_salsas import seleccionar_salsa as salsa
from seleccionar_masas import seleccionar_masa as masas
from seleccionar_ingredientes import seleccionar_ingrediente as ingredientes
from menu_seleccion import menu


# Definir opciones
class armar_pizza:
    def __init__(self):
        self.masa = "Tradicional"
        self.salsa = "Tomate"
        self.ingredientes = []

    def cambiar_masa(self, masa):
        self.masa = masa

    def cambiar_salsa(self, salsa):
        self.salsa = salsa

    def agregar_ingrediente(self, ingrediente):
        if ingrediente not in self.ingredientes:
            self.ingredientes.append(ingrediente)

    def eliminar_ingrediente(self, ingrediente):
        if ingrediente in self.ingredientes:
            self.ingredientes.remove(ingrediente)

    def mostrar_pizza(self):
        print(f"Masa: {self.masa}")
        print(f"Salsa: {self.salsa}")
        print(
            f"Ingredientes: {', '.join(self.ingredientes) if self.ingredientes else 'Ninguno'}"
        )

    def estimar_tiempo(self):
        return 20 + 2 * len(self.ingredientes)


# respuesta a seleccion de opciones
def dar_respuesta():
    pizza = armar_pizza()

    while True:
        menu()
        opcion = seleccionar_opcion()

        if opcion == 1:
            pizza.cambiar_masa(masas())
        elif opcion == 2:
            pizza.cambiar_salsa(salsa())
        elif opcion == 3:
            pizza.agregar_ingrediente(ingredientes())
        elif opcion == 4:
            pizza.eliminar_ingrediente(ingredientes())
        elif opcion == 5:
            pizza.mostrar_pizza()
        elif opcion == 6:
            print(
                f"El tiempo estimado de preparación es {pizza.estimar_tiempo()} minutos."
            )
        elif opcion == 7:
            pizza.mostrar_pizza()
            print(
                f"El tiempo estimado de preparación es {pizza.estimar_tiempo()} minutos."
            )
            confirmar = input("¿Desea confirmar el pedido? (s/n): ").lower()
            if confirmar == "s":
                print("¡Pedido confirmado!")
                break
        elif opcion == 8:
            print("Saliendo del menú. ¡Gracias!")
            break


if __name__ == "__main__":
    dar_respuesta()
