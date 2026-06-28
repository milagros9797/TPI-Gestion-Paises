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

# FUNCIONES DE GESTIÓN

def agregar_pais(paises):
    """Agrega un nuevo país a la lista."""
    print("\n--- AGREGAR PAÍS ---")
    nombre = input("Nombre del país: ").strip()
    if not nombre:
        print("Error: el nombre no puede estar vacío.")
        return

    for p in paises:
        if p["nombre"].lower() == nombre.lower():
            print("Error: ese país ya existe.")
            return

    try:
        poblacion = int(input("Población: "))
        superficie = int(input("Superficie en km²: "))
    except ValueError:
        print("Error: población y superficie deben ser números enteros.")
        return

    continente = input("Continente: ").strip()
    if not continente:
        print("Error: el continente no puede estar vacío.")
        return

    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    paises.append(pais)
    guardar_paises(paises)
    print(f"País '{nombre}' agregado correctamente.")


def actualizar_pais(paises):
    """Actualiza población y superficie de un país existente."""
    print("\n--- ACTUALIZAR PAÍS ---")
    nombre = input("Nombre del país a actualizar: ").strip()
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            try:
                pais["poblacion"] = int(input(f"Nueva población (actual: {pais['poblacion']}): "))
                pais["superficie"] = int(input(f"Nueva superficie (actual: {pais['superficie']}): "))
                guardar_paises(paises)
                print("País actualizado correctamente.")
            except ValueError:
                print("Error: ingresá valores numéricos válidos.")
            return
    print("País no encontrado.")


def buscar_pais(paises):
    """Busca un país por nombre (parcial o exacto)."""
    print("\n--- BUSCAR PAÍS ---")
    nombre = input("Ingresá el nombre (o parte del nombre): ").strip().lower()
    resultados = [p for p in paises if nombre in p["nombre"].lower()]
    if resultados:
        for p in resultados:
            mostrar_pais(p)
    else:
        print("No se encontraron países con ese nombre.")

# FUNCIONES DE FILTRO

def filtrar_por_continente(paises):
    """Filtra países por continente."""
    print("\n--- FILTRAR POR CONTINENTE ---")
    continente = input("Ingresá el continente: ").strip().lower()
    resultados = [p for p in paises if p["continente"].lower() == continente]
    if resultados:
        for p in resultados:
            mostrar_pais(p)
    else:
        print("No se encontraron países en ese continente.")


def filtrar_por_poblacion(paises):
    """Filtra países por rango de población."""
    print("\n--- FILTRAR POR RANGO DE POBLACIÓN ---")
    try:
        minimo = int(input("Población mínima: "))
        maximo = int(input("Población máxima: "))
        resultados = [p for p in paises if minimo <= p["poblacion"] <= maximo]
        if resultados:
            for p in resultados:
                mostrar_pais(p)
        else:
            print("No se encontraron países en ese rango.")
    except ValueError:
        print("Error: ingresá valores numéricos válidos.")


def filtrar_por_superficie(paises):
    """Filtra países por rango de superficie."""
    print("\n--- FILTRAR POR RANGO DE SUPERFICIE ---")
    try:
        minimo = int(input("Superficie mínima (km²): "))
        maximo = int(input("Superficie máxima (km²): "))
        resultados = [p for p in paises if minimo <= p["superficie"] <= maximo]
        if resultados:
            for p in resultados:
                mostrar_pais(p)
        else:
            print("No se encontraron países en ese rango.")
    except ValueError:
        print("Error: ingresá valores numéricos válidos.")
