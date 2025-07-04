
import sys
import time
from funciones import FUNCIONES_PREDEFINIDAS
from algoritmo_genetico import AlgoritmoGenetico, optimizar_funcion_personalizada

def mostrar_banner():
    print("=" * 60)
    print(" " * 15 + "ALGORITMO GENÉTICO")
    print(" " * 10 + "Optimización de Funciones")
    print("=" * 60)
    print()

def mostrar_menu_principal():
    print("Seleccione una opción:")
    print("1. Optimización de función unidimensional: y = sin²(x)/x")
    print("2. Optimización de función bidimensional: z = 20 + x - 10·cos(2π·x) + y - 10·cos(2π·y)")
    print("3. Introducir función personalizada")
    print("4. Configurar parámetros del algoritmo genético")
    print("5. Salir")
    print()

def obtener_parametros_usuario():
    print("\nConfiguración de parámetros del algoritmo genético:")
    print("(Presione Enter para usar el valor por defecto)")
    
    parametros = {}
    
    try:
        entrada = input(f"Tamaño de la población (default: 10): ").strip()
        parametros['tamano_poblacion'] = int(entrada) if entrada else 10
        
        entrada = input(f"Umbral de diferencia (default: 0.05): ").strip()
        parametros['umbral_diferencia'] = float(entrada) if entrada else 0.05
        
        entrada = input(f"Número máximo de iteraciones (default: 500): ").strip()
        parametros['max_iteraciones'] = int(entrada) if entrada else 500
        
        entrada = input(f"Variabilidad de la mutación (default: 1): ").strip()
        parametros['variabilidad_mutacion'] = float(entrada) if entrada else 1
        
        print("\nParámetros configurados:")
        for clave, valor in parametros.items():
            print(f"  {clave}: {valor}")
        
    except ValueError:
        print("Error: Por favor introduzca valores numéricos válidos.")
        return obtener_parametros_usuario()
    
    return parametros

def optimizar_funcion_predefinida(tipo_funcion, parametros):
    config = FUNCIONES_PREDEFINIDAS[tipo_funcion]
    
    print(f"\nOptimizando función: {config['nombre']}")
    print(f"Dominio: {config['dominio']}")
    print("-" * 50)
    
    ag = AlgoritmoGenetico(
        tamano_poblacion=parametros.get('tamano_poblacion', 10),
        umbral_diferencia=parametros.get('umbral_diferencia', 0.05),
        max_iteraciones=parametros.get('max_iteraciones', 500),
        variabilidad_mutacion=parametros.get('variabilidad_mutacion', 1)
    )
    
    inicio = time.time()
    mejor_individuo = ag.optimizar(config['funcion'], config['dominio'])
    fin = time.time()
    
    print("-" * 50)
    print("RESULTADOS DE LA OPTIMIZACIÓN:")
    print(f"Tiempo de ejecución: {fin - inicio:.2f} segundos")
    print(f"Mejor valor encontrado: {mejor_individuo.fitness:.8f}")
    
    if len(mejor_individuo.genes) == 1:
        print(f"Valor óptimo de x: {mejor_individuo.genes[0]:.8f}")
    else:
        for i, variable in enumerate(config['variables']):
            print(f"Valor óptimo de {variable}: {mejor_individuo.genes[i]:.8f}")
    
    print(f"Número de generaciones: {len(ag.historial_fitness)}")
    print("-" * 50)
    
    return mejor_individuo

def introducir_funcion_personalizada(parametros):
    print("\nIntroducir función personalizada:")
    print("Funciones disponibles: sin, cos, tan, exp, log, sqrt, abs, pow")
    print("Constantes disponibles: pi, e")
    print("Operadores: +, -, *, /, **, ()")
    print()
    
    try:
        num_variables = int(input("Número de variables (1 o 2): "))
        if num_variables not in [1, 2]:
            print("Error: Solo se admiten 1 o 2 variables.")
            return
        
        variables = []
        for i in range(num_variables):
            var_name = input(f"Nombre de la variable {i+1}: ").strip()
            if not var_name:
                var_name = 'x' if i == 0 else 'y'
            variables.append(var_name)
        
        dominio = []
        for i, var in enumerate(variables):
            print(f"Dominio para la variable {var}:")
            min_val = float(input(f"  Valor mínimo (default: -10): ") or "-10")
            max_val = float(input(f"  Valor máximo (default: 10): ") or "10")
            dominio.append((min_val, max_val))
        
        print(f"\nIntroduzca la expresión de la función usando las variables: {', '.join(variables)}")
        print("Ejemplo: sin(x)**2 / x")
        expresion = input("Expresión: ").strip()
        
        if not expresion:
            print("Error: Debe introducir una expresión.")
            return
        
        print(f"\nFunción a optimizar: {expresion}")
        print(f"Variables: {variables}")
        print(f"Dominio: {dominio}")
        print("-" * 50)
        
        confirmar = input("¿Desea proceder con la optimización? (s/n): ").strip().lower()
        if confirmar not in ['s', 'si', 'sí', 'y', 'yes']:
            return
        
        inicio = time.time()
        mejor_individuo = optimizar_funcion_personalizada(expresion, variables, dominio, parametros)
        fin = time.time()
        
        print("-" * 50)
        print("RESULTADOS DE LA OPTIMIZACIÓN:")
        print(f"Tiempo de ejecución: {fin - inicio:.2f} segundos")
        print(f"Mejor valor encontrado: {mejor_individuo.fitness:.8f}")
        
        for i, variable in enumerate(variables):
            print(f"Valor óptimo de {variable}: {mejor_individuo.genes[i]:.8f}")
        print("-" * 50)
        
    except ValueError:
        print("Error: Por favor introduzca valores numéricos válidos.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    mostrar_banner()
    
    parametros = {
        'tamano_poblacion': 10,
        'umbral_diferencia': 0.05,
        'max_iteraciones': 500,
        'variabilidad_mutacion': 1
    }
    
    while True:
        mostrar_menu_principal()
        
        try:
            opcion = input("Seleccione una opción (1-5): ").strip()
            
            if opcion == '1':
                print("\n" + "=" * 60)
                print("OPTIMIZACIÓN DE FUNCIÓN UNIDIMENSIONAL")
                print("=" * 60)
                optimizar_funcion_predefinida('unidimensional', parametros)
                
            elif opcion == '2':
                print("\n" + "=" * 60)
                print("OPTIMIZACIÓN DE FUNCIÓN BIDIMENSIONAL")
                print("=" * 60)
                optimizar_funcion_predefinida('bidimensional', parametros)
                
            elif opcion == '3':
                print("\n" + "=" * 60)
                print("OPTIMIZACIÓN DE FUNCIÓN PERSONALIZADA")
                print("=" * 60)
                introducir_funcion_personalizada(parametros)
                
            elif opcion == '4':
                print("\n" + "=" * 60)
                print("CONFIGURACIÓN DE PARÁMETROS")
                print("=" * 60)
                parametros = obtener_parametros_usuario()
                
            elif opcion == '5':
                print("\nFinalizado")
                break
                
            else:
                print("Error: Opción no válida. Por favor seleccione una opción del 1 al 5.")
            
            if opcion in ['1', '2', '3']:
                input("\nPresione Enter para continuar...")
                print()
        
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario.")
            print("¡Gracias por usar el programa!")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")
            print("Por favor, intente nuevamente.")

if __name__ == "__main__":
    main() 