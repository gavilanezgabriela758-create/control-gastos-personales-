# =========================================================
# SISTEMA DE CONTROL DE GASTOS PERSONALES
# Autor: Dayana Gabriela Gavilanez Monteros
# =========================================================

def mostrar_menu():
    print("\n--- SISTEMA DE CONTROL DE GASTOS PERSONALES ---")
    print("1. Registrar Ingreso")
    print("2. Registrar Gasto")
    print("3. Ver Resumen Financiero")
    print("4. Ver Historial de Movimientos")
    print("5. Salir")

def calcular_resumen(ingresos, gastos):
    total_ingresos = sum(ingresos)
    total_gastos = sum(gastos)
    saldo_actual = total_ingresos - total_gastos
    return total_ingresos, total_gastos, saldo_actual

def main():
    ingresos = []
    gastos = []
    historial = []
    monto_limite_alerta = 500.0

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            try:
                monto = float(input("Ingrese el monto del ingreso: $"))
                if monto > 0:
                    ingresos.append(monto)
                    historial.append(f"Ingreso: +${monto:.2f}")
                    print("¡Ingreso registrado con éxito!")
                else:
                    print("El monto debe ser mayor a 0.")
            except ValueError:
                print("Error: Ingrese un número válido.")

        elif opcion == '2':
            try:
                monto = float(input("Ingrese el monto del gasto: $"))
                categoria = input("Ingrese la categoría (ej. Alimentación, Transporte, Salud): ")
                if monto > 0:
                    gastos.append(monto)
                    historial.append(f"Gasto ({categoria}): -${monto:.2f}")
                    print("¡Gasto registrado con éxito!")
                    if monto >= monto_limite_alerta:
                        print(f"⚠️ ADVERTENCIA: Has registrado un gasto elevado que supera el umbral de ${monto_limite_alerta:.2f}.")
                else:
                    print("El monto debe ser mayor a 0.")
            except ValueError:
                print("Error: Ingrese un número válido.")

        elif opcion == '3':
            tot_ing, tot_gas, saldo = calcular_resumen(ingresos, gastos)
            print("\n--- RESUMEN FINANCIERO ---")
            print(f"Total Ingresos: ${tot_ing:.2f}")
            print(f"Total Gastos:   ${tot_gas:.2f}")
            print(f"Saldo Actual:   ${saldo:.2f}")
            if saldo < 0:
                print("⚠️ ATENCIÓN: Tus gastos superan tus ingresos.")
            elif saldo == 0 and tot_ing > 0:
                print("ℹ️ Tu presupuesto está al límite.")
            else:
                print("✅ Tus finanzas están equilibradas.")

        elif opcion == '4':
            print("\n--- HISTORIAL DE MOVIMIENTOS ---")
            if not historial:
                print("No hay movimientos registrados.")
            else:
                for item in historial:
                    print(f"- {item}")

        elif opcion == '5':
            print("Gracias por usar el Sistema de Control de Gastos Personales.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
