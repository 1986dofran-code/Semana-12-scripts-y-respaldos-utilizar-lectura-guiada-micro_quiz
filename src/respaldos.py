from datetime import datetime
from pathlib import Path
import shutil


def crear_respaldo(ruta_origen: Path, carpeta_respaldos: Path) -> Path:
    """
    Crea una copia de seguridad del archivo de datos.

    El respaldo incluye fecha y hora para evitar sobrescribir respaldos anteriores.
    """
    if not ruta_origen.exists():
        raise FileNotFoundError(f"No se puede respaldar un archivo inexistente: {ruta_origen}")

    carpeta_respaldos.mkdir(parents=True, exist_ok=True)
    marca_tiempo = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    nombre_respaldo = f"respaldo_{ruta_origen.stem}_{marca_tiempo}{ruta_origen.suffix}"
    ruta_destino = carpeta_respaldos / nombre_respaldo
    shutil.copy2(ruta_origen, ruta_destino)
    return ruta_destino
