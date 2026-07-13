# ============================================================
#  FERRETERÍA MACKLENA S.A.
#  Módulo: Sistema de Auditoría y Control de Inventario
#  Integrante: Remigio Valentín, Dalet
#  Curso: Fundamentos de Programación 1 — 1FIS0274
#  Ciclo: 2026-15 | TB2
#  US cubiertos: US-08, US-09, US-10, US-11, US-12, US-13, US-14
# ============================================================

def mostrar_encabezado():
    print("=" * 62)
    print("     FERRETERÍA MACKLENA S.A.")
    print("     Sistema de Auditoría y Control de Inventario")
    print("=" * 62)

def ingresar_entero_positivo(mensaje):
    """Solicita un número entero mayor a cero con validación de bucle."""
    while True:
        entrada = input(mensaje).strip()
        if entrada.isdigit() and int(entrada) > 0:
            return int(entrada)
        print("  ⚠ Ingrese un número entero mayor a cero.\n")

def ingresar_stock(mensaje):
    """
    Solicita un valor de stock (entero >= 0).
    US-10: rechaza valores negativos.
    US-11: valida que sea un número lógico.
    """
    while True:
        try:
            valor = int(input(mensaje).strip())
            if valor >= 0:
                return valor
            # US-10 / US-11: valores negativos son filtrados
            print("  ⚠ El stock no puede ser negativo. Intente nuevamente.\n")
        except ValueError:
            print("  ⚠ Valor inválido. Ingrese un número entero (ej: 15).\n")

def ingresar_codigo(mensaje):
    """US-09: solicita código alfanumérico no vacío."""
    while True:
        codigo = input(mensaje).strip().upper()
        if codigo:
            return codigo
        print("  ⚠ El código no puede estar vacío.\n")

def auditar_producto(numero):
    """
    Captura los datos de un producto y evalúa su estado de stock.
    Retorna dict con resultado del análisis.
    """
    print(f"\n  {'─'*58}")
    print(f"  PRODUCTO {numero}")
    print(f"  {'─'*58}")

    # US-09: código alfanumérico del artículo
    codigo = ingresar_codigo("  Código del producto (ej: FER-042): ")

    while True:
        nombre = input("  Nombre del producto             : ").strip()
        if nombre:
            break
        print("  ⚠ El nombre no puede estar vacío.\n")

    # US-10 / US-11: validación de stock actual y mínimo
    stock_actual  = ingresar_stock("  Stock actual en almacén (unid.) : ")
    stock_minimo  = ingresar_stock("  Stock mínimo de seguridad       : ")

    # US-12: comparación automática de existencias vs límite mínimo
    en_alerta = stock_actual < stock_minimo

    unidades_a_pedir = 0
    if en_alerta:
        # US-13: cálculo matemático de unidades faltantes
        unidades_a_pedir = stock_minimo - stock_actual
        print(f"\n  ⚠ ALERTA — Stock crítico detectado.")
        print(f"     Stock actual  : {stock_actual} unid.")
        print(f"     Stock mínimo  : {stock_minimo} unid.")
        print(f"     A reponer     : {unidades_a_pedir} unid.")
    else:
        print(f"\n  ✔ Stock óptimo ({stock_actual} unid. / mín. {stock_minimo} unid.)")

    return {
        "numero"          : numero,
        "codigo"          : codigo,
        "nombre"          : nombre,
        "stock_actual"    : stock_actual,
        "stock_minimo"    : stock_minimo,
        "en_alerta"       : en_alerta,
        "unidades_pedir"  : unidades_a_pedir
    }

def generar_reporte(productos, total_alertas, total_unidades):
    """
    US-14: Visualiza reporte detallado de artículos en crisis
    con cantidad exacta sugerida por proveedor.
    """
    print("\n")
    print("=" * 62)
    print("     REPORTE DE AUDITORÍA DE INVENTARIO")
    print("     Ferretería Macklena S.A.")
    print("=" * 62)
    print(f"  Total de productos evaluados : {len(productos)}")
    print(f"  Total de alertas de stock    : {total_alertas}")
    # US-13: total acumulado de unidades a pedir
    print(f"  Total unidades a reabastecer : {total_unidades} unid.")
    print()

    if total_alertas == 0:
        print("  ✔ Todos los productos tienen stock suficiente.")
    else:
        # US-14: lista detallada de artículos en crisis
        print(f"  {'─'*58}")
        print("  LISTA DE COMPRAS URGENTES — Artículos desabastecidos")
        print(f"  {'─'*58}")
        print(f"  {'N°':<5} {'Código':<12} {'Producto':<22} "
              f"{'Act':>5} {'Mín':>5} {'Pedir':>7}")
        print(f"  {'─'*5} {'─'*12} {'─'*22} {'─'*5} {'─'*5} {'─'*7}")

        # US-14: recorre solo productos en alerta (bucle for sobre la lista)
        contador = 1
        for p in productos:
            if p["en_alerta"]:
                print(f"  {contador:<5} {p['codigo']:<12} {p['nombre']:<22} "
                      f"{p['stock_actual']:>5} {p['stock_minimo']:>5} "
                      f"{p['unidades_pedir']:>6} u.")
                contador += 1

        print(f"  {'─'*58}")
        print(f"\n  → Orden de reabastecimiento lista para envío al proveedor.")

    print("=" * 62)
    print("  Auditoría finalizada correctamente.")
    print("=" * 62)

def main():
    mostrar_encabezado()
    print("\nBienvenido al sistema de auditoría de inventario.\n")

    # US-08: el encargado define cuántos productos va a revisar en el ciclo
    n_productos = ingresar_entero_positivo(
        "Ingrese la cantidad total de productos a evaluar: "
    )

    productos       = []    # US-08: lista de productos evaluados
    total_alertas   = 0     # contador de alertas detectadas
    total_unidades  = 0     # US-13: acumulador de unidades a pedir

    # US-08: bucle while — revisa cada producto secuencialmente
    i = 1
    while i <= n_productos:
        resultado = auditar_producto(i)
        productos.append(resultado)

        # US-12: acumula alertas detectadas
        if resultado["en_alerta"]:
            total_alertas  += 1
            # US-13: acumula unidades totales a reponer
            total_unidades += resultado["unidades_pedir"]

        i += 1

    # US-14: genera el reporte final con todos los artículos en crisis
    generar_reporte(productos, total_alertas, total_unidades)

if __name__ == "__main__":
    main()