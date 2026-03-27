# Archivo principal del proyecto SGFS

# Listas para almacenamiento de transacciones
Fechas = []
Monto = []
Tipo = []
Descripcion = []

while True:
    # Menú de opciones para el usuario
    print("=== SGFS - Sistema de Gestión Financiera Simple ===")

    print("1) Registrar transacción")
    print("2) Ver resumen financiero")
    print("3) Ver flujo de caja del mes")
    print("4) Buscar transacciones")
    print("5) Salir")

    # CTA al usuario
    print("Elegí una opción")
    opcion = int(input())

    # Pedir datos al usuario según la opción elegida
    if opcion == 1:
        print("Escogiste registrar una transacción")
        fecha_ingresada = input("Ingrese la fecha de la transaccion (DD/MM/AA): ")
        monto_ingresado = int(input("Ingrese el monto de la transacción: "))
        tipo_ingresado = input("Ingrese el tipo de transacción (Ingreso/Egreso): ")
        descripcion_ingresada = input("Glosa de la transacción: ")
        # Agregar los datos a las listas correspondientes
        Fechas.append(fecha_ingresada)
        Monto.append(monto_ingresado)
        Tipo.append(tipo_ingresado)
        Descripcion.append(descripcion_ingresada)
        print("Transacción registrada con éxito.")

    # Resumen financiero    
    elif opcion == 2:
        print("Escogiste ver el resumen financiero")
        total_ingresos = 0
        for i in range(len(Tipo)):
            if Tipo[i] == "Ingreso":
                total_ingresos += Monto[i]

        print("Total de ingresos:", total_ingresos)

        total_egresos = 0
        for i in range(len(Tipo)):
            if Tipo[i] == "Egreso":
                total_egresos += Monto[i]

        print("Total de egresos: ", total_egresos)

        saldo_final = total_ingresos - total_egresos
        print("Saldo final: ", saldo_final)

        cantidad_transacciones = len(Monto)
        print("Cantidad de transacciones: ", cantidad_transacciones)

    elif opcion == 3:
        print("Escogiste ver el flujo de caja mensual")
        mes = (input("Ingrese el mes para el cual desea ver el flujo de caja (MM): "))

        ingresos_mes = 0 
        egresos_mes = 0

        for i in range(len(Fechas)):
            if mes in Fechas[i]:
                if Tipo[i] == "Ingreso":
                    ingresos_mes += Monto[i]
                elif Tipo[i] == "Egreso":
                    egresos_mes += Monto[i]
        
        print("Ingresos del mes: ", ingresos_mes)
        print("Egresos del mes: ", egresos_mes)
        print("Flujo de caja del mes: ", ingresos_mes - egresos_mes)

    elif opcion == 4:
        print("Escogiste buscar transacciones")
        key_word = input("Ingrese la palabra clave: ").lower()

        encontradas = False

        for i in range(len(Descripcion)):
            if key_word in Descripcion[i].lower():
                print("Palabra clave encontrada en la transacción: ")
                print("Fecha: ", Fechas[i])
                print("Monto: ", Monto[i])
                print("Tipo: ", Tipo[i])
                print("Descripción: ", Descripcion[i])
                encontradas = True

        if not encontradas:
                 print("No se encontraron transacciones con la palabra clave ingresada.")


    elif opcion == 5:
        print("Saliendo del sistema")
        break

    respuestaContinuacion = input("Presiona Enter para elegir una nueva opción o presiona 5 para salir")

    if respuestaContinuacion == "5":
        print("Saliendo del sistema")
        break
