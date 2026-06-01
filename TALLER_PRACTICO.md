# Taller práctico - Semana 12

## Nombre del taller

**Automatización de respaldos y reportes con scripts en Python**

## Objetivo

Aplicar los conceptos de script, automatización, respaldo y reporte mediante la ejecución y análisis de un proyecto en VS Code.

---

# Parte 1. Reconocimiento del proyecto

Abre la carpeta del proyecto y responde:
1. ¿Cuál es el nombre del archivo principal que ejecuta el programa? **src/main.py**
2. ¿En qué carpeta están los datos de entrada? **data/**
3. ¿En qué carpeta se guardan los reportes? **outputs/reportes/**
4. ¿En qué carpeta se guardan los respaldos? **outputs/respaldos/**
5. ¿Qué archivo se usa como bitácora o log? **logs/ejecucion.log**

---

# Parte 2. Ejecución básica

Ejecuta el programa con:
1. ¿Qué mensaje aparece en la terminal? **"Proceso completado" seguido del resumen de registros válidos, errores, advertencias y las rutas de los archivos generados.**
2. ¿Qué archivo nuevo apareció en `outputs/reportes/`? **Un archivo de texto llamado `reporte_semanal_` seguido de la fecha y hora actual (ej. `reporte_semanal_2026-05-27_143000.txt`).**
3. ¿Qué archivo nuevo apareció en `outputs/respaldos/`? **Una copia del CSV original llamada `respaldo_produccion_finca_` con la marca de tiempo.**
4. ¿Qué información contiene el reporte? **Indicadores estadísticos (total, promedio, máximo, mínimo) por cada producto, alertas de producción alta/baja y el detalle de errores encontrados.**
5. ¿Qué información contiene el log? **La trazabilidad de la ejecución: fecha/hora de inicio, archivo procesado, conteo de registros y confirmación de éxito de cada módulo.**

---

# Parte 3. Análisis de reporte

Abre el reporte generado y responde:
1. ¿Cuál fue el total semanal de leche? **162.00 litros.**
2. ¿Cuál fue el promedio diario de leche? **23.14 litros.**
3. ¿Cuál producto tuvo mayor cantidad total? **Huevos (1090.00 unidades).**
4. ¿Qué día tuvo menor producción de leche? **2026-05-24 (20 litros).**
5. ¿Apareció alguna alerta? Explica. **Sí, una observación de producción alta para la leche el día 2026-05-22, ya que los 27 litros superan el promedio semanal en más de un 15%.**

---

# Parte 4. Prueba con datos incorrectos

Ejecuta:
1. ¿Qué errores detectó el programa? **Fechas con formato incorrecto, campos obligatorios vacíos (como área o unidad) y cantidades que no son números.**
2. ¿Qué registros fueron rechazados? **Aquellos donde la validación falló (ej. cantidad negativa o fecha inválida), los cuales se listan en la sección "ERRORES DETECTADOS" del reporte.**
3. ¿Qué registros sí pudieron procesarse? **Todos aquellos que cumplieron con el formato AAAA-MM-DD y tenían valores numéricos positivos en la columna de cantidad.**
4. ¿Por qué el programa no debería aceptar cantidades negativas? **Porque físicamente no es posible producir cantidades negativas; un valor negativo indica un error de captura que alteraría negativamente los promedios y totales.**
5. ¿Por qué el programa debe informar los errores encontrados? **Para garantizar la integridad de los datos y permitir que el usuario corrija la fuente original de información.**

---

# Parte 5. Modificación controlada

Abre el archivo:
1. ¿El nuevo producto aparece en el reporte? **Sí, el script lo agrupa automáticamente bajo el encabezado "HUEVOS".**
2. ¿Qué total aparece para huevos? **1090.00 unidades.**
3. ¿Qué promedio aparece para huevos? **121.11 unidades.**
4. ¿Qué aprendiste sobre modificar datos de entrada? **Que el script es dinámico y escalable; no importa si se añaden más filas o productos nuevos, el proceso de cálculo se adapta automáticamente.**

---

# Parte 6. Ejercicios de código
Los ejercicios en la carpeta `ejercicios_estudiante/` han sido completados exitosamente siguiendo las reglas de validación y generación de archivos solicitadas.

---

# Parte 7. Preguntas de reflexión

1. ¿Qué tarea repetitiva automatizó este proyecto? **La lectura de registros diarios, el cálculo de estadísticas de producción, la generación de reportes y la creación de copias de seguridad.**
2. ¿Qué ventajas tiene usar un script frente a hacerlo manualmente? **Ahorro de tiempo, precisión en los cálculos matemáticos y la garantía de que el proceso siempre se realiza bajo los mismos estándares.**
3. ¿Por qué los respaldos deben tener nombres claros? **Para permitir una recuperación rápida y organizada de la información, identificando fácilmente qué versión del archivo corresponde a cada momento del tiempo.**
4. ¿Qué riesgos existen si no se valida la información? **Se pueden tomar decisiones erróneas basadas en datos falsos, como creer que hay una baja producción cuando en realidad es un error de digitación.**
5. ¿Cómo se relaciona este proyecto con situaciones reales de una finca o escuela? **Es idéntico a llevar el control de inventarios, asistencia de estudiantes o notas, donde se requiere reportar estados periódicos y asegurar los datos.**
6. ¿Qué dificultad encontraste al ejecutar o entender el proyecto? **Comprender cómo se comunican diferentes archivos entre sí (módulos), pero la estructura organizada facilitó el seguimiento.**
7. ¿Cómo podrías mejorar el reporte generado? **Agregando visualizaciones gráficas (como gráficos de barras) o enviando el reporte automáticamente por correo electrónico.**
8. ¿Qué otra tarea repetitiva automatizarías con Python? **El control de gastos mensuales o el renombrado masivo de archivos de fotografías.**

---

# Entregables

Entrega en Moodle:

1. Documento con respuestas del taller.
2. Captura de ejecución en VS Code.
3. Reporte generado.
4. Evidencia del respaldo creado.
5. Glosario con mínimo 10 términos.
6. Micro-quiz resuelto.
