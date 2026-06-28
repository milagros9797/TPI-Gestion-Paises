# TPI - Gestión de Datos de Países en Python
# Programación 1 - UTN TUP
# Alumna: Milagros Herrera

import csv

ARCHIVO_CSV = "paises.csv"

# FUNCIONES DE ARCHIVO

def cargar_paises():
    """Lee el archivo CSV y devuelve una lista de diccionarios."""
    paises = []
    try:
        with open(ARCHIVO_CSV, newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip()
                    }
                    paises.append(pais)
                except (ValueError, KeyError):
                    print(f"Fila con formato incorrecto ignorada: {fila}")
    except FileNotFoundError:
        print("Archivo CSV no encontrado. Se iniciará con lista vacía.")
    return paises


def guardar_paises(paises):
    """Guarda la lista de países en el archivo CSV."""
    with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for pais in paises:
            escritor.writerow(pais)
    print("Datos guardados correctamente.")
