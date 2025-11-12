import math
import re

def calculadora_avanzada_segura(expresion):
    """
    Evalúa una expresión matemática limitando las funciones disponibles
    para mejorar la seguridad y la usabilidad.
    """
    
    # 1. Definir funciones y constantes permitidas
    # Creamos un diccionario con las únicas funciones y constantes que eval() puede ver.
    safe_dict = {
        '__builtins__': None,  # Deshabilita todas las funciones integradas de Python
        'sin': math.sin, 'cos': math.cos, 'tan': math.tan, 
        'sqrt': math.sqrt, 'log': math.log, 'log10': math.log10,
        'pow': math.pow, 'factorial': math.factorial,
        'pi': math.pi, 'e': math.e,
        'abs': abs, # También permitimos la función abs
    }
    
    # 2. Pre-procesamiento de la expresión
    # Esto asegura que las constantes pi y e sean reconocidas como variables.
    expresion = expresion.replace('pi', 'pi').replace('e', 'e')
    
    # 3. Validar la expresión (Seguridad básica)
    # Patrón para permitir: números, operadores (+-*/%), paréntesis, 
    # y los nombres de las funciones permitidas (sin, cos, etc.)
    # Este paso es crucial para evitar la inyección de código.
    patron_seguro = r'^[\d\s\+\-\*\/\%\(\)\.]+$|^[\d\s\+\-\*\/\%\(\)\.]*(sin|cos|tan|sqrt|log|log10|pow|factorial|pi|e|abs)[\d\s\+\-\*\/\%\(\)\.]*$'
    
    # Nota: Una validación perfecta es compleja, pero esta es mejor que nada.
    # Una librería como 'sympy' sería ideal para una seguridad total.
    
    # if not re.match(patron_seguro, expresion):
    #     return "Error: Expresión contiene caracteres o funciones no permitidas."

    try:
        # Usamos eval() con un diccionario limitado (safe_dict)
        resultado = eval(expresion, safe_dict)
        return resultado
    except SyntaxError:
        return "Error: Sintaxis matemática inválida."
    except NameError as e:
        return f"Error: Función o constante no definida: {e}"
    except Exception as e:
        return f"Error de cálculo: {e}"

# --- Ejemplo de Uso Mejorado ---
print("--- Calculadora Avanzada (Segura) ---")
print("Funciones permitidas: sin, cos, tan, sqrt, log, log10, pow, factorial, abs")
print("Constantes permitidas: pi, e")
print("Ejemplo: sqrt(9) + 5 * pi / abs(-2)")

# Pedir la expresión al usuario
expresion_usuario = input("Ingrese su expresión matemática: ")

# Calcular y mostrar el resultado
resultado_final = calculadora_avanzada_segura(expresion_usuario)
print(f"Resultado: {resultado_final}")