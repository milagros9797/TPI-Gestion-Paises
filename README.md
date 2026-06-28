Universidad Tecnologica Nacional (UTN)
Tecnicatura Universitaria en Programacion - Modalidad a Distancia
Materia: Programacion 1
Año: 2026

## Docentes
Martin Alejandro Garcia
## Tutor
Virginia Cimino

TPI - Gestión de Datos de Países en Python

## Descripción
Aplicación en Python que permite gestionar información sobre países. Lee datos desde un archivo CSV y ofrece un menú en consola para realizar búsquedas, filtros, ordenamientos y estadísticas.

## Integrantes
Milagros Herrera

## Requisitos
Python 3.x
Archivo paises.csv en la misma carpeta que el script

## Como ejecutar
1. Clona el repositorio
2. Asegurate de que el archivo paises.csv este en la misma carpeta que gestion_paises.py
3. Abri una terminal y ejecuta: python gestion_paises.py

## Funcionalidades
-Agregar, actualizar y buscar países.
-Filtrar por continente, rango de población o superficie.
-Ordenar por nombre, población o superficie (ascendente o descendente).
-Estadísticas: país con mayor/menor población, promedios y cantidad por continente.

## Ejemplo de uso
Al ejecutar el programa aparece un menu con opciones:

========================================
   GESTION DE DATOS DE PAISES
========================================
1. Agregar pais
2. Actualizar pais
3. Buscar pais por nombre
4. Filtrar por continente
5. Filtrar por rango de poblacion
6. Filtrar por rango de superficie
7. Ordenar paises
8. Mostrar estadisticas
9. Mostrar todos los paises
0. Salir
========================================

- Opcion 1: pide nombre, poblacion, superficie y continente para agregar un nuevo pais
- Opcion 2: permite modificar la poblacion y superficie de un pais existente
- Opcion 3: busca un pais por nombre exacto o parcial
- Opcion 4: muestra todos los paises de un continente
- Opcion 5: filtra paises dentro de un rango de poblacion
- Opcion 6: filtra paises dentro de un rango de superficie
- Opcion 7: ordena los paises por nombre, poblacion o superficie
- Opcion 8: muestra estadisticas generales como promedios y extremos
- Opcion 9: lista todos los paises cargados
- Opcion 0: cierra el programa

## Estructura del proyecto
- gestion_paises.py - codigo principal del programa
- paises.csv - dataset base con informacion de paises
- README.md - documentacion del proyecto
