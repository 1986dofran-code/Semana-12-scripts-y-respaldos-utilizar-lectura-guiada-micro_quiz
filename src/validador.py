import csv
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

from config import COLUMNAS_OBLIGATORIAS

Registro = Dict[str, object]


def validar_fecha(valor: str) -> bool:
    """Valida que la fecha tenga el formato AAAA-MM-DD."""
    try:
        datetime.strptime(valor, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def leer_y_validar_csv(ruta_archivo: Path) -> Tuple[List[Registro], List[str], List[str]]:
    """
    Lee un archivo CSV y separa los registros validos de los errores.

    Retorna:
        registros_validos: lista de filas listas para procesar.
        errores: lista de errores criticos encontrados.
        advertencias: lista de alertas no criticas.
    """
    registros_validos: List[Registro] = []
    errores: List[str] = []
    advertencias: List[str] = []

    if not ruta_archivo.exists():
        errores.append(f"El archivo no existe: {ruta_archivo}")
        return registros_validos, errores, advertencias

    with ruta_archivo.open("r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)

        columnas = lector.fieldnames or []
        for columna in COLUMNAS_OBLIGATORIAS:
            if columna not in columnas:
                errores.append(f"Falta la columna obligatoria: {columna}")

        if errores:
            return registros_validos, errores, advertencias

        for numero_fila, fila in enumerate(lector, start=2):
            fecha = (fila.get("fecha") or "").strip()
            area = (fila.get("area") or "").strip()
            producto = (fila.get("producto") or "").strip()
            cantidad_texto = (fila.get("cantidad") or "").strip()
            unidad = (fila.get("unidad") or "").strip()
            responsable = (fila.get("responsable") or "").strip()
            observacion = (fila.get("observacion") or "").strip()

            if not fecha or not validar_fecha(fecha):
                errores.append(f"Fila {numero_fila}: fecha invalida o vacia: '{fecha}'")
                continue

            if not area:
                errores.append(f"Fila {numero_fila}: area vacia")
                continue

            if not producto:
                errores.append(f"Fila {numero_fila}: producto vacio")
                continue

            if not unidad:
                errores.append(f"Fila {numero_fila}: unidad vacia")
                continue

            if not cantidad_texto:
                errores.append(f"Fila {numero_fila}: cantidad vacia")
                continue

            try:
                cantidad = float(cantidad_texto)
            except ValueError:
                errores.append(f"Fila {numero_fila}: cantidad no numerica: '{cantidad_texto}'")
                continue

            if cantidad < 0:
                errores.append(f"Fila {numero_fila}: cantidad negativa no permitida: {cantidad}")
                continue

            if cantidad == 0:
                advertencias.append(f"Fila {numero_fila}: cantidad igual a cero para {producto}")

            registros_validos.append(
                {
                    "fecha": fecha,
                    "area": area,
                    "producto": producto.lower(),
                    "cantidad": cantidad,
                    "unidad": unidad,
                    "responsable": responsable,
                    "observacion": observacion,
                }
            )

    return registros_validos, errores, advertencias
