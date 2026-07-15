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
    print("=" * 85)
    print("AUDITORÍA DE CONTROL Y PREVENCIÓN DE INVENTARIO".center(85))
    print("=" * 85)

    if len(inventario) == 0:
        print("No hay productos registrados para auditar.")
        pausa()
        return

    total_reponer = 0
    productos_criticos = 0
    productos_alerta = 0

    print("{:<10}{:<22}{:>10}{:>10}{:>12}{:>15}".format("Código", "Producto", "Stock", "Mínimo", "Comprar", "Estado"))
    print("-" * 85)
    
    for producto in inventario:
        stock_actual = producto[3]
        stock_minimo = producto[4]
        
        limite_preventivo = stock_minimo * 1.20

        if stock_actual < stock_minimo:
            estado = "CRÍTICO"
            productos_criticos += 1
            comprar = (stock_minimo * 2) - stock_actual
        elif stock_actual == stock_minimo or stock_actual <= limite_preventivo:
            estado = "ALERTA"
            productos_alerta += 1
            comprar = (stock_minimo * 2) - stock_actual
        else:
            estado = "CONFORME"
            comprar = 0
            
        total_reponer += comprar
            
        print("{:<10}{:<22}{:>10}{:>10}{:>12}{:>15}".format(
            producto[0], producto[1], stock_actual, stock_minimo, comprar, estado
        ))
   
    print("-" * 85)
    print(f"RESUMEN OPERATIVO DE ALMACÉN:")
    print(f" - Productos en desabastecimiento (CRÍTICO) : {productos_criticos} ítem(s).")
    print(f" - En riesgo de desabastecerse (ALERTA)     : {productos_alerta} ítem(s).")
    print(f" - Total de unidades a pedir al proveedor   : {total_reponer} und.")
    print("=" * 85)
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
        print("4. Auditoría Logística y Prevención")
        print("5. Salir al menú principal")
        
        opcion = validar_entero("\nSeleccione una opción (1-5): ")

        if opcion == 1:
            registrar_producto()
        elif opcion == 2:
            buscar_producto()
        elif opcion == 3:
            modificar_producto()
        elif opcion == 4:
            auditar_inventario()
        elif opcion == 5:
            print("\nGracias por usar el sistema de inventario.")
            break
        else:
            print("ERROR. Opción inválida.")
            pausa()

menu_inventario()
        
        
    
