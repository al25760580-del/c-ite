# FPA-P8 Sumador

## Problema

Dadas dos horas en formato HH:MM:SS, sumarlas y mostrar el resultado en el mismo formato

La solución usa únicamente estructuras secuenciales. Los acarreos se calculan mediante división entera y módulo

## Archivos

- `diagrama.png` diagrama generado con la herramienta propia de la clase
- `diagrama.txt` texto usado para generar el diagrama
- `pseudocodigo.txt` algoritmo en el formato de la clase
- `codigo.c` programa en C con comentarios en inglés
- `ejecucion_ejemplo_a.txt` resultado del primer ejemplo
- `ejecucion_ejemplo_b.txt` resultado del segundo ejemplo

## Compilación

```text
gcc codigo.c -o sumador
./sumador
```

## Pruebas solicitadas

- `6:15:15 + 4:10:5 = 10:25:20`
- `12:33:40 + 8:28:45 = 21:02:25`
