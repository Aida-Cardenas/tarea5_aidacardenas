import random
import math
import statistics
from funciones import evaluar_funcion_personalizada

class Individuo:

    def __init__(self, genes, dominio):
        self.genes = genes  
        self.dominio = dominio 
        self.fitness = 0.0
        self.evaluado = False
    
    def evaluar(self, funcion_objetivo):
 
        if not self.evaluado:
            try:
                if len(self.genes) == 1:
                    self.fitness = funcion_objetivo(self.genes[0])
                else:
                    self.fitness = funcion_objetivo(*self.genes)
                self.evaluado = True
            except Exception as e:
                self.fitness = float('-inf')
                self.evaluado = True
        return self.fitness
    
    def mutar(self, variabilidad_mutacion):

        for i in range(len(self.genes)):
            if random.random() < 0.1:  
                min_val, max_val = self.dominio[i]
                rango = max_val - min_val
                
                mutacion = random.gauss(0, variabilidad_mutacion)
                self.genes[i] += mutacion * rango * 0.1
                
                self.genes[i] = max(min_val, min(max_val, self.genes[i]))
        
        self.evaluado = False  
    
    def clonar(self):
        nuevo = Individuo(self.genes.copy(), self.dominio)
        nuevo.fitness = self.fitness
        nuevo.evaluado = self.evaluado
        return nuevo

class AlgoritmoGenetico:
    
    def __init__(self, tamano_poblacion=10, umbral_diferencia=0.05, 
                 max_iteraciones=500, variabilidad_mutacion=1):
        self.tamano_poblacion = tamano_poblacion
        self.umbral_diferencia = umbral_diferencia
        self.max_iteraciones = max_iteraciones
        self.variabilidad_mutacion = variabilidad_mutacion
        self.poblacion = []
        self.mejor_individuo = None
        self.historial_fitness = []
    
    def inicializar_poblacion(self, dominio):

        self.poblacion = []
        for _ in range(self.tamano_poblacion):
            genes = []
            for min_val, max_val in dominio:
                genes.append(random.uniform(min_val, max_val))
            self.poblacion.append(Individuo(genes, dominio))
    
    def evaluar_poblacion(self, funcion_objetivo):

        for individuo in self.poblacion:
            individuo.evaluar(funcion_objetivo)
    
    def seleccion_torneo(self, tamano_torneo=3):

        candidatos = random.sample(self.poblacion, min(tamano_torneo, len(self.poblacion)))
        return max(candidatos, key=lambda x: x.fitness)
    
    def cruzamiento(self, padre1, padre2):

        hijo1_genes = []
        hijo2_genes = []
        
        for i in range(len(padre1.genes)):
            if random.random() < 0.5:
                hijo1_genes.append(padre1.genes[i])
                hijo2_genes.append(padre2.genes[i])
            else:
                hijo1_genes.append(padre2.genes[i])
                hijo2_genes.append(padre1.genes[i])
        
        hijo1 = Individuo(hijo1_genes, padre1.dominio)
        hijo2 = Individuo(hijo2_genes, padre1.dominio)
        
        return hijo1, hijo2
    
    def obtener_estadisticas(self):

        fitness_valores = [ind.fitness for ind in self.poblacion]
        return {
            'maximo': max(fitness_valores),
            'minimo': min(fitness_valores),
            'mediana': statistics.median(fitness_valores),
            'promedio': statistics.mean(fitness_valores)
        }
    
    def convergio(self):

        if len(self.historial_fitness) < 10:
            return False
        
        fitness_recientes = self.historial_fitness[-10:]
        mejora = max(fitness_recientes) - min(fitness_recientes)
        
        return mejora < self.umbral_diferencia
    
    def optimizar(self, funcion_objetivo, dominio, mostrar_progreso=True):
        self.inicializar_poblacion(dominio)
        self.historial_fitness = []
        
        for generacion in range(self.max_iteraciones):

            self.evaluar_poblacion(funcion_objetivo)
            

            mejor_actual = max(self.poblacion, key=lambda x: x.fitness)
            if self.mejor_individuo is None or mejor_actual.fitness > self.mejor_individuo.fitness:
                self.mejor_individuo = mejor_actual.clonar()
 
            stats = self.obtener_estadisticas()
            self.historial_fitness.append(stats['maximo'])
 
            if mostrar_progreso:
                print(f"Generación {generacion + 1:3d}: "
                      f"Máximo = {stats['maximo']:.6f}, "
                      f"Mediana = {stats['mediana']:.6f}, "
                      f"Mínimo = {stats['minimo']:.6f}")
            
            if self.convergio():
                if mostrar_progreso:
                    print(f"Convergencia alcanzada en la generación {generacion + 1}")
                break
            
            nueva_poblacion = []
            
            poblacion_ordenada = sorted(self.poblacion, key=lambda x: x.fitness, reverse=True)
            num_elite = max(1, self.tamano_poblacion // 10)  
            for i in range(num_elite):
                nueva_poblacion.append(poblacion_ordenada[i].clonar())
            
            while len(nueva_poblacion) < self.tamano_poblacion:
                padre1 = self.seleccion_torneo()
                padre2 = self.seleccion_torneo()
                
                if random.random() < 0.8:  
                    hijo1, hijo2 = self.cruzamiento(padre1, padre2)
                else:
                    hijo1, hijo2 = padre1.clonar(), padre2.clonar()
                
                hijo1.mutar(self.variabilidad_mutacion)
                hijo2.mutar(self.variabilidad_mutacion)
                
                nueva_poblacion.extend([hijo1, hijo2])
            
            self.poblacion = nueva_poblacion[:self.tamano_poblacion]
        
        return self.mejor_individuo

def optimizar_funcion_personalizada(expresion, variables, dominio, parametros=None):
    if parametros is None:
        parametros = {}
    
    def funcion_objetivo(*args):
        var_dict = dict(zip(variables, args))
        return evaluar_funcion_personalizada(expresion, var_dict)
    
    ag = AlgoritmoGenetico(
        tamano_poblacion=parametros.get('tamano_poblacion', 10),
        umbral_diferencia=parametros.get('umbral_diferencia', 0.05),
        max_iteraciones=parametros.get('max_iteraciones', 500),
        variabilidad_mutacion=parametros.get('variabilidad_mutacion', 1)
    )
    
    return ag.optimizar(funcion_objetivo, dominio)