# Guía de diagramas de flujo para estos trabajos

## 1. Qué representa un diagrama de flujo

Un diagrama de flujo muestra la secuencia de un algoritmo mediante símbolos conectados por líneas de flujo

La notación formal de diagramas de flujo se documenta en ISO 5807:1985. La norma define símbolos y convenciones para diagramas de datos, programas y sistemas

En esta clase se usa la tabla de símbolos que aparece en el material del profesor

## 2. Tabla de símbolos usada en clase

| Símbolo | Significado | Uso en estos trabajos |
| --- | --- | --- |
| Flecha | Línea de flujo. Muestra la dirección del proceso | Conecta todos los pasos |
| Óvalo | Inicio o fin | INICIO y FIN |
| Paralelogramo | Entrada o salida de datos | Leer datos y mostrar resultados |
| Rombo | Toma de decisiones | Solo cuando el problema tenga una condición |
| Selector múltiple | Selección entre varias ramas | En la actividad de VAL se usa el selector mostrado en el ejemplo de la profesora |
| Rectángulo | Procesos | Asignaciones y operaciones |
| Rectángulo redondeado | Terminal o terminador | Símbolo adicional de la tabla |
| Rectángulo con borde inferior ondulado | Documento | En el ejercicio de VAL se utiliza para presentar el resultado |
| Círculo | Conector | Une partes del diagrama en la misma página |
| Pentágono | Conector fuera de página | Continúa el flujo en otra página |
| Forma de retraso | Retraso | Representa una espera |
| Círculo con X | Y | Representa una unión lógica Y |
| Círculo con signo más | O | Representa una unión lógica O |

## 3. La forma especial para imprimir valores

En el diagrama del ejercicio de VAL, el bloque que contiene `VAL` tiene un borde inferior ondulado

De acuerdo con la tabla de símbolos, esa forma corresponde a **Documento**. En el material del profesor se emplea como la forma visual para presentar o imprimir el resultado de la función

Por lo tanto, para ese ejercicio se conserva el símbolo de documento con el texto `VAL`

No se debe sustituir por un rectángulo de proceso, porque imprimir un valor no es un cálculo. Tampoco se debe escribir código C dentro del símbolo. La instrucción `Escribir VAL` pertenece al pseudocódigo y `printf` pertenece al código C

## 4. Herramienta propia para los diagramas

Los diagramas de este repositorio se dibujan con una herramienta propia incluida en `herramienta_diagramas_profesor.py`

La herramienta utiliza los símbolos de la tabla del profesor y guarda cada diagrama como una imagen PNG

Para un diagrama secuencial se define una lista de símbolos en este orden

```text
inicio
entrada
proceso
salida
fin
```

La herramienta dibuja las líneas de flujo con flechas negras verticales, los terminales en forma redondeada, la entrada como paralelogramo, los procesos como rectángulos y la salida como documento con borde inferior ondulado

No se utiliza una librería externa de diagramas de flujo ni se inventan nodos que no aparecen en la tabla del profesor

## 5. Reglas de construcción

1. Todo diagrama debe tener un inicio y un fin
2. El flujo principal se organiza de arriba hacia abajo
3. Las flechas deben conectarse con símbolos
4. Se prefieren líneas verticales y horizontales
5. La entrada aparece antes del procesamiento
6. La salida aparece después del procesamiento
7. Las asignaciones van en procesos
8. Las lecturas y escrituras van en entrada o salida
9. Las decisiones van en rombos y cada rama debe estar identificada
10. La actividad de VAL usa un selector múltiple con las ramas 1, 2, 3 y De otra forma
11. No se agregan decisiones a un problema que pide únicamente estructuras secuenciales
12. El diagrama debe representar exactamente el pseudocódigo y el código
13. Si el diagrama ocupa más de una página se utilizan conectores

## 6. Diferencia entre pseudocódigo y C

| Pseudocódigo | C |
| --- | --- |
| `Leer A` | `scanf` |
| `Hacer RES <- A + B` | `RES = A + B` |
| `Escribir RES` | `printf` |
| `**` para potencia | `pow` de `math.h` |

En C se usan punto y coma porque forman parte de la sintaxis del lenguaje. No deben copiarse al pseudocódigo ni a las etiquetas del diagrama

## 7. Fechas de los archivos

No se agrega la fecha de elaboración a los trabajos P7, P8 ni a la plantilla de evaluación

El ejercicio de VAL es la excepción y queda identificado con la fecha `2026-10-06`

## 8. Fuentes consultadas

- ISO 5807:1985, Information processing, Documentation symbols and conventions for data, program and system flowcharts
  https://www.iso.org/standard/11955.html
- Lucidchart, Flowchart Symbols and Their Meanings
  https://lucid.co/diagram/flowchart/symbols
- LibreTexts, Basic Flowchart Symbols
  https://biz.libretexts.org/Courses/Western_Technical_College/Operations_Management_(Hammond)/04:_Operational_Processes/4.03:_Basic_Flowchart_Symbols
- Enrique Vicente Bonet Esteban, El lenguaje de programación C
  https://informatica.uv.es/estguia/ATD/apuntes/laboratorio/Lenguaje-C.pdf

## 9. Reglas comprobadas en las páginas del material

- Página 6: el rectángulo representa procesos, asignaciones y operaciones
- Página 8: el orden general es inicio, lectura, procesamiento, impresión y fin
- Página 9: las líneas de flujo deben ser rectas y estar conectadas
- Página 10: el diagrama se construye de arriba hacia abajo y de izquierda a derecha. La notación debe ser independiente del lenguaje de programación
- Página 11: no debe llegar más de una línea a un símbolo
- Página 13: el pseudocódigo inicia con título, descripción entre llaves y variables en mayúsculas con su tipo
- Página 13: las instrucciones se numeran de forma secuencial y se indentan según su dependencia
- Página 14: se usan palabras reservadas como `Leer`, `Escribir`, `Hacer`, `Si`, `entonces` y `sino`
- Página 14: los condicionales y ciclos se cierran con una expresión de fin
- Página 15: el ejemplo de invertir datos usa `Leer` y `Escribir` sin agregar asignaciones innecesarias
- Página 16: las asignaciones se escriben con una flecha hacia la variable, por ejemplo `RES <- (A + B) ** (2 / 3)`
- Página 16: `**` representa potencia en el lenguaje algorítmico del curso
