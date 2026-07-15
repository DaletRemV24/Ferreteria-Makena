ventas = []
detalleVentas = []

def validar_texto(mensaje):
    while True:
        dato = input(mensaje).strip()
        if dato != "":
            return dato
        print("ERROR. No puede dejar el campo vacío.")

def validar_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                return numero
            print("ERROR. Debe ingresar un número mayor que cero.")
        except ValueError:
            print("ERROR. Debe ingresar un número entero.")

def validar_real(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            if numero > 0:
                return numero
            print("ERROR. Debe ingresar un valor mayor que cero.")
        except ValueError:
            print("ERROR. Debe ingresar un número válido.")

def limpiar():
    print("\n" * 30)
def pausa():
    input("\nPresione ENTER para volver al menú...")

def buscar_boleta(boleta):
    for i in range(len(ventas)):
        if ventas[i][0] == boleta:
            return i
    return -1
    
def titulo(texto):
    limpiar()
    print("=" * 60)
    print(texto.center(60))
    print("=" * 60)

def registrar_venta():
    titulo("REGISTRAR VENTA")
    while True:
        boleta = validar_texto("Código de boleta (Ej. B001): ").upper()
        if buscar_boleta(boleta) == -1:
            break
        print("ERROR. La boleta ya existe.")

    cliente = validar_texto("Nombre del cliente: ").title()
    cantidadProductos = validar_entero("N° de productos en esta boleta: ")
    totalVenta = 0

    for i in range(cantidadProductos):
        print()
        print("-" * 55)
        print(f" Producto {i+1} de {cantidadProductos}")
        print("-" * 55)
        producto = validar_texto("Nombre del producto: ").title()
        cantidad = validar_entero("Cantidad vendida: ")
        precio = validar_real("Precio unitario (S/): ")
        subtotal = cantidad * precio

        print()
        print(f"Subtotal: {cantidad} x S/{precio:.2f} = S/{subtotal:.2f}")

        # Guardar detalle

        detalleVentas.append([boleta, producto, cantidad, precio, subtotal])
        totalVenta += subtotal

    ventas.append([boleta, cliente, totalVenta])

    print()
    print("=" * 70)
    print(f"BOLETA N° {boleta}")
    print(f"CLIENTE : {cliente}")
    print("=" * 70)
    print("{:<25}{:>10}{:>12}{:>15}".format("Producto","Cant.","P.Unit","Subtotal"))
    print("-" * 70)
    for detalle in detalleVentas:
        if detalle[0] == boleta:
            print("{:<25}{:>10}{:>12.2f}{:>15.2f}".format(detalle[1], detalle[2], detalle[3], detalle[4]))
    print("-" * 70)
    print("{:>58} S/{:.2f}".format("TOTAL:", totalVenta))
    print("=" * 70)
    print()
    print("Venta registrada correctamente.")

    pausa()

def modificar_venta():
    titulo("MODIFICAR VENTA")
    if len(ventas) == 0:
        print("No existen ventas.")
        pausa()
        return
    boleta = validar_texto("Ingrese la boleta: ").upper()
    posicion = buscar_boleta(boleta)
    if posicion == -1:
        print("La boleta no existe.")
        pausa()
        return
    print()
    print("1. Cambiar cliente")
    print("2. Rehacer productos")
    print("3. Cancelar")

    opcion = validar_entero("Seleccione: ")
    if opcion == 1:
        nuevoCliente = validar_texto("Nuevo cliente: ").title()
        ventas[posicion][1] = nuevoCliente
        print()
        print("Cliente actualizado correctamente.")
    elif opcion == 2:
        respuesta = input("¿Desea rehacer toda la boleta? (S/N): ").upper()
        if respuesta == "S":
            eliminar_detalle(boleta)
            registrar_detalle(boleta,posicion)
    pausa()

def eliminar_detalle(boleta):
    i = 0
    while i < len(detalleVentas):
        if detalleVentas[i][0] == boleta:
            detalleVentas.pop(i)
        else:
            i += 1

def registrar_detalle(boleta,posicion):
    cantidadProductos = validar_entero("Cantidad de productos: ")
    total = 0
    for i in range(cantidadProductos):
        print()
        print(f"Producto {i+1}")
        producto = validar_texto("Nombre: ").title()
        cantidad = validar_entero("Cantidad: ")
        precio = validar_real("Precio: ")
        subtotal = cantidad * precio
        detalleVentas.append([boleta, producto, cantidad, precio, subtotal])
        total += subtotal
    ventas[posicion][2] = total
    print()
    print("Boleta actualizada.")     

def eliminar_venta():
    titulo("ELIMINAR VENTA")
    if len(ventas)==0:
        print("No existen ventas.")
        pausa()
        return
    boleta = validar_texto("Ingrese boleta: ").upper()
    posicion = buscar_boleta(boleta)

    if posicion==-1:
        print("Boleta inexistente.")
        pausa()
        return
    respuesta = input("¿Eliminar la venta? (S/N): ").upper()

    if respuesta=="S":
        eliminar_detalle(boleta)
        ventas.pop(posicion)
        print()
        print("Venta eliminada correctamente.")

    else:
        print()
        print("Operación cancelada.")

    pausa()

def mostrar_ventas():
    titulo("VENTAS REGISTRADAS")
    if len(ventas) == 0:
        print("No existen ventas.")
        pausa()
        return

    print("{:<10}{:<30}{:>15}".format("Boleta","Cliente","Total"))
    print("-" * 60)
    totalGeneral = 0

    for venta in ventas:
        print("{:<10}{:<30}{:>15.2f}".format(venta[0],venta[1],venta[2]))
        totalGeneral += venta[2]

    print("-" * 60)
    print("{:<40}{:>15.2f}".format("TOTAL GENERAL",totalGeneral))

    pausa()

def reporte_general():
    titulo("REPORTE GENERAL DE VENTAS")
    if len(ventas) == 0:
        print("No existen ventas.")
        pausa()
        return

    totalBoletas = len(ventas)
    totalProductos = 0
    ingresoTotal = 0
    print("{:<10}{:<25}{:>15}".format("Boleta","Cliente","Importe"))
    print("-"*55)
    for venta in ventas:
        print("{:<10}{:<25}{:>15.2f}".format(venta[0],venta[1],venta[2]))
        ingresoTotal += venta[2]

    for detalle in detalleVentas:
        totalProductos += detalle[2]

    print("-"*55)
    print()
    print("Boletas emitidas :", totalBoletas)
    print("Productos vendidos :", totalProductos)
    print("Ingreso total : S/",round(ingresoTotal,2))
    pausa()

def indicadores():
    titulo("INDICADORES")
    if len(ventas)==0:
        print("No existen ventas.")
        pausa()
        return

    ingreso = 0
    mayor = ventas[0][2]
    menor = ventas[0][2]
    clienteMayor = ventas[0][1]
    clienteMenor = ventas[0][1]

    for venta in ventas:
        ingreso += venta[2]
        if venta[2] > mayor:
            mayor = venta[2]
            clienteMayor = venta[1]
        if venta[2] < menor:
            menor = venta[2]
            clienteMenor = venta[1]
    promedio = ingreso / len(ventas)

    print()
    print("Ventas registradas :",len(ventas))
    print("Ingreso total : S/",round(ingreso,2))
    print("Venta promedio : S/",round(promedio,2))
    print()
    print("Mayor compra")
    print(clienteMayor)
    print("S/",round(mayor,2))
    print()
    print("Menor compra")
    print(clienteMenor)
    print("S/",round(menor,2))
    pausa()
    
def menu():
    while True:
        limpiar()
        print("=" * 60)
        print("      FERRETERÍA MACKLENA S.A.")
        print("      SISTEMA DE GESTIÓN DE VENTAS")
        print("=" * 60)

        print("1. Registrar venta")
        print("2. Mostrar ventas")
        print("3. Modificar venta")
        print("4. Eliminar venta")
        print("5. Reporte general")
        print("6. Indicadores")
        print("7. Salir")

        print("=" * 60)
        opcion = validar_entero("Seleccione una opción: ")
        if opcion == 1:
            registrar_venta()
        elif opcion == 2:
            mostrar_ventas()
        elif opcion == 3:
            modificar_venta()
        elif opcion == 4:
            eliminar_venta()
        elif opcion == 5:
            reporte_general()
        elif opcion == 6:
            indicadores()
        elif opcion == 7:
            print("\nGracias por utilizar el Sistema de Ventas.")
            break
        else:
            print("\nOpción incorrecta.")
            pausa()

menu()