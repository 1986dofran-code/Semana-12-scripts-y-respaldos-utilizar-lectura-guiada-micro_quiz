from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUTS_DIR = BASE_DIR / "outputs"
REPORTES_DIR = OUTPUTS_DIR / "reportes"
RESPALDOS_DIR = OUTPUTS_DIR / "respaldos"
LOGS_DIR = BASE_DIR / "logs"

DATA_FILE = DATA_DIR / "produccion_finca.csv"
LOG_FILE = LOGS_DIR / "ejecucion.log"

COLUMNAS_OBLIGATORIAS = [
    "fecha",
    "area",
    "producto",
    "cantidad",
    "unidad",
    "responsable",
    "observacion",
]
