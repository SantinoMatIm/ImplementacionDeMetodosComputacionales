# Manual del Usuario: Analizador Léxico para Expresiones Aritméticas

## Descripción

Este programa implementa un analizador léxico (lexer) para expresiones aritméticas. El analizador recibe como entrada un archivo de texto que contiene expresiones aritméticas y comentarios, y produce como salida una tabla con los tokens identificados y sus tipos.

## Requisitos

- Python 3.x instalado en el sistema

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

## Instalación y Uso

1. Guarde el archivo `lexer_aritmetico.py` en su computadora.
2. Cree un archivo de texto con las expresiones aritméticas a analizar.
3. Abra una terminal y ejecute el programa:

bash

Copiar

`python lexer_aritmetico.py nombre_archivo.txt`

Si no especifica el nombre del archivo como argumento, el programa le pedirá ingresarlo durante la ejecución.

## Ejemplo de Uso

Supongamos que tiene un archivo llamado `expresiones.txt` con el siguiente contenido:

Copiar

`b=7 a = 32.4 *(-8.6 - b)/       6.1E-8 d = a ^ b // Esto es un comentario`

Al ejecutar:

bash

Copiar

`python lexer_aritmetico.py expresiones.txt`

El programa mostrará:

Copiar

`Token           Tipo ---------------------------------------- b               Variable =               Asignación 7               Entero a               Variable =               Asignación 32.4            Real *               Multiplicación (               Paréntesis que abre -8.6            Real -               Resta b               Variable )               Paréntesis que cierra /               División 6.1E-8          Real d               Variable =               Asignación a               Variable ^               Potencia b               Variable // Esto es un comentario  Comentario`

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

El diseño detallado del autómata finito determinístico se encuentra en el archivo adjunto (`diagrama-automata.md`). Este diagrama muestra los estados, transiciones y condiciones del autómata utilizado para el reconocimiento de tokens.