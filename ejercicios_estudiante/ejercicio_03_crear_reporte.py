"""
Ejercicio 3 - Crear un reporte simple

Objetivo:
Crear un archivo de texto con un resumen de produccion.
"""

from pathlib import Path


def crear_reporte_simple(total_leche: float, promedio_leche: float, ruta_salida: str) -> None:
    contenido = (
        "REPORTE DE PRODUCCION SIMPLE\n"
        f"Total Leche: {total_leche} litros\n"
        f"Promedio Leche: {promedio_leche} litros\n"
    )
    Path(ruta_salida).write_text(contenido, encoding="utf-8")


if __name__ == "__main__":
    crear_reporte_simple(164, 23.42, "reporte_prueba.txt")
    print("Reporte simple creado.")
