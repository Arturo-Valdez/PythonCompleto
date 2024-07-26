class Producto:
    #Constructor
    #  Inicializa un producto con un nombre y un precio.
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    #Devuelve una representación en cadena del producto para facilitar la visualización.
    def __str__(self):
        return f"Producto: {self.nombre} - Precio: {self.precio}"


class Categoria:
    productos = []

    # Inicializa una categoría con un nombre y una lista de productos.
    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos
    
    #Añade un producto a la lista de productos de la categoría.
    def agregar(self, producto):
        self.productos.append(producto)
    
    #Imprime la representación en cadena de cada producto en la lista.
    def imprimir(self):
        for producto in self.productos:
            print(producto)

kayak = Producto("Kayak", 1000)
bicicleta = Producto("Bicicleta", 750)
surfboard = Producto("Surfboard", 500)                
deportes = Categoria("Deportes", [kayak, bicicleta])
deportes.agregar(surfboard)

#Producto: Bicicleta - Precio: 750
# Producto: Kayak - Precio: 1000
# Producto: Surfboard - Precio: 500
deportes.imprimir()