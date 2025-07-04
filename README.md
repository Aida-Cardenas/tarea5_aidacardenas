# Tarea 5: Algoritmo Genético

## Descripción
Este programa implementa un algoritmo genético para encontrar el valor óptimo de funciones matemáticas. El programa permite optimizar funciones predefinidas y también permite al usuario introducir funciones personalizadas.

## Funciones Implementadas

### 1. Función Unidimensional
- **Función**: `y = sin²(x)/x`
- **Dominio**: x ∈ [-10, 10]
- **Objetivo**: Encontrar el valor de x que maximiza la función

### 2. Función Bidimensional
- **Función**: `z = 20 + x - 10·cos(2π·x) + y - 10·cos(2π·y)`
- **Dominio**: x, y ∈ [-10, 10]
- **Objetivo**: Encontrar los valores de x e y que maximizan la función

## Estructura del Programa

### Archivos Principales
- `main.py`: Programa principal con interfaz de consola
- `gui.py`: Interfaz gráfica del programa
- `algoritmo_genetico.py`: Implementación del algoritmo genético
- `funciones.py`: Definiciones de las funciones a optimizar
- `test_programa.py`: Archivo de pruebas para validar el funcionamiento

## Parámetros del Algoritmo Genético

El programa permite configurar los siguientes parámetros:

- **Tamaño de la población** (default: 10): Número de individuos en cada generación
- **Umbral de diferencia** (default: 0.05): Criterio de convergencia
- **Número máximo de iteraciones** (default: 500): Límite de generaciones
- **Variabilidad de la mutación** (default: 1): Intensidad de las mutaciones

## Instrucciones de Uso

### Ejecución del Programa Principal (Consola)
```bash
python main.py
```

### Ejecución de la Interfaz Gráfica
```bash
python gui.py
```

### Ejecución de Pruebas
```bash
python test_programa.py
```

## Características Destacadas

### 1. Interfaz de Usuario Intuitiva
- **Interfaz Gráfica**: Ventana moderna con pestañas organizadas
- **Interfaz de Consola**: Menú interactivo tradicional
- Configuración de parámetros interactiva
- Visualización en tiempo real del progreso

### 2. Algoritmo Genético Robusto
- Selección por torneo
- Cruzamiento uniforme
- Mutación gaussiana
- Estrategia elitista
- Criterio de convergencia automático

### 3. Funcionalidad Extendida (Puntos Extra)
- Permite introducir funciones personalizadas durante la ejecución
- Soporte para funciones matemáticas complejas
- Evaluación segura de expresiones
- Interfaz gráfica para facilitar el uso

### 4. Visualización de Resultados
- Estadísticas por generación (máximo, mediana, mínimo)
- Tiempo de ejecución
- Número de generaciones hasta convergencia
- Valores óptimos encontrados

## Interfaz Gráfica

La interfaz gráfica (`gui.py`) ofrece una experiencia de usuario moderna y facilita el uso del programa:

### Características de la GUI:
- **Pestañas organizadas**: Funciones predefinidas, personalizada y parámetros
- **Introducción de funciones**: Campo de texto para expresiones matemáticas
- **Configuración visual**: Dominio de variables y parámetros del algoritmo
- **Resultados en tiempo real**: Consola integrada con colores
- **Ejecución en segundo plano**: No bloquea la interfaz durante la optimización

### Cómo usar la GUI:
1. Ejecute `python gui.py`
2. Seleccione una pestaña según su necesidad
3. Configure los parámetros del algoritmo
4. Presione "Ejecutar Optimización"
5. Observe los resultados en la consola integrada

## Ejemplo de Uso

### Optimización de Función Unidimensional
```
Generación   1: Máximo = 0.708073, Mediana = 0.234567, Mínimo = -0.456789
Generación   2: Máximo = 0.722488, Mediana = 0.345678, Mínimo = -0.234567
...
Convergencia alcanzada en la generación 16

RESULTADOS DE LA OPTIMIZACIÓN:
Mejor valor encontrado: 0.72248799
Valor óptimo de x: 1.10589123
```

### Función Personalizada
El programa permite introducir funciones como:
- `sin(x)**2 / x`
- `x**2 + y**2`
- `exp(-x**2) * cos(y)`
- `log(abs(x)) + sqrt(abs(y))`

## Formato de Funciones Personalizadas

### Sintaxis Básica
Para introducir funciones personalizadas, use la siguiente sintaxis:

#### Variables Permitidas:
- **Una variable**: Use `x` como nombre de variable
- **Dos variables**: Use `x` e `y` como nombres de variables

#### Operadores Matemáticos:
- **Aritméticos**: `+`, `-`, `*`, `/`, `**` (potencia)
- **Paréntesis**: `(`, `)` para agrupar operaciones

#### Funciones Matemáticas Disponibles:
- **Trigonométricas**: `sin(x)`, `cos(x)`, `tan(x)`
- **Exponenciales**: `exp(x)` (e^x), `log(x)` (logaritmo natural)
- **Otras**: `sqrt(x)`, `abs(x)`, `pow(x, y)`

#### Constantes Matemáticas:
- **pi**: Valor de π (3.14159...)
- **e**: Número de Euler (2.71828...)

### Ejemplos de Funciones Válidas:

#### Funciones de Una Variable:
```python
# Función sinusoidal
sin(x)**2 / x

# Función exponencial
exp(-x**2)

# Función polinómica
x**3 - 2*x**2 + x

# Función con valor absoluto
abs(x) * cos(x)

# Función logarítmica
log(abs(x) + 1)

# Función con constantes
pi * sin(x) + e * cos(x)
```

#### Funciones de Dos Variables:
```python
# Función cuadrática
x**2 + y**2

# Función trigonométrica
sin(x) * cos(y)

# Función exponencial bidimensional
exp(-(x**2 + y**2))

# Función mixta
x*y - x**2 - y**2

# Función con raíz cuadrada
sqrt(abs(x*y))

# Función de Rosenbrock
100*(y - x**2)**2 + (1 - x)**2
```

### Reglas Importantes:

1. **Nombres de Variables**: Use exactamente `x` para una variable o `x`, `y` para dos variables
2. **Paréntesis**: Siempre use paréntesis para argumentos de funciones: `sin(x)`, no `sin x`
3. **Potencias**: Use `**` para potencias: `x**2`, no `x^2`
4. **Multiplicación**: Use `*` explícitamente: `2*x`, no `2x`
5. **División por Cero**: Tenga cuidado con funciones que pueden dividir por cero
6. **Dominio**: Asegúrese de que la función esté definida en el dominio especificado

### Ejemplos de Sintaxis Incorrecta:
```python
# ❌ Incorrecto
sin x           # Falta paréntesis
x^2             # Usar ** en lugar de ^
2x              # Falta * entre 2 y x
log(x)          # Puede fallar si x ≤ 0
sqrt(x)         # Puede fallar si x < 0

# ✅ Correcto
sin(x)          # Con paréntesis
x**2            # Con **
2*x             # Con * explícito
log(abs(x) + 1) # Evitar log de números negativos
sqrt(abs(x))    # Evitar raíz de números negativos
```

### Consejos para Funciones Personalizadas:

1. **Pruebe su función**: Verifique que la sintaxis sea correcta
2. **Evite singularidades**: Use `abs()` para evitar valores negativos en `log()` y `sqrt()`
3. **Dominio apropiado**: Ajuste el dominio según el comportamiento de su función
4. **Parámetros del algoritmo**: Funciones complejas pueden requerir más iteraciones

## Requisitos del Sistema

- Python 3.6 o superior
- Módulos estándar de Python:
  - `math`
  - `random`
  - `statistics`
  - `sys`
  - `time`

## Consideraciones Técnicas

### Manejo de Casos Especiales
- División por cero en la función sin²(x)/x
- Evaluación segura de funciones personalizadas
- Validación de dominios y parámetros

### Optimizaciones Implementadas
- Estrategia elitista para preservar las mejores soluciones
- Criterio de convergencia para evitar iteraciones innecesarias
- Mutación adaptativa según el dominio de las variables

## Resultados Esperados

### Función Unidimensional
- Valor óptimo aproximado: x ≈ 1.11
- Valor máximo: y ≈ 0.722

### Función Bidimensional
- Los valores óptimos dependerán de los parámetros del algoritmo
- La función tiene múltiples máximos locales

## Desarrollo y Pruebas

El programa ha sido desarrollado siguiendo buenas prácticas:
- Código modular y bien documentado
- Manejo de errores y excepciones
- Archivo de pruebas para validación
- Interfaz de usuario amigable

## Autor
Desarrollado para la Tarea 5: Algoritmo Genético 