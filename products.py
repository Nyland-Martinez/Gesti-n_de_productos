import os

productos = []

def añadir_producto():
    nombre = input("Introduce el nombre del producto: ")
    while True:
        try:
            precio = float(input("Introduce el precio del producto: "))
            break
        except ValueError:
            print("Por favor, introduce un valor numérico válido para el precio")
    
    while True:
        try:
            cantidad = int(input("Introduce la cantidad disponible del producto: "))
            break
        except ValueError:
            print("Por favor, introduce un valor numérico válido para la cantidad")
            
    productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    print(f"Producto {nombre} añadido correctamente")

    pass

def ver_productos():
    if productos:
        print("\nLista de productos:")
        for i, producto in enumerate(productos, 1):
            print(f"{i}. Nombre: {producto['nombre']}, Precio: {producto['precio']:.2f}, Cantidad: {producto['cantidad']}")
    else:
        print("No hay productos en el inventario")
    pass

def actualizar_producto():
    nombre = input("Introduce el nombre del producto a actualizar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            print(f"Producto encontrado: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
            nuevo_nombre = input("Introduce el nuevo nombre: ")
            
            if nuevo_nombre:
                producto['nombre'] = nuevo_nombre
            while True:
                nuevo_precio = input("Introduce el nuevo precio: ")
                if nuevo_precio:
                    try:
                        producto['precio'] = float(nuevo_precio)
                        break
                    except ValueError:
                        print("Por favor, introduce un valor numérico válido para el precio")
                else:
                    break

            while True:
                nueva_cantidad = input("Introduce la nueva cantidad: ")
                if nueva_cantidad:
                    try:
                        producto['cantidad'] = int(nueva_cantidad)
                        break
                    except ValueError:
                        print("Por favor, introduce un valor numérico válido para la cantidad")
                else:
                    break

            print(f"Producto {producto['nombre']} actualizado correctamente")
            return
    print("Producto no encontrado.")
    pass

def eliminar_producto():
    nombre = input("Introduce el nombre del producto a eliminar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            productos.remove(producto)
            print(f"Producto {nombre} eliminado correctamente")
            return
    print("Producto no encontrado")
    pass

def guardar_datos():
    with open('productos.txt', 'w') as f:
        for producto in productos:
            f.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados correctamente")
    pass

def cargar_datos():
    if os.path.exists('productos.txt'):
        print("Cargando productos desde 'productos.txt'...")
        with open('productos.txt', 'r') as f:
            for linea in f:
                # Separar cada línea por comas
                nombre, precio, cantidad = linea.strip().split(',')
                # Agregar a la lista de productos como diccionario
                productos.append({"nombre": nombre, "precio": float(precio), "cantidad": int(cantidad)})
        print("Datos cargados correctamente.")
    else:
        print("Archivo 'productos.txt' no encontrado. Comenzando con un inventario vacío.")
    pass

def menu():
    cargar_datos() # Esta línea asegura que se carguen los datos guardados previamente

    while True:
        print("\tMenú")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

# Ejecución del programa
if __name__ == "__main__":
    menu()