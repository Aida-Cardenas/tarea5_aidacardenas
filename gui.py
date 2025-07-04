import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import sys
import time
from funciones import FUNCIONES_PREDEFINIDAS
from algoritmo_genetico import AlgoritmoGenetico, optimizar_funcion_personalizada

class RedirectText:
    def __init__(self, text_widget):
        self.text_widget = text_widget
    
    def write(self, string):
        self.text_widget.configure(state='normal')
        self.text_widget.insert(tk.END, string)
        self.text_widget.configure(state='disabled')
        self.text_widget.see(tk.END)
    
    def flush(self):
        pass

class AlgoritmoGeneticoGUI:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Algoritmo Genético - Optimización de Funciones")
        self.root.geometry("900x700")
        self.root.configure(bg='#f0f0f0')
        
        self.ejecutando = False
        self.crear_widgets()
        self.redirigir_salida()
    
    def crear_widgets(self):
    
        title_frame = ttk.Frame(self.root)
        title_frame.pack(fill='x', padx=10, pady=5)
        ttk.Label(title_frame, text="🧬 Algoritmo Genético - Optimización de Funciones", 
                  font=('Arial', 14, 'bold')).pack()
        

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=5)
        
        self.crear_pestana_predefinidas()
        self.crear_pestana_personalizada()
        self.crear_pestana_parametros()
        self.crear_area_resultados()
        self.crear_botones_control()
    
    def crear_pestana_predefinidas(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Funciones Predefinidas")
        
        ttk.Label(frame, text="Seleccione una función predefinida:", 
                  font=('Arial', 11, 'bold')).pack(anchor='w', padx=10, pady=5)
        
        self.funcion_predefinida = tk.StringVar(value="unidimensional")
        
        ttk.Radiobutton(frame, text="Función Unidimensional: y = sin²(x)/x", 
                       variable=self.funcion_predefinida, value="unidimensional").pack(anchor='w', padx=20)
        
        ttk.Radiobutton(frame, text="Función Bidimensional: z = 20 + x - 10·cos(2π·x) + y - 10·cos(2π·y)", 
                       variable=self.funcion_predefinida, value="bidimensional").pack(anchor='w', padx=20)
        
        info_frame = ttk.LabelFrame(frame, text="Información")
        info_frame.pack(fill='x', padx=10, pady=10)
        
        info_text = tk.Text(info_frame, height=8, wrap='word', bg='#f8f8f8')
        info_text.pack(fill='x', padx=5, pady=5)
        
        info_content = """• Función Unidimensional: Busca el valor de x en [-10, 10] que maximiza y = sin²(x)/x
• Función Bidimensional: Busca los valores de x, y en [-10, 10] que maximizan la función dada
• Ambas funciones utilizan el dominio [-10, 10] para todas las variables
• El algoritmo genético encontrará el máximo global o local de la función seleccionada

Dominio: [-10, 10] para todas las variables"""
        
        info_text.insert('1.0', info_content)
        info_text.configure(state='disabled')
    
    def crear_pestana_personalizada(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Función Personalizada")
        
        ttk.Label(frame, text="Defina su función personalizada:", 
                  font=('Arial', 11, 'bold')).pack(anchor='w', padx=10, pady=5)
        
        var_frame = ttk.Frame(frame)
        var_frame.pack(fill='x', padx=10, pady=5)
        
        ttk.Label(var_frame, text="Número de variables:").pack(side='left')
        self.num_variables = tk.StringVar(value="1")
        combo = ttk.Combobox(var_frame, textvariable=self.num_variables, values=["1", "2"], 
                           state='readonly', width=5)
        combo.pack(side='left', padx=5)
        combo.bind('<<ComboboxSelected>>', self.actualizar_variables)
        
        ttk.Label(frame, text="Expresión matemática:").pack(anchor='w', padx=10, pady=(10,0))
        self.expresion_funcion = tk.StringVar(value="sin(x)**2 / x")
        ttk.Entry(frame, textvariable=self.expresion_funcion, width=60).pack(padx=10, pady=5)
        
        dominio_frame = ttk.LabelFrame(frame, text="Dominio de las Variables")
        dominio_frame.pack(fill='x', padx=10, pady=10)
        
        var1_frame = ttk.Frame(dominio_frame)
        var1_frame.pack(fill='x', padx=5, pady=2)
        
        ttk.Label(var1_frame, text="Variable x:").pack(side='left')
        ttk.Label(var1_frame, text="Mín:").pack(side='left', padx=(20,0))
        self.x_min = tk.StringVar(value="-10")
        ttk.Entry(var1_frame, textvariable=self.x_min, width=8).pack(side='left', padx=2)
        ttk.Label(var1_frame, text="Máx:").pack(side='left', padx=(10,0))
        self.x_max = tk.StringVar(value="10")
        ttk.Entry(var1_frame, textvariable=self.x_max, width=8).pack(side='left', padx=2)
        
        self.var2_frame = ttk.Frame(dominio_frame)
        ttk.Label(self.var2_frame, text="Variable y:").pack(side='left')
        ttk.Label(self.var2_frame, text="Mín:").pack(side='left', padx=(20,0))
        self.y_min = tk.StringVar(value="-10")
        ttk.Entry(self.var2_frame, textvariable=self.y_min, width=8).pack(side='left', padx=2)
        ttk.Label(self.var2_frame, text="Máx:").pack(side='left', padx=(10,0))
        self.y_max = tk.StringVar(value="10")
        ttk.Entry(self.var2_frame, textvariable=self.y_max, width=8).pack(side='left', padx=2)
        
        ejemplos_frame = ttk.LabelFrame(frame, text="Ejemplos de Funciones")
        ejemplos_frame.pack(fill='x', padx=10, pady=10)
        
        ejemplos_text = tk.Text(ejemplos_frame, height=6, wrap='word', bg='#f8f8f8')
        ejemplos_text.pack(fill='x', padx=5, pady=5)
        
        ejemplos_content = """Una Variable: sin(x)**2 / x, exp(-x**2), x**3 - 2*x**2 + x, abs(x) * cos(x)
Dos Variables: x**2 + y**2, sin(x) * cos(y), exp(-(x**2 + y**2)), x*y - x**2 - y**2

Funciones: sin, cos, tan, exp, log, sqrt, abs, pow
Constantes: pi, e  //  Operadores: +, -, *, /, **, ()"""
        
        ejemplos_text.insert('1.0', ejemplos_content)
        ejemplos_text.configure(state='disabled')
    
    def crear_pestana_parametros(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Parámetros")
        
        ttk.Label(frame, text="Configuración del Algoritmo Genético:", 
                  font=('Arial', 11, 'bold')).pack(anchor='w', padx=10, pady=5)
        
        params_frame = ttk.LabelFrame(frame, text="Parámetros")
        params_frame.pack(fill='x', padx=10, pady=10)
        
        params = [
            ("Tamaño de la población:", "tamano_poblacion", "10"),
            ("Umbral de diferencia:", "umbral_diferencia", "0.05"),
            ("Número máximo de iteraciones:", "max_iteraciones", "500"),
            ("Variabilidad de la mutación:", "variabilidad_mutacion", "1")
        ]
        
        for label, attr, default in params:
            param_frame = ttk.Frame(params_frame)
            param_frame.pack(fill='x', padx=5, pady=5)
            
            ttk.Label(param_frame, text=label).pack(side='left')
            setattr(self, attr, tk.StringVar(value=default))
            ttk.Entry(param_frame, textvariable=getattr(self, attr), width=10).pack(side='right')
    
    def crear_area_resultados(self):
        results_frame = ttk.LabelFrame(self.root, text="Resultados de la Optimización")
        results_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        self.resultado_text = scrolledtext.ScrolledText(results_frame, height=10, wrap='word', 
                                                       bg='#000000', fg='#00ff00', 
                                                       font=('Courier', 9))
        self.resultado_text.pack(fill='both', expand=True, padx=5, pady=5)
        
        self.resultado_text.insert('1.0', "🧬 Bienvenido al Algoritmo Genético\n")
        self.resultado_text.insert('end', "Seleccione una función y presione 'Ejecutar Optimización'\n")
        self.resultado_text.insert('end', "="*60 + "\n")
        self.resultado_text.configure(state='disabled')
    
    def crear_botones_control(self):
        button_frame = ttk.Frame(self.root)
        button_frame.pack(fill='x', padx=10, pady=5)
        
        self.btn_ejecutar = ttk.Button(button_frame, text="🚀 Ejecutar Optimización", 
                                      command=self.ejecutar_optimizacion)
        self.btn_ejecutar.pack(side='left', padx=5)
        
        ttk.Button(button_frame, text="🧹 Limpiar", 
                  command=self.limpiar_resultados).pack(side='left', padx=5)
        
        ttk.Button(button_frame, text="❌ Salir", 
                  command=self.root.quit).pack(side='right', padx=5)
        
        self.progress = ttk.Progressbar(button_frame, mode='indeterminate')
        self.progress.pack(side='left', fill='x', expand=True, padx=20)
    
    def actualizar_variables(self, event=None):
        if self.num_variables.get() == "2":
            self.var2_frame.pack(fill='x', padx=5, pady=2)
        else:
            self.var2_frame.pack_forget()
    
    def redirigir_salida(self):
        self.redirect_text = RedirectText(self.resultado_text)
    
    def limpiar_resultados(self):
        self.resultado_text.configure(state='normal')
        self.resultado_text.delete('1.0', tk.END)
        self.resultado_text.configure(state='disabled')
    
    def obtener_parametros(self):
        try:
            return {
                'tamano_poblacion': int(self.tamano_poblacion.get()),
                'umbral_diferencia': float(self.umbral_diferencia.get()),
                'max_iteraciones': int(self.max_iteraciones.get()),
                'variabilidad_mutacion': float(self.variabilidad_mutacion.get())
            }
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduzca valores numéricos válidos.")
            return None
    
    def ejecutar_optimizacion(self):
        if self.ejecutando:
            messagebox.showwarning("Advertencia", "Ya hay una optimización en ejecución.")
            return
        
        parametros = self.obtener_parametros()
        if parametros is None:
            return
        
        self.ejecutando = True
        self.btn_ejecutar.configure(state='disabled')
        self.progress.start()
        
        thread = threading.Thread(target=self.ejecutar_optimizacion_thread, args=(parametros,))
        thread.daemon = True
        thread.start()
    
    def ejecutar_optimizacion_thread(self, parametros):
        try:
            old_stdout = sys.stdout
            sys.stdout = self.redirect_text
            
            if self.notebook.tab(self.notebook.select(), "text") == "Funciones Predefinidas":
                self.optimizar_predefinida(parametros)
            else:
                self.optimizar_personalizada(parametros)
                
        except Exception as e:
            messagebox.showerror("Error", f"Error durante la optimización: {str(e)}")
        finally:
            sys.stdout = old_stdout
            self.root.after(0, self.finalizar_optimizacion)
    
    def optimizar_predefinida(self, parametros):
        tipo_funcion = self.funcion_predefinida.get()
        config = FUNCIONES_PREDEFINIDAS[tipo_funcion]
        
        print(f"\n{'='*60}")
        print(f"OPTIMIZACIÓN DE FUNCIÓN {tipo_funcion.upper()}")
        print(f"{'='*60}")
        print(f"Función: {config['nombre']}")
        print(f"Dominio: {config['dominio']}")
        print(f"Parámetros: {parametros}")
        print("-" * 60)
        
        ag = AlgoritmoGenetico(**parametros)
        
        inicio = time.time()
        mejor_individuo = ag.optimizar(config['funcion'], config['dominio'])
        fin = time.time()
        
        print("-" * 60)
        print("RESULTADOS:")
        print(f"Tiempo: {fin - inicio:.2f} segundos")
        print(f"Mejor valor: {mejor_individuo.fitness:.8f}")
        
        if len(mejor_individuo.genes) == 1:
            print(f"x óptimo: {mejor_individuo.genes[0]:.8f}")
        else:
            for i, var in enumerate(config['variables']):
                print(f"{var} óptimo: {mejor_individuo.genes[i]:.8f}")
        
        print(f"Generaciones: {len(ag.historial_fitness)}")
        print("=" * 60)
    
    def optimizar_personalizada(self, parametros):
        try:
            expresion = self.expresion_funcion.get().strip()
            if not expresion:
                messagebox.showerror("Error", "Introduzca una expresión matemática.")
                return
            
            num_vars = int(self.num_variables.get())
            variables = ['x'] if num_vars == 1 else ['x', 'y']
            
            dominio = []
            try:
                dominio.append((float(self.x_min.get()), float(self.x_max.get())))
                if num_vars == 2:
                    dominio.append((float(self.y_min.get()), float(self.y_max.get())))
            except ValueError:
                messagebox.showerror("Error", "Valores de dominio inválidos.")
                return
            
            print(f"\n{'='*60}")
            print("OPTIMIZACIÓN DE FUNCIÓN PERSONALIZADA")
            print(f"{'='*60}")
            print(f"Función: {expresion}")
            print(f"Variables: {variables}")
            print(f"Dominio: {dominio}")
            print(f"Parámetros: {parametros}")
            print("-" * 60)
            
            inicio = time.time()
            mejor_individuo = optimizar_funcion_personalizada(expresion, variables, dominio, parametros)
            fin = time.time()
            
            print("-" * 60)
            print("RESULTADOS:")
            print(f"Tiempo: {fin - inicio:.2f} segundos")
            print(f"Mejor valor: {mejor_individuo.fitness:.8f}")
            
            for i, var in enumerate(variables):
                print(f"{var} óptimo: {mejor_individuo.genes[i]:.8f}")
            
            print("=" * 60)
            
        except Exception as e:
            print(f"Error: {str(e)}")
            messagebox.showerror("Error", f"Error: {str(e)}")
    
    def finalizar_optimizacion(self):
        self.ejecutando = False
        self.btn_ejecutar.configure(state='normal')
        self.progress.stop()

def main():
    root = tk.Tk()
    app = AlgoritmoGeneticoGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()