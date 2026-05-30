# Taller práctico - Semana 12

## Nombre del taller

**Automatización de respaldos y reportes con scripts en Python**

## Objetivo

Aplicar los conceptos de script, automatización, respaldo y reporte mediante la ejecución y análisis de un proyecto en VS Code.

---

# Parte 1. Reconocimiento del proyecto

Abre la carpeta del proyecto y responde:

1. ¿Cuál es el nombre del archivo principal que ejecuta el programa?
2. ¿En qué carpeta están los datos de entrada?
3. ¿En qué carpeta se guardan los reportes?
4. ¿En qué carpeta se guardan los respaldos?
5. ¿Qué archivo se usa como bitácora o log?

---

# Parte 2. Ejecución básica

Ejecuta el programa con:

```bash
python src/main.py
```

Responde:

1. ¿Qué mensaje aparece en la terminal?
2. ¿Qué archivo nuevo apareció en `outputs/reportes/`?
3. ¿Qué archivo nuevo apareció en `outputs/respaldos/`?
4. ¿Qué información contiene el reporte?
5. ¿Qué información contiene el log?

---

# Parte 3. Análisis de reporte

Abre el reporte generado y responde:

1. ¿Cuál fue el total semanal de leche?
2. ¿Cuál fue el promedio diario de leche?
3. ¿Cuál producto tuvo mayor cantidad total?
4. ¿Qué día tuvo menor producción de leche?
5. ¿Apareció alguna alerta? Explica.

---

# Parte 4. Prueba con datos incorrectos

Ejecuta:

```bash
python src/main.py --data data/produccion_finca_con_errores.csv
```

Responde:

1. ¿Qué errores detectó el programa?
2. ¿Qué registros fueron rechazados?
3. ¿Qué registros sí pudieron procesarse?
4. ¿Por qué el programa no debería aceptar cantidades negativas?
5. ¿Por qué el programa debe informar los errores encontrados?

---

# Parte 5. Modificación controlada

Abre el archivo:

```text
data/produccion_finca.csv
```

Agrega dos registros nuevos al final, por ejemplo:

```csv
2026-05-25,avicultura,huevos,130,unidades,Daniel,registro adicional
2026-05-26,avicultura,huevos,125,unidades,Daniel,registro adicional
```

Ejecuta nuevamente el programa.

Responde:

1. ¿El nuevo producto aparece en el reporte?
2. ¿Qué total aparece para huevos?
3. ¿Qué promedio aparece para huevos?
4. ¿Qué aprendiste sobre modificar datos de entrada?

---

# Parte 6. Ejercicios de código

Abre la carpeta:

```text
ejercicios_estudiante/
```

Desarrolla los siguientes ejercicios:

## Ejercicio 1

Completa `ejercicio_01_completar_respaldo.py` para que genere un nombre de respaldo con fecha.

## Ejercicio 2

Completa `ejercicio_02_validar_datos.py` para rechazar cantidades negativas o vacías.

## Ejercicio 3

Completa `ejercicio_03_crear_reporte.py` para escribir un reporte sencillo en archivo `.txt`.

---

# Parte 7. Preguntas de reflexión

1. ¿Qué tarea repetitiva automatizó este proyecto?
2. ¿Qué ventajas tiene usar un script frente a hacerlo manualmente?
3. ¿Por qué los respaldos deben tener nombres claros?
4. ¿Qué riesgos existen si no se valida la información?
5. ¿Cómo se relaciona este proyecto con situaciones reales de una finca o escuela?
6. ¿Qué dificultad encontraste al ejecutar o entender el proyecto?
7. ¿Cómo podrías mejorar el reporte generado?
8. ¿Qué otra tarea repetitiva automatizarías con Python?

---

# Entregables

Entrega en Moodle:

1. Documento con respuestas del taller.
2. Captura de ejecución en VS Code.
3. Reporte generado.
4. Evidencia del respaldo creado.
5. Glosario con mínimo 10 términos.
6. Micro-quiz resuelto.
