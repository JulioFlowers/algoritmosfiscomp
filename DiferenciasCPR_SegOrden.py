import math

def Dif_progresiva_SO(f, x, h=1e-5):

    seg_derivada = (-3 * f(x) + 4 * f(x + h) - f(x + 2 * h)) / (h**2)
    return seg_derivada

def Dif_regresiva_SO(f, x, h=1e-5):

    seg_derivada = (3 * f(x) - 4 * f(x - h) + f(x - 2 * h)) / (2 * h)
    return seg_derivada

def Dif_centrada_SO(f, x, h=1e-5):

    seg_derivada = (f(x + h) - f(x - h)) / (2 * h)
    return seg_derivada

    """
    Calcular la derivada numérica de segundo orden de una función utilizando el método de las diferencias centrada,
    regresiva y progresiva.

    Parametros:
    - f: La funcion objetivo.
    - x: El punto en el que se calcula la derivada.
    - h: El tamaño del paso para la diferencia central (con 1e-5 por defecto).

    Salida:
    - seg_derivada: La derivada numerica de segundo orden  en el punto x.
    """


# Uso:
if __name__ == "__main__":
    # Definir la funcion para la cual se quiere calcular la derivada numerica de segundo orden.
    def my_function(x):
        return math.cos(x)

    # Definir el punto en el que se quiere derivar
    x = 2.0

    # Calcular la derivada numerica de segundo orden con los direrentes metodos
    segunda_derivada_progresiva = Dif_progresiva_SO(my_function, x)
    segunda_derivada_regresiva = Dif_regresiva_SO(my_function, x)
    segunda_derivada_centrada = Dif_centrada_SO(my_function, x)

    print(f"Derivada numérica de segundo orden (progresiva): {segunda_derivada_progresiva}")
    print(f"Derivada numérica de segundo orden (regresiva): {segunda_derivada_regresiva}")
    print(f"Derivada numérica de segundo orden (Centrada): {segunda_derivada_centrada}")