class Cliente:
    #Aca creamos las propiedades del Cliente:
    def __init__(self, nombre, email, direccion):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.carrito = []

    #Funcion para agregar productos al carrito de cada cliente:
    def agregar_al_carrito(self, item):
        self.carrito.append(item)
        print(f"{item} agregado al carrito.")

    #Funcion para calcular el total de la compra por el cliente:
    def realizar_compra(self):
        total = sum(item.precio for item in self.carrito)
        if total == 0:
            print("El carrito está vacío. No se puede realizar la compra.")
        else:
            print(f"Compra realizada por {self.nombre}. Total a pagar: ${total} y el envio es a la direccion: {self.direccion}")
            self.carrito = []            

    #Imprimimos los datos del cliente:
    def __str__(self):
        return f"Cliente: {self.nombre}\nEmail: {self.email}\nDirección: {self.direccion}"

class Producto:
    #Aca creamos las propiedades del Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    #Funcion para que devuelva el producto creado:
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"
