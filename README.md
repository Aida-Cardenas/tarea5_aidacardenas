# Tarea 5: Algoritmo Genético

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
- `main.py`: main
- `gui.py`: Interfaz gráfica. debes correrlo para que funcione el programa jeje
- `algoritmo_genetico.py`: algoritmo
- `funciones.py`: las funciones a utilizar

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

### Ejemplos por si quieres probarlos nose 

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

