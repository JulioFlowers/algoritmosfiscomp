import numpy as np

def gaussian_quadrature(f, a, b, n):
    """
    Aproxima la integral de una función utilizando la cuadratura de Gauss.

    Parámetros:
    - f: La función a integrar (invocable).
    - a: El límite inferior del intervalo de integración.
    - b: Límite superior del intervalo de integración.
    - n: El número de nodos y pesos a utilizar (orden de cuadratura).

    Devuelve:
    - integral: El valor aproximado de la integral.
    """

    # Definir los nodos y pesos para la cuadratura gaussiana
    nodes, weights = np.polynomial.legendre.leggauss(n)

    # Transformar nodos del intervalo [-1, 1] al intervalo [a, b]
    nodes = 0.5 * (nodes + 1) * (b - a) + a

    # Calcular la integral utilizando la cuadratura de Gauss
    integral = 0.0
    for i in range(n):
        integral += weights[i] * f(nodes[i])

    integral *= 0.5 * (b - a)

    return integral

# Ejemplo de uso:
if __name__ == "__main__":
    # Definir la función a integrar
    def my_function(x):
        return x**2

    # Definir los límites de integración y el número de nodos (orden de cuadratura)
    a = 0.0
    b = 1.0
    n = 5  # Elije un número adecuado de nodos para su función

    # Calcular la integral utilizando la cuadratura de Gauss
    integral = gaussian_quadrature(my_function, a, b, n)
    print(f"Approximate integral: {integral}")
