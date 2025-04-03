# Manual del Usuario: Analizador Léxico para Expresiones Aritméticas

## Descripción

Este programa implementa un analizador léxico (lexer) para expresiones aritméticas. El analizador recibe como entrada un archivo de texto que contiene expresiones aritméticas y comentarios, y produce como salida una tabla con los tokens identificados y sus tipos.
## Requisitos

- Python 3 instalado en el sistema
## Funcionalidad

El analizador léxico reconoce los siguientes tipos de tokens:

1. **Enteros**: Secuencias de dígitos (ej. 42, 7, 123)

2. **Reales (Flotantes)**: Números con punto decimal y/o notación científica (ej. 3.14, .5, 6.1E-8)

3. **Variables**: Identificadores que inician con una letra y pueden contener letras, números y guiones bajos (ej. x, contador, valor_1)

4. **Operadores**:

    - Asignación (=)

    - Suma (+)

    - Resta (-)

    - Multiplicación (*)

    - División (/)

    - Potencia (^)

5. **Símbolos especiales**:

    - Paréntesis que abre (()

    - Paréntesis que cierra ())

6. **Comentarios**: Texto que comienza con // y continúa hasta el final de la línea

## Estructura del Programa

El analizador léxico está implementado utilizando un Autómata Finito Determinístico (AFD) con las siguientes características:

1. **Clasificación de caracteres**: Se agrupan los caracteres en categorías (dígitos, letras, operadores, etc.).

2. **Tabla de transiciones**: Define el comportamiento del autómata según el estado actual y el tipo de caracter leído.

3. **Estados finales**: Indican qué tipo de token se ha reconocido.

## Limitaciones

- El analizador no realiza análisis sintáctico, por lo que no verifica si las expresiones son gramaticalmente correctas.

- No soporta operadores compuestos (como ++, -=, etc.).

- Los números negativos sin espacio después de un operador pueden ser interpretados incorrectamente (ej. "a+-5" se interpretará como "a", "+", "-", "5").
## Errores y Solución de Problemas

  

Si el programa encuentra caracteres no reconocidos o transiciones no válidas, mostrará mensajes de error indicando:

- El caracter problemático

- El estado en el que se produjo el error

- El lexema parcial, si corresponde

En caso de error, el analizador intentará recuperarse y continuar con el análisis.

  

## Anexo: Diseño del Autómata

## Estructura del Autómata

### Estados

El autómata consta de los siguientes estados:

|Estado|Descripción|
|---|---|
|0|Estado inicial|
|1|Leyendo dígitos (entero)|
|2|Punto después de dígito|
|3|Real (después del punto)|
|4|Variable|
|5|Exponente (después de E/e)|
|6|Signo después de exponente|
|7|Valor del exponente|
|8|Operador suma|
|9|Operador resta|
|10|Operador multiplicación|
|11|Operador potencia|
|12|Paréntesis que abre|
|13|Paréntesis que cierra|
|14|Operador asignación|
|15|Operador división (no utilizado explícitamente)|
|16|División / Posible comentario|
|17|Comentario|
|18|Punto inicial (sin dígito previo)|
|99|Estado de error|

### Tipos de Entrada

Los caracteres de entrada se clasifican en las siguientes categorías:

|Tipo|Descripción|Caracteres|
|---|---|---|
|d|Dígitos|0-9|
|l|Letras|a-z, A-Z (excepto E/e cuando se usa en notación científica)|
|suma|Operador suma|+|
|resta|Operador resta|-|
|mult|Operador multiplicación|*|
|div|Operador división|/|
|pot|Operador potencia|^|
|igual|Operador asignación|=|
|pa|Paréntesis que abre|(|
|pc|Paréntesis que cierra|)|
|punto|Punto decimal|.|
|guion|Guion bajo|_|
|b|Espacios en blanco|espacio, tab, retorno de carro|
|nl|Salto de línea|\n|
|e/E|Exponente|e, E (en notación científica)|

## Tabla de Transiciones

La tabla de transiciones se implementa como un diccionario anidado en Python. A continuación se presenta una representación textual simplificada:

```
`Estado 0 (Inicial):
   - Dígito → Estado 1 (Entero)
  - Letra → Estado 4 (Variable)
  - '+' → Estado 8 (Suma)
  - '-' → Estado 9 (Resta)
  - '*' → Estado 10 (Multiplicación)
  - '/' → Estado 16 (División/Comentario)
  - '^' → Estado 11 (Potencia)
  - '(' → Estado 12 (Paréntesis abre)
  - ')' → Estado 13 (Paréntesis cierra)
  - '=' → Estado 14 (Asignación)
  - '.' → Estado 18 (Punto inicial)
  - Espacio/Salto → Estado 0 (Permanece en inicial)
 Estado 1 (Entero):
   - Dígito → Estado 1 (Sigue en Entero)
  - '.' → Estado 2 (Punto después de dígito)
  - 'E'/'e' → Estado 5 (Exponente)
  - Espacio/Salto/Operadores/Paréntesis → Aceptar como Entero y transitar
 Estado 2 (Punto después de dígito):
   - Dígito → Estado 3 (Real)
  - Otro → Error (99)
 Estado 3 (Real):
   - Dígito → Estado 3 (Sigue en Real)
  - 'E'/'e' → Estado 5 (Exponente)
  - Espacio/Salto/Operadores/Paréntesis → Aceptar como Real y transitar
 ...
 Estado 17 (Comentario):
   - Cualquier caracter excepto salto de línea → Estado 17 (Sigue en Comentario)
  - Salto de línea → Aceptar como Comentario y volver a Estado 0`
```

## Algoritmo de Análisis

El algoritmo para procesar el texto de entrada es el siguiente:

1. Inicializar el estado actual a 0 (estado inicial).
2. Inicializar un lexema vacío.
3. Para cada caracter en el texto de entrada: a. Determinar el tipo de entrada del caracter. b. Consultar la tabla de transiciones para obtener el estado siguiente. c. Si la transición no está definida, reportar un error y reiniciar el estado. d. Si el estado actual es un estado final y cambiamos a otro estado, aceptar el lexema como un token. e. Actualizar el estado actual. f. Actualizar el lexema si corresponde.
4. Si queda un lexema al final del texto y el estado es final, aceptar como token.

## Manejo de Casos Especiales

### Notación Científica

La notación científica se maneja a través de los estados 5, 6 y 7:

- Estado 5: Después de leer 'E' o 'e' en un número
- Estado 6: Después de leer un signo opcional (+/-) después de E/e
- Estado 7: Leyendo los dígitos del exponente

### Comentarios

Los comentarios se reconocen mediante:

- Estado 16: Después de leer una barra '/'
- Estado 17: Después de leer dos barras '//'
- El comentario termina con un salto de línea

### Números sin parte entera

Números como `.45` se manejan con:

- Estado 18: Después de leer un punto sin dígitos previos
- Estado 3: Después de leer dígitos a continuación del punto

## Diagrama Visual

El diagrama del autómata se muestra en el archivo `diagrama-automata.md`. Esta representación visual ayuda a comprender las transiciones entre estados y el flujo del proceso de análisis léxico.

## Implementación en Código

La implementación en Python utiliza diccionarios anidados para representar la tabla de transiciones:

- Diccionario externo: La clave es el estado actual
- Diccionario interno: La clave es el tipo de entrada, el valor es el estado siguiente

Esta estructura de datos permite una consulta eficiente de las transiciones y facilita la adición de nuevos estados o tipos de entrada según sea necesario.
