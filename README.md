# 🛠️ Sistema de Gestión para Ferretería Macklena S.A.

Proyecto desarrollado para el curso **Fundamentos de Programación I** de la **Universidad Peruana de Ciencias Aplicadas (UPC)**.

El sistema busca optimizar los procesos de venta y control de inventario de la empresa **Ferretería Macklena S.A.**, automatizando tareas que anteriormente se realizaban de forma manual.

---

# 📌 Objetivo

Desarrollar una aplicación en Python que permita gestionar de manera eficiente los procesos de ventas e inventario, mejorando el control de productos, reduciendo errores en el registro de información y facilitando la toma de decisiones mediante reportes automáticos.

---

# 👥 Integrantes

- Evelyn Gianela Gallardo Silva
- Dalet Remigio Valentin

Curso: Fundamentos de Programación I

Docente: Erick Teodoro Maldonado Cuzcano


---

# 🚀 Funcionalidades

## 🛒 Sistema de Ventas

- Registrar ventas mediante boletas.
- Registrar múltiples productos en una misma venta.
- Calcular subtotales y total automáticamente.
- Buscar ventas por número de boleta.
- Buscar ventas por cliente.
- Modificar ventas.
- Eliminar ventas.
- Mostrar historial de ventas.
- Reportes generales.
- Indicadores de ventas.

---

## 📦 Sistema de Inventario

- Registrar productos.
- Buscar productos.
- Modificar productos.
- Eliminar productos.
- Auditoría automática de inventario.
- Detección de productos con stock crítico.
- Cálculo automático de unidades a reponer.
- Reporte de reposición.
- Estadísticas del inventario.

---

# 🧩 Tecnologías utilizadas

- Python 3
- Visual Studio Code
- Git
- GitHub

---

# 📂 Estructura del proyecto

```
Ferreteria-Macklena
│
├── ventas.py
├── inventario.py
├── README.md
└── docs
    ├── TB1.pdf
    ├── TB2.pdf
    └── Diagramas
```

---

# 🔄 Flujo general del sistema

```
                 Inicio
                    │
        ┌───────────┴───────────┐
        │                       │
 Sistema de Ventas      Sistema de Inventario
        │                       │
Registrar Venta        Registrar Productos
        │                       │
Calcular Totales       Auditoría de Stock
        │                       │
Generar Boleta         Detectar Faltantes
        │                       │
        └───────────┬───────────┘
                    │
             Generación de Reportes
                    │
                    Fin
```

---

# 📖 Historias de Usuario implementadas

### Sistema de Ventas

- US-01 Registrar venta
- US-02 Buscar venta
- US-03 Buscar cliente
- US-04 Modificar venta
- US-05 Eliminar venta
- US-06 Reportes
- US-07 Indicadores

### Sistema de Inventario

- US-08 Registrar productos
- US-09 Buscar productos
- US-10 Validar existencias
- US-11 Validar stock mínimo
- US-12 Detectar quiebre de stock
- US-13 Calcular reposición
- US-14 Generar reporte de compras

---



# 📷 Capturas del proyecto

Se recomienda agregar imágenes de:

- Menú principal de Inventario:
  
<img width="539" height="269" alt="image" src="https://github.com/user-attachments/assets/e83d7806-9888-4511-a824-5b9a6f962ca7" />

- Menú principal de Ventas

<img width="537" height="276" alt="image" src="https://github.com/user-attachments/assets/ab12dbe7-f151-4f5b-8891-020dee32dd16" />



---

# 📄 Licencia

Proyecto desarrollado únicamente con fines académicos para el curso **Fundamentos de Programación I** de la Universidad Peruana de Ciencias Aplicadas (UPC).
