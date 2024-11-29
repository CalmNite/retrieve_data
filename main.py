import csv
import login, assets, devices, edges
import pandas as pd

def menu_principal():
    global token
    ip_puerto = input("Introduce la IP y el puerto de la plataforma sobre la que quieres trabajar (ejemplo: http://217.160.101.174:24587): ")
    while True:
        print(f"\nMenú Principal: estamos trabajando en al siguiente IP: {ip_puerto}")
        print("1. Loguearse en la plataforma")
        print("2. Cambiar de IP")
        print("3. Cargar csv")
        print("5. Salir")
        
        try:
            opcion = int(input("Selecciona una opción (1-4): "))
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número del 1 al 4.")
            continue

        if opcion == 1:
            token = loguearse(ip_puerto)
        elif opcion == 2:
            ip_puerto = input("Introduce la IP y el puerto de la plataforma sobre la que quieres trabajar (ejemplo: http://217.160.101.174:24587): ")
            print("IP actualizada correctamente")
        elif opcion in [3]:
            if token:
                if opcion == 3:
                    cargar_csv(ip_puerto, token)
        elif opcion == 5:
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 4.")

def loguearse(ip_puerto):
    try:
        usuario = input("Introduce tu usuario: ")
        contrasena = input("Introduce tu contraseña: ")

        token = login.login(ip_puerto, usuario, contrasena)
        print("Logueado con éxito.")
        return token

    except Exception as e:
        print(f"Error inesperado: {e}")

def cargar_csv(ip_puerto, token):
    print("\n--- Cargar CSV y Crear Elementos ---")
    
    ruta_csv = input("Introduce el nombre del archivo CSV (debe estar dentro de la carpeta-archivos): ")
    try:
        datos = pd.read_csv(f"./archivos/{ruta_csv}.csv", encoding='utf-8')
        if datos.empty:
            print("El archivo CSV no contiene datos. Operación cancelada.")
            return 
        
        print("\n¿Qué deseas crear a partir del CSV?")
        print("1. Activos")
        print("2. Dispositivos")
        print("3. Edge")
        
        try:
            opcion = int(input("Selecciona una opción (1-3): "))
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número del 1 al 3.")
            return

        if opcion == 1:
            assets.create_assets(ip_puerto, token, datos)
        elif opcion == 2:
            devices.create_devices(ip_puerto, token, datos)
        elif opcion == 3:
            edges.create_edges(ip_puerto, token, datos)
        else:
            print("Opción no válida. Operación cancelada.")
    except FileNotFoundError:
        print("Archivo no encontrado. Por favor, verifica la ruta.")
    except pd.errors.EmptyDataError:
        print("El archivo CSV está vacío. Por favor, verifica el contenido.")
    except pd.errors.ParserError:
        print("Error al procesar el archivo CSV. Asegúrate de que esté correctamente formateado.")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")


if __name__ == "__main__":
    menu_principal()
