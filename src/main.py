import argparse
from datetime import datetime
from pathlib import Path
import sys

# Permite importar archivos ubicados en src cuando se ejecuta desde la raiz del proyecto.
sys.path.append(str(Path(__file__).resolve().parent))

from config import DATA_FILE, LOG_FILE, REPORTES_DIR, RESPALDOS_DIR, LOGS_DIR
from reportes import generar_texto_reporte, guardar_reporte
from respaldos import crear_respaldo
from validador import leer_y_validar_csv


def registrar_log(mensaje: str) -> None:
    """Agrega mensajes a una bitacora de ejecucion."""
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with LOG_FILE.open("a", encoding="utf-8") as log:
        log.write(f"[{fecha}] {mensaje}\n")


def construir_argumentos() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Genera reporte semanal y respaldo de datos de produccion rural."
    )
    parser.add_argument(
        "--data",
        default=str(DATA_FILE),
        help="Ruta del archivo CSV que contiene los datos de produccion.",
    )
    return parser.parse_args()


def main() -> None:
    args = construir_argumentos()
    ruta_datos = Path(args.data)

    registrar_log(f"Inicio de ejecucion con archivo: {ruta_datos}")

    registros, errores, advertencias = leer_y_validar_csv(ruta_datos)
    texto_reporte = generar_texto_reporte(registros, errores, advertencias)
    ruta_reporte = guardar_reporte(texto_reporte, REPORTES_DIR)

    try:
        ruta_respaldo = crear_respaldo(ruta_datos, RESPALDOS_DIR)
        mensaje_respaldo = f"Respaldo creado: {ruta_respaldo}"
    except FileNotFoundError as error:
        ruta_respaldo = None
        mensaje_respaldo = f"No se pudo crear respaldo: {error}"

    registrar_log(f"Registros validos: {len(registros)}")
    registrar_log(f"Errores detectados: {len(errores)}")
    registrar_log(f"Advertencias detectadas: {len(advertencias)}")
    registrar_log(f"Reporte creado: {ruta_reporte}")
    registrar_log(mensaje_respaldo)
    registrar_log("Fin de ejecucion")

    print("Proceso completado.")
    print(f"Registros validos procesados: {len(registros)}")
    print(f"Errores detectados: {len(errores)}")
    print(f"Advertencias detectadas: {len(advertencias)}")
    print(f"Reporte generado en: {ruta_reporte}")
    print(mensaje_respaldo)
    print(f"Bitacora actualizada en: {LOG_FILE}")

    if errores:
        print("\nAlgunos registros tenian errores. Revisa el reporte generado para ver el detalle.")


if __name__ == "__main__":
    main()
