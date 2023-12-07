from cliente import Cliente, Producto

# Crear instancias de productos
producto1 = Producto("Pava Electrica", 3500)
producto2 = Producto("Ventilador", 4000)
producto3 = Producto("Motoguadana", 50000)

# Obtener datos del clientes
nombre = input("Ingrese el nombre del cliente: ")
email = input("Ingrese el email del cliente: ")
direccion = input("Ingrese la dirección del cliente: ")

# Crear instancia de cliente con los datos ingresados
cliente1 = Cliente(nombre, email, direccion)

# Agregar productos al carrito del cliente
cliente1.agregar_al_carrito(producto1)
cliente1.agregar_al_carrito(producto2)
cliente1.agregar_al_carrito(producto3)

# Realizar compra
cliente1.realizar_compra()

#Imprimimos al CLIENTE para ver sus datos:
print(cliente1)
