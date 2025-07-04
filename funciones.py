import math

def funcion_unidimensional(x):
    """
    Función a optimizar: y = sin²(x)/x
    Dominio: x ∈ [-10, 10]
    
    Args:
        x (float): Valor de entrada
        
    Returns:
        float: Valor de la función evaluada en x
    """
    if x == 0:
        # Límite cuando x tiende a 0 de sin²(x)/x = 0
        return 0.0
    
    return (math.sin(x) ** 2) / x

def funcion_bidimensional(x, y):
    """
    Función a optimizar: z = 20 + x - 10·cos(2π·x) + y - 10·cos(2π·y)
    Dominio: x, y ∈ [-10, 10]
    
    Args:
        x (float): Primera variable
        y (float): Segunda variable
        
    Returns:
        float: Valor de la función evaluada en (x, y)
    """
    return 20 + x - 10 * math.cos(2 * math.pi * x) + y - 10 * math.cos(2 * math.pi * y)

def evaluar_funcion_personalizada(expresion, variables):
    """
    Evalúa una función personalizada introducida por el usuario
    
    Args:
        expresion (str): Expresión matemática como string
        variables (dict): Diccionario con las variables y sus valores
        
    Returns:
        float: Resultado de la evaluación
    """
    try:
        # Crear un entorno seguro para evaluar la expresión
        entorno_seguro = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'exp': math.exp,
            'log': math.log,
            'sqrt': math.sqrt,
            'pi': math.pi,
            'e': math.e,
            'abs': abs,
            'pow': pow,
            **variables
        }
        
        return eval(expresion, {"__builtins__": {}}, entorno_seguro)
    except Exception as e:
        print(f"Error al evaluar la función personalizada: {e}")
        return float('-inf')  # Retornar un valor muy bajo en caso de error

# Configuración de funciones predefinidas
FUNCIONES_PREDEFINIDAS = {
    'unidimensional': {
        'funcion': funcion_unidimensional,
        'nombre': 'y = sin²(x)/x',
        'variables': ['x'],
        'dominio': [(-10, 10)]
    },
    'bidimensional': {
        'funcion': funcion_bidimensional,
        'nombre': 'z = 20 + x - 10·cos(2π·x) + y - 10·cos(2π·y)',
        'variables': ['x', 'y'],
        'dominio': [(-10, 10), (-10, 10)]
    }
} 