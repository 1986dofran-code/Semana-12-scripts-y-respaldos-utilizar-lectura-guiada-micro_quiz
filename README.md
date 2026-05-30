# Semana 12 - Scripts para tareas repetitivas, respaldos y reportes

Proyecto didáctico para abrir en **Visual Studio Code** y trabajar la primera actividad de la Semana 12: **lectura guiada + micro-quiz + glosario técnico**.

Este material está diseñado para que el estudiante comprenda, paso a paso, cómo un script puede automatizar tareas repetitivas, generar reportes y crear respaldos de información en un caso contextualizado de finca rural.

---

## 1. Propósito de la actividad

Al finalizar la actividad, el estudiante deberá ser capaz de explicar y aplicar los siguientes conceptos:

- Qué es un script.
- Para qué sirve automatizar una tarea repetitiva.
- Qué es un respaldo o copia de seguridad.
- Qué es un reporte y cómo ayuda a tomar decisiones.
- Cómo leer datos desde un archivo `.csv`.
- Cómo generar un archivo `.txt` con resultados.
- Cómo organizar evidencias de trabajo en VS Code.

---

## 2. Producto que construirá el estudiante

El estudiante ejecutará y analizará un proyecto en Python que hace lo siguiente:

```text
Lee datos de producción semanal
        ↓
Valida si los datos tienen errores
        ↓
Calcula totales, promedios, máximos y mínimos
        ↓
Genera un reporte semanal en archivo .txt
        ↓
Crea un respaldo del archivo de datos
        ↓
Registra la ejecución en una bitácora/log
```

---

## 3. Estructura del proyecto

```text
semana12_scripts_respaldos_reportes/
│
├── README.md
├── GUIA_DOCENTE.md
├── GUIA_ESTUDIANTE.md
├── TALLER_PRACTICO.md
├── CUESTIONARIO_Y_RESPUESTAS.md
├── GLOSARIO_TECNICO.md
├── RUBRICA_EVALUACION.md
├── requirements.txt
│
├── data/
│   ├── produccion_finca.csv
│   └── produccion_finca_con_errores.csv
│
├── src/
│   ├── main.py
│   ├── config.py
│   ├── validador.py
│   ├── reportes.py
│   └── respaldos.py
│
├── ejercicios_estudiante/
│   ├── ejercicio_01_completar_respaldo.py
│   ├── ejercicio_02_validar_datos.py
│   └── ejercicio_03_crear_reporte.py
│
├── material_docente/
│   └── soluciones_ejercicios.py
│
├── moodle/
│   ├── banco_preguntas_semana12.xml
│   └── glosario_base_semana12.csv
│
├── tests/
│   └── test_reportes.py
│
├── outputs/
│   ├── reportes/
│   │   └── .gitkeep
│   └── respaldos/
│       └── .gitkeep
│
├── logs/
│   └── .gitkeep
│
└── .vscode/
    ├── settings.json
    └── launch.json
```

---

## 4. Cómo abrir el proyecto en VS Code

1. Descarga y descomprime el archivo ZIP.
2. Abre Visual Studio Code.
3. Selecciona **File / Archivo > Open Folder / Abrir carpeta**.
4. Elige la carpeta `semana12_scripts_respaldos_reportes`.
5. Abre una terminal integrada en VS Code:
   - Menú **Terminal > New Terminal**.
6. Verifica que Python esté instalado:

```bash
python --version
```

En algunos equipos puede ser:

```bash
python3 --version
```

---

## 5. Cómo ejecutar el proyecto

Desde la terminal ubicada en la carpeta principal del proyecto, ejecuta:

```bash
python src/main.py
```

En algunos equipos:

```bash
python3 src/main.py
```

También puedes probar el archivo con errores:

```bash
python src/main.py --data data/produccion_finca_con_errores.csv
```

---

## 6. Qué debe entregar el estudiante

El estudiante debe entregar en Moodle:

1. Captura de pantalla de la ejecución del programa.
2. Archivo de reporte generado en `outputs/reportes/`.
3. Evidencia del respaldo creado en `outputs/respaldos/`.
4. Glosario con mínimo 10 términos.
5. Respuestas del taller práctico.
6. Micro-quiz en Moodle.

---

## 7. Recomendación para el docente

La clase puede desarrollarse en tres momentos:

1. **Comprensión conceptual:** qué es un script, respaldo y reporte.
2. **Demostración técnica:** ejecutar el proyecto, revisar carpetas y analizar salidas.
3. **Práctica guiada:** resolver el taller, completar ejercicios y responder el cuestionario.

El archivo `moodle/banco_preguntas_semana12.xml` puede importarse en Moodle como banco de preguntas.
