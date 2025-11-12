import math

# --- Funciones Wrapper (para manejar GRADOS) ---
def sin_grados(x):
    return math.sin(math.radians(x))

def cos_grados(x):
    return math.cos(math.radians(x))

def tan_grados(x):
    return math.tan(math.radians(x))

def calculadora_final_estable(expresion):
    """
    Evalúa una expresión permitiendo operaciones básicas y funciones 
    trigonométricas en grados, usando un scope seguro.
    """
    
    # 1. Definir el scope seguro (lo único accesible para eval())
    safe_scope = {
        '__builtins__': None,  # Deshabilita todas las funciones integradas
        
        # Operadores
        'sum': sum,
        
        # Funciones trigonométricas (usan grados)
        'sin': sin_grados, 'cos': cos_grados, 'tan': tan_grados, 
        
        # Otras funciones de math (usan radianes o valores normales)
        'sqrt': math.sqrt, 'log': math.log, 'log10': math.log10,
        'pow': math.pow, 'factorial': math.factorial,
        
        # Funciones generales
        'abs': abs, 'round': round,
        
        # Constantes
        'pi': math.pi, 'e': math.e,
        
        # Para forzar el uso de radianes si el usuario lo desea
        'radians': math.radians 
    }
    
    try:
        # 2. Evaluar la expresión usando únicamente el scope seguro
        # Esto soluciona problemas de conflicto de strings
        resultado = eval(expresion, safe_scope)
        return resultado
    except SyntaxError:
        return "Error: Sintaxis matemática inválida."
    except NameError:
        # Esto incluye si el usuario intenta usar una función no definida
        return "Error: Función o constante no permitida o mal escrita."
    except Exception as e:
        return f"Error de cálculo: {e}"

# --- Ejemplo de Uso ---
print("--- Calculadora (Estable) ---")
print("¡Las funciones sin, cos, tan ahora usan GRADOS!")
print("Ejemplo: tan(30) + sin(90) + sqrt(16)")

# Pedir la expresión al usuario
expresion_usuario = input("Ingrese su expresión matemática: ")

# Calcular y mostrar el resultado
resultado_final = calculadora_final_estable(expresion_usuario)
print(f"Resultado: {resultado_final}")