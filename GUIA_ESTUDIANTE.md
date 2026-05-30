# Guía del estudiante - Semana 12

## Tema

**Scripts para tareas repetitivas; automatización de respaldos y reportes.**

En esta actividad aprenderás a comprender y ejecutar un pequeño proyecto en Python que automatiza una tarea común: leer datos, generar un reporte y crear un respaldo.

---

## 1. Problema que vamos a resolver

Una finca registra diariamente información de producción. Por ejemplo:

- Litros de leche producidos.
- Kilos de maíz cosechados.
- Cantidad de huevos recolectados.

Al finalizar la semana, se necesita:

1. Calcular totales.
2. Calcular promedios.
3. Identificar días de mayor y menor producción.
4. Crear un reporte.
5. Guardar una copia de seguridad de los datos.

Hacer esto manualmente puede generar errores. Por eso usaremos un script.

---

## 2. Conceptos clave

### Script

Un script es un archivo con instrucciones que el computador puede ejecutar para realizar una tarea específica.

Ejemplo:

```text
Un script puede leer datos de producción y generar automáticamente un reporte semanal.
```

### Automatización

Automatizar significa hacer que una tarea se realice con menos intervención manual.

Ejemplo:

```text
En vez de copiar un archivo manualmente, el script crea una copia de seguridad.
```

### Respaldo

Un respaldo es una copia de seguridad de un archivo importante.

Ejemplo:

```text
Si se daña el archivo original, se puede recuperar la información desde el respaldo.
```

### Reporte

Un reporte es un documento que presenta resultados de manera organizada.

Ejemplo:

```text
Total semanal de leche: 164 litros.
Promedio diario: 23.4 litros.
```

---

## 3. Entrada, proceso y salida

Todo programa puede analizarse con esta lógica:

```text
Entrada → Proceso → Salida
```

En este proyecto:

| Parte | Ejemplo |
|---|---|
| Entrada | Archivo `produccion_finca.csv` |
| Proceso | Validar datos, calcular totales y promedios |
| Salida | Reporte `.txt`, respaldo `.csv` y log de ejecución |

---

## 4. Paso a paso para trabajar el proyecto

### Paso 1. Abre el proyecto en VS Code

Abre la carpeta completa del proyecto, no solo un archivo.

### Paso 2. Revisa el archivo de datos

Abre:

```text
data/produccion_finca.csv
```

Observa que tiene columnas separadas por comas.

### Paso 3. Ejecuta el script principal

En la terminal escribe:

```bash
python src/main.py
```

Si tu equipo usa `python3`, escribe:

```bash
python3 src/main.py
```

### Paso 4. Revisa el reporte generado

Busca la carpeta:

```text
outputs/reportes/
```

Allí debe aparecer un archivo parecido a:

```text
reporte_semanal_2026-05-27_1430.txt
```

### Paso 5. Revisa el respaldo generado

Busca la carpeta:

```text
outputs/respaldos/
```

Allí debe aparecer una copia del archivo de datos.

### Paso 6. Revisa la bitácora

Busca:

```text
logs/ejecucion.log
```

La bitácora permite saber cuándo se ejecutó el programa y qué ocurrió.

---

## 5. Prueba con errores

Ejecuta este comando:

```bash
python src/main.py --data data/produccion_finca_con_errores.csv
```

Luego responde:

1. ¿Qué errores detectó el programa?
2. ¿El programa se detuvo o continuó con los datos válidos?
3. ¿Por qué es importante validar los datos antes de generar un reporte?

---

## 6. Preguntas de comprensión

Responde en tu cuaderno o documento de entrega:

1. ¿Qué es un script?
2. ¿Qué tarea repetitiva automatiza este proyecto?
3. ¿Qué archivo funciona como entrada?
4. ¿Qué archivos se generan como salida?
5. ¿Por qué es importante crear respaldos?
6. ¿Qué información aparece en el reporte?
7. ¿Qué diferencia hay entre dato y reporte?
8. ¿Qué podría pasar si se genera un reporte con datos incorrectos?
9. ¿En qué otro contexto escolar podrías usar un script similar?
10. ¿Qué aprendiste sobre la organización de carpetas en un proyecto?

---

## 7. Evidencias que debes entregar

Sube a Moodle:

1. Captura de pantalla de la terminal después de ejecutar el programa.
2. Archivo de reporte generado.
3. Captura o archivo del respaldo creado.
4. Respuestas del taller práctico.
5. Glosario con mínimo 10 términos.
6. Micro-quiz resuelto en Moodle.
