# ============================================================
#  FERRETERÍA MACKLENA S.A.
#  Módulo: Sistema de Auditoría y Control de Inventario
#  Curso: Fundamentos de Programación 1
#  Ciclo: 2026-15 | TB2
#  US cubiertos: US-08, US-09, US-10, US-11, US-12, US-13, US-14
# ============================================================

inventario = []

def buscar_codigo(codigo):
    for i in range(len(inventario)):
        if inventario[i][0] == codigo:
            return i
    return -1
def validar_texto(mensaje):
    while True:
        dato = input(mensaje).strip()
        if dato != "":
            return dato
        print("ERROR. Debe ingresar un texto válido.")

def validar_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                return numero
            print("ERROR. Debe ingresar un número mayor que cero.")
        except ValueError:
            print("ERROR. Debe ingresar un número entero.")

def limpiar():
    print("\n" * 30)
    
def pausa():
    input("\nPresione ENTER para volver al menú...")
    
def registrar_producto():
    limpiar()
    print("=" * 60)
    print("REGISTRAR PRODUCTO".center(60))
    print("=" * 60)

    while True:
        codigo = validar_texto("Código del producto (Ej. P001): ").upper()
        if buscar_codigo(codigo) == -1:
            break
        print("ERROR. El código ya existe.")

    nombre = validar_texto("Nombre del producto: ")
    categoria = validar_texto("Categoría del producto: ")
    stock = validar_entero("Stock actual: ")
    minimo = validar_entero("Stock mínimo: ")

    inventario.append([codigo, nombre, categoria, stock, minimo])
    print("\nProducto registrado exitosamente.")
    pausa()

def buscar_producto():
    limpiar()
    print("=" * 60)
    print("BUSCAR PRODUCTO".center(60))
    print("=" * 60)
    
    if len(inventario) == 0:
        print("No hay productos registrados.")
        pausa()
        return

    codigo = validar_texto("Ingrese el código: ").upper()
    indice = buscar_codigo(codigo)

    if indice != -1:
        producto = inventario[indice]
        print("\nProducto encontrado:")
        print(f"Código: {producto[0]}")
        print(f"Nombre: {producto[1]}")
        print(f"Categoría: {producto[2]}")
        print(f"Stock actual: {producto[3]}")
        print(f"Stock mínimo: {producto[4]}")
    else:
        print("\nProducto no encontrado.")
    
    pausa()

def modificar_producto():
    limpiar()
    print("=" * 60)
    print("MODIFICAR PRODUCTO".center(60))
    print("=" * 60)
    
    if len(inventario) == 0:
        print("No hay productos registrados.")
        pausa()
        return

    codigo = validar_texto("Ingrese el código del producto a modificar: ").upper()
    indice = buscar_codigo(codigo)

    if indice != -1:
        producto = inventario[indice]
        print("\nProducto encontrado:")
        print(f"Código: {producto[0]}")
        print(f"Nombre: {producto[1]}")
        print(f"Categoría: {producto[2]}")
        print(f"Stock actual: {producto[3]}")
        print(f"Stock mínimo: {producto[4]}")

        nombre = validar_texto("Nuevo nombre del producto: ")
        categoria = validar_texto("Nueva categoría del producto: ")
        stock = validar_entero("Nuevo stock actual: ")
        minimo = validar_entero("Nuevo stock mínimo: ")

        inventario[indice] = [codigo, nombre, categoria, stock, minimo]
        print("\nProducto modificado exitosamente.")
    else:
        print("\nProducto no encontrado.")
    
    pausa()
    
def auditar_inventario():
    limpiar()
    print("=" * 70)
    print("AUDITORÍA DE INVENTARIO".center(70))
    print("=" * 70)

    if len(inventario) == 0:
        print("No hay productos registrados.")
        pausa()
        return
    total_reponer = 0
    productos_criticos = 0

    print("{:<10}{:<20}{:>10}{:>10}{:>12}{:>15}".format("Código", "Producto", "Stock", "Mínimo", "Comprar", "Estado"))
    print("-" * 80)
    for producto in inventario:
        comprar = producto[4] - producto[3] if producto[3] < producto[4] else 0
        estado = "CRÍTICO" if producto[3] < producto[4] else "OK"
        if estado == "CRÍTICO":
            productos_criticos += 1
            total_reponer += comprar
        print("{:<10}{:<20}{:>10}{:>10}{:>12}{:>15}".format(producto[0], producto[1], producto[3], producto[4], comprar, estado))
   
    print("-" * 80)
    print(f"Total de productos críticos: {productos_criticos}")
    print(f"Total a reponer: {total_reponer}")
    pausa()

def reporte_reposicion():
    limpiar()
    print("=" * 70)
    print("REPORTE DE REPOSICIÓN".center(70))
    print("=" * 70)

    if len(inventario) == 0:
        print("\nNo hay productos registrados.")
        pausa()
        return

    total_reponer = 0
    existe = False

    print("{:<10}{:<20}{:>10}{:>10}{:>12}".format("Código", "Producto", "Stock", "Mínimo", "Comprar"))
    print("-" * 70)
    for producto in inventario:
        if producto[3] < producto[4]:
            existe = True
            comprar = producto[4] - producto[3]
            total_reponer += comprar
            print("{:<10}{:<20}{:>10}{:>10}{:>12}".format(producto[0], producto[1], producto[3], producto[4], comprar))
    print("-" * 70)
    if existe:
        print(f"\nTotal a reponer: {total_reponer}")
    else:
        print("\nNo hay productos que requieran reposición.")
    pausa()
    
def menu_inventario():
    while True:
        limpiar()
        print("=" * 60)
        print("FERRERÍA MAKENA".center(60))
        print("MENÚ DE INVENTARIO".center(60))
        print("=" * 60)
        print("1. Registrar producto")
        print("2. Buscar producto")
        print("3. Modificar producto")
        print("4. Auditoría de inventario")
        print("5. Reporte de reposición")
        print("6. Salir al menú principal")
        
        opcion = validar_entero("\nSeleccione una opción (1-6): ")

        if opcion == 1:
            registrar_producto()
        elif opcion == 2:
            buscar_producto()
        elif opcion == 3:
            modificar_producto()
        elif opcion == 4:
            auditar_inventario()
        elif opcion == 5:
            reporte_reposicion()
        elif opcion == 6:
            print("\nGracias por usar el sistema de inventario.")
            break
        else:
            print("ERROR. Opción inválida.")
            pausa()

menu_inventario()
        
        
    
