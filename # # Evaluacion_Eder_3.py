# # Evaluacion_Eder_3
# Desarrolle una aplicación en Python utilizando Visual Studio que permita resolver el siguiente caso:
# El Servicio Nacional del Consumidor (SERNAC), está probando una forma simplificada para registrar y gestionar los
# reclamos de los consumidores. Para ello utiliza solo cuatro campos de información:
# ° RUT: Rut del reclamante, con DV.
# ° Fecha: Fecha del reclamo en formato dd-mm-yyyy HH:MM:SS
# ° Monto: Valor de la compra en miles de pesos.
# ° Reclamo: Reseña del reclamo en texto libre, de no más de veinte caracteres.
# Y considera las siguientes funcionalidades:
# 1. Registrar Reclamo
# 2. Listar Reclamos
# 3. Respaldar Reclamos
# 4. Salir
# Registrar Reclamo: Permite ingresar RUT, Monto y Reclamo
# Listar Reclamos: Se usa para mostrar todos los reclamos ingresados, incluyendo la fecha
# Respaldar Reclamos: Genera un respaldo en archivo de todos los reclamos ingresados en formato CSV.
# El programa debe funcionar hasta que el usuario decida finalizar el programa.
from datetime import datetime
import csv



def registrar(reclamos):
        rut = input("Ingrese el RUT sin puntos ni guion: ")
        fecha = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        monto = int(input("Ingrese el monto de la compra a reclamar: "))
        while True:
            reclamo = input("Ingrese una breve descripcion del reclamo (no mas de 20 caracteres): ",)
            if len(reclamo) <= 20:
                break
            else:
                print("Ha excedido el limite de caracteres favor intente nuevamente")
        try:
            fecha = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            reclamos.append({
                'RUT': rut,
                'Fecha': fecha,
                'Monto': monto,
                'Reclamo': reclamo
            })
            print("Reclamo registrado correctamente.")
        except ValueError:
            print("Error al ingresar la fecha. Asegúrese de ingresar en el formato correcto.")

def listar(reclamos):
    if not reclamos:
        print("No existe registros de reclamos.")
    else:
        print("\n Listado de Reclamos:")
        for i, reclamo in enumerate(reclamos, start=1):
            print(f"{i}. RUT: {reclamo['RUT']}, Fecha: {reclamo['Fecha']}, Monto: {reclamo['Monto']}, Reclamo: {reclamo['Reclamo']}")       

    
def respaldar(reclamos):
    if not reclamos:
        print("No existen reclamos para respaldar.")
        return
    
    archivo_csv = input("Ingrese el nombre del archivo CSV para respaldar ejemplo ingrese sin la extension .CSV (base de datos): ")

    archivo_csv += ".csv"

    try:
        with open(archivo_csv, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['RUT', 'Fecha', 'Monto', 'Reclamo'])
            for reclamo in reclamos:
                writer.writerow([reclamo['RUT'], reclamo['Fecha'], reclamo['Monto'], reclamo['Reclamo']])
        print(f"Reclamos han sido respaldados en '{archivo_csv}' de manera correcta.")
    except ValueError:
        print(f"Se ha producido un error al intentar escribir en el archivo '{archivo_csv}'. intente nuevamente")


def main():
    reclamos = []
    
    while True:
        print("-----------------------------------------")
        print("\n SERNAC - Sistema de Reclamos ")
        print("1. Registrar Reclamo")
        print("2. Listar Reclamos")
        print("3. Respaldar Reclamos")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): \n ")

        if opcion == '1':
            print("Ha seleccionado Registrar Reclamo")
            print("--------------------------------")
            registrar(reclamos)
        elif opcion == '2':
            listar(reclamos)
        elif opcion == '3':
            respaldar(reclamos)
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no valida. Por favor, ingrese una opción del 1 al 4.")

if __name__ == "__main__":
    main()
