"""
Ejercicio 1 - Completar nombre de respaldo

Objetivo:
Crear una funcion que genere un nombre de respaldo con fecha y hora.

Instruccion:
Completa la funcion generar_nombre_respaldo.
"""

from datetime import datetime
from pathlib import Path


def generar_nombre_respaldo(nombre_archivo_original: str) -> str:
    """
    Debe retornar un nombre como:
    respaldo_produccion_finca_2026-05-27_143000.csv
    """
    archivo = Path(nombre_archivo_original)
    marca_tiempo = datetime.now().strftime("%Y-%m-%d_%H%M%S")

    return f"respaldo_{archivo.stem}_{marca_tiempo}{archivo.suffix}"


if __name__ == "__main__":
    resultado = generar_nombre_respaldo("produccion_finca.csv")
    print(resultado)
