# FPA-P7 Primeros programas

## Propósito

Familiarizarse con el entorno de programación mediante el diseño, edición y compilación de dos programas sencillos

## Programas

- [Invertir_Datos](Invertir_Datos/)
- [Calculo_Expresion](Calculo_Expresion/)

## Entregables de cada programa

- `diagrama.png` generado con la herramienta propia
- `diagrama.txt` con el texto utilizado para generar el diagrama
- `pseudocodigo.txt` en el formato de la clase
- `codigo.c` con documentación en inglés
- `ejecucion.txt` con una ejecución de prueba

## Compilación

```text
gcc codigo.c -o programa
./programa
```

Para Calculo_Expresion se necesita enlazar la biblioteca matemática

```text
gcc codigo.c -o programa -lm
./programa
```
