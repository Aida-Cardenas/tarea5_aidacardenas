#!/usr/bin/env python3
"""
Archivo de prueba para validar el funcionamiento del algoritmo genético
"""

from funciones import funcion_unidimensional, funcion_bidimensional, FUNCIONES_PREDEFINIDAS
from algoritmo_genetico import AlgoritmoGenetico, optimizar_funcion_personalizada
import math

def test_funciones_basicas():
    """
    Prueba las funciones básicas
    """
    print("=" * 50)
    print("PRUEBAS DE FUNCIONES BÁSICAS")
    print("=" * 50)
    
    # Prueba función unidimensional
    print("Función unidimensional:")
    test_values = [1, 2, 3, -1, -2, 0.1, -0.1]
    for x in test_values:
        y = funcion_unidimensional(x)
        print(f"  f({x:4.1f}) = {y:.6f}")
    
    # Prueba función bidimensional
    print("\nFunción bidimensional:")
    test_pairs = [(0, 0), (1, 1), (-1, -1), (2, 3), (-2, -3)]
    for x, y in test_pairs:
        z = funcion_bidimensional(x, y)
        print(f"  f({x:4.1f}, {y:4.1f}) = {z:.6f}")
    
    print("✓ Pruebas de funciones básicas completadas")

def test_algoritmo_genetico_simple():
    """
    Prueba el algoritmo genético con parámetros simples
    """
    print("\n" + "=" * 50)
    print("PRUEBAS DEL ALGORITMO GENÉTICO")
    print("=" * 50)
    
    # Parámetros de prueba (valores pequeños para prueba rápida)
    parametros = {
        'tamano_poblacion': 20,
        'umbral_diferencia': 0.01,
        'max_iteraciones': 50,
        'variabilidad_mutacion': 0.5
    }
    
    # Prueba función unidimensional
    print("Optimizando función unidimensional...")
    config = FUNCIONES_PREDEFINIDAS['unidimensional']
    
    ag = AlgoritmoGenetico(
        tamano_poblacion=parametros['tamano_poblacion'],
        umbral_diferencia=parametros['umbral_diferencia'],
        max_iteraciones=parametros['max_iteraciones'],
        variabilidad_mutacion=parametros['variabilidad_mutacion']
    )
    
    mejor_individuo = ag.optimizar(config['funcion'], config['dominio'], mostrar_progreso=False)
    
    print(f"Mejor resultado unidimensional:")
    print(f"  x = {mejor_individuo.genes[0]:.6f}")
    print(f"  f(x) = {mejor_individuo.fitness:.6f}")
    print(f"  Generaciones: {len(ag.historial_fitness)}")
    
    # Prueba función bidimensional
    print("\nOptimizando función bidimensional...")
    config = FUNCIONES_PREDEFINIDAS['bidimensional']
    
    ag2 = AlgoritmoGenetico(
        tamano_poblacion=parametros['tamano_poblacion'],
        umbral_diferencia=parametros['umbral_diferencia'],
        max_iteraciones=parametros['max_iteraciones'],
        variabilidad_mutacion=parametros['variabilidad_mutacion']
    )
    
    mejor_individuo2 = ag2.optimizar(config['funcion'], config['dominio'], mostrar_progreso=False)
    
    print(f"Mejor resultado bidimensional:")
    print(f"  x = {mejor_individuo2.genes[0]:.6f}")
    print(f"  y = {mejor_individuo2.genes[1]:.6f}")
    print(f"  f(x,y) = {mejor_individuo2.fitness:.6f}")
    print(f"  Generaciones: {len(ag2.historial_fitness)}")
    
    print("✓ Pruebas del algoritmo genético completadas")

def test_funcion_personalizada():
    """
    Prueba la funcionalidad de función personalizada
    """
    print("\n" + "=" * 50)
    print("PRUEBAS DE FUNCIÓN PERSONALIZADA")
    print("=" * 50)
    
    # Parámetros de prueba
    parametros = {
        'tamano_poblacion': 15,
        'umbral_diferencia': 0.01,
        'max_iteraciones': 30,
        'variabilidad_mutacion': 0.8
    }
    
    # Prueba función simple: x^2
    print("Optimizando función personalizada: x**2")
    expresion = "x**2"
    variables = ['x']
    dominio = [(-5, 5)]
    
    mejor_individuo = optimizar_funcion_personalizada(expresion, variables, dominio, parametros)
    
    print(f"Resultado para x**2:")
    print(f"  x = {mejor_individuo.genes[0]:.6f}")
    print(f"  f(x) = {mejor_individuo.fitness:.6f}")
    print(f"  Nota: Para x**2, el máximo en [-5,5] debería estar en x=5 o x=-5")
    
    # Prueba función bidimensional: -(x^2 + y^2)
    print("\nOptimizando función personalizada: -(x**2 + y**2)")
    expresion = "-(x**2 + y**2)"
    variables = ['x', 'y']
    dominio = [(-3, 3), (-3, 3)]
    
    mejor_individuo2 = optimizar_funcion_personalizada(expresion, variables, dominio, parametros)
    
    print(f"Resultado para -(x**2 + y**2):")
    print(f"  x = {mejor_individuo2.genes[0]:.6f}")
    print(f"  y = {mejor_individuo2.genes[1]:.6f}")
    print(f"  f(x,y) = {mejor_individuo2.fitness:.6f}")
    print(f"  Nota: Para -(x**2 + y**2), el máximo debería estar en (0,0) con valor 0")
    
    print("✓ Pruebas de función personalizada completadas")

def main():
    """
    Ejecuta todas las pruebas
    """
    print("EJECUTANDO PRUEBAS DEL PROGRAMA")
    print("=" * 60)
    
    try:
        test_funciones_basicas()
        test_algoritmo_genetico_simple()
        test_funcion_personalizada()
        
        print("\n" + "=" * 60)
        print("✓ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
        print("✓ El programa está listo para ser usado")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ ERROR EN LAS PRUEBAS: {e}")
        print("Por favor, revise el código antes de usar el programa.")

if __name__ == "__main__":
    main() 