# SGFS – Sistema de Gestión Financiera Simple

SGFS es un proyecto personal desarrollado en Python con el objetivo de practicar programación aplicada a Administración y Finanzas.

La idea principal fue construir un sistema sencillo pero funcional que permita registrar transacciones y obtener información financiera básica sin usar librerías externas ni bases de datos, solo lógica y estructuras básicas de Python.

---

## ¿Qué hace el sistema?

El programa funciona por consola y tiene un menú interactivo que permite:

1. **Registrar transacciones**
   - Fecha (DD/MM/AA)
   - Monto
   - Tipo de transacción (Ingreso o Egreso)
   - Descripción

2. **Ver un resumen financiero**
   - Total de ingresos
   - Total de egresos
   - Resultado neto
   - Cantidad de transacciones registradas
   - Listado completo de las transacciones

3. **Ver el flujo de caja por mes**
   - Ingresos del mes
   - Egresos del mes
   - Flujo neto del mes seleccionado

4. **Buscar transacciones**
   - Búsqueda por palabra clave
   - La búsqueda se realiza únicamente sobre la descripción
   - No distingue entre mayúsculas y minúsculas

5. **Salir del sistema**
   - El menú permite ejecutar varias operaciones sin reiniciar el programa

---

## Cómo se usa

1. Tener Python 3 instalado.
2. Ejecutar el archivo principal:

```bash
python main.py
