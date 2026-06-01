from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

from config import UMBRAL_BAJA_PRODUCCION, UMBRAL_ALTA_PRODUCCION

Registro = Dict[str, object]


def agrupar_por_producto(registros: List[Registro]) -> Dict[str, List[Registro]]:
    """Agrupa los registros por producto."""
    grupos: Dict[str, List[Registro]] = defaultdict(list)
    for registro in registros:
        grupos[str(registro["producto"])].append(registro)
    return dict(grupos)


def calcular_indicadores(registros: List[Registro]) -> Dict[str, object]:
    """Calcula indicadores principales para un conjunto de registros."""
    if not registros:
        return {
            "total": 0,
            "promedio": 0,
            "maximo": None,
            "minimo": None,
            "cantidad_registros": 0,
            "unidad": "",
        }

    cantidades = [float(registro["cantidad"]) for registro in registros]
    total = sum(cantidades)
    promedio = total / len(cantidades)
    maximo = max(registros, key=lambda registro: float(registro["cantidad"]))
    minimo = min(registros, key=lambda registro: float(registro["cantidad"]))

    return {
        "total": total,
        "promedio": promedio,
        "maximo": maximo,
        "minimo": minimo,
        "cantidad_registros": len(registros),
        "unidad": registros[0]["unidad"],
    }


def crear_alertas(producto: str, indicadores: Dict[str, object]) -> List[str]:
    """Genera alertas sencillas segun el comportamiento de los datos."""
    alertas: List[str] = []
    promedio = float(indicadores["promedio"])
    minimo = indicadores["minimo"]
    maximo = indicadores["maximo"]

    if minimo and promedio > 0:
        cantidad_minima = float(minimo["cantidad"])
        if cantidad_minima < promedio * 0.85:
        if cantidad_minima < (promedio * UMBRAL_BAJA_PRODUCCION):
            alertas.append(
                f"Alerta: {producto} tuvo una produccion baja el dia {minimo['fecha']} "
                f"({cantidad_minima:.2f} {indicadores['unidad']})."
            )

    if maximo and promedio > 0:
        cantidad_maxima = float(maximo["cantidad"])
        if cantidad_maxima > promedio * 1.15:
        if cantidad_maxima > (promedio * UMBRAL_ALTA_PRODUCCION):
            alertas.append(
                f"Observacion: {producto} tuvo una produccion alta el dia {maximo['fecha']} "
                f"({cantidad_maxima:.2f} {indicadores['unidad']})."
            )

    return alertas


def generar_texto_reporte(registros: List[Registro], errores: List[str], advertencias: List[str]) -> str:
    """Crea el contenido textual del reporte semanal."""
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lineas: List[str] = []

    lineas.append("REPORTE SEMANAL DE PRODUCCION RURAL")
    lineas.append("=" * 48)
    lineas.append(f"Fecha de generacion: {ahora}")
    lineas.append(f"Registros validos procesados: {len(registros)}")
    lineas.append("")

    if not registros:
        lineas.append("No hay registros validos para procesar.")
    else:
        grupos = agrupar_por_producto(registros)
        for producto, datos_producto in sorted(grupos.items()):
            indicadores = calcular_indicadores(datos_producto)
            maximo = indicadores["maximo"]
            minimo = indicadores["minimo"]
            unidad = indicadores["unidad"]

            lineas.append(f"PRODUCTO: {producto.upper()}")
            lineas.append("-" * 48)
            lineas.append(f"Total semanal: {indicadores['total']:.2f} {unidad}")
            lineas.append(f"Promedio por registro: {indicadores['promedio']:.2f} {unidad}")
            lineas.append(f"Cantidad de registros: {indicadores['cantidad_registros']}")

            if maximo:
                lineas.append(
                    f"Mayor produccion: {maximo['fecha']} - {float(maximo['cantidad']):.2f} {unidad} "
                    f"/ Responsable: {maximo['responsable']}"
                )

            if minimo:
                lineas.append(
                    f"Menor produccion: {minimo['fecha']} - {float(minimo['cantidad']):.2f} {unidad} "
                    f"/ Responsable: {minimo['responsable']}"
                )

            alertas = crear_alertas(producto, indicadores)
            if alertas:
                lineas.append("Alertas y observaciones:")
                for alerta in alertas:
                    lineas.append(f"  - {alerta}")
            else:
                lineas.append("Alertas y observaciones: sin alertas relevantes.")

            lineas.append("")

    lineas.append("ERRORES DETECTADOS")
    lineas.append("-" * 48)
    if errores:
        for error in errores:
            lineas.append(f"- {error}")
    else:
        lineas.append("No se detectaron errores criticos.")
    lineas.append("")

    lineas.append("ADVERTENCIAS")
    lineas.append("-" * 48)
    if advertencias:
        for advertencia in advertencias:
            lineas.append(f"- {advertencia}")
    else:
        lineas.append("No se detectaron advertencias.")
    lineas.append("")

    lineas.append("INTERPRETACION")
    lineas.append("-" * 48)
    lineas.append(
        "Este reporte permite revisar la produccion semanal, detectar variaciones "
        "y conservar evidencia organizada para la toma de decisiones."
    )

    return "\n".join(lineas)


def guardar_reporte(texto: str, carpeta_reportes: Path) -> Path:
    """Guarda el reporte en la carpeta de salida."""
    carpeta_reportes.mkdir(parents=True, exist_ok=True)
    marca_tiempo = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    ruta_reporte = carpeta_reportes / f"reporte_semanal_{marca_tiempo}.txt"
    ruta_reporte.write_text(texto, encoding="utf-8")
    return ruta_reporte
