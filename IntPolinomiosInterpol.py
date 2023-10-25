import numpy as np

def lagrange_interpolation(x_data, y_data, x):
    """
    Realiza la interpolación de Lagrange para estimar el valor de una función en un punto concreto.

    Los polinomios interpolantes pueden utilizarse para la integración numérica cuando
    se aproxima la integral de una función utilizando un polinomio que interpola
    la función en puntos de datos seleccionados.

    Parametros:
    - x_data: Una matriz de coordenadas x de puntos de datos conocidos.
    - y_data: Una matriz de coordenadas y de puntos de datos conocidos.
    - x: Punto en el que se desea obtener el valor interpolado.

    devuelve:
    - interpolated_value: El valor estimado en el punto dado.
    """

    n = len(x_data)
    interpolated_value = 0

    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if j != i:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        interpolated_value += term

    return interpolated_value

def interpolating_polynomial_integration(x_data, y_data, a, b):
    """
    Aproximar la integral de una función mediante polinomios interpolantes.

    Parameters:
    - x_data:  Una matriz de coordenadas x de puntos de datos conocidos.
    - y_data:  Una matriz de coordenadas y de puntos de datos conocidos.
    - a: El límite inferior del intervalo de integración.
    - b: El límite superior del intervalo de integración.

    devuelve:
    - integral: el valor apooroximado de la integral
    """

    # Calcular el número de puntos de datos
    n = len(x_data)

    # Iniciar la integral
    integral = 0

    # Realizar la integración utilizando el polinomio interpolador
    for i in range(n - 1):
        x1, x2 = x_data[i], x_data[i + 1]
        if x2 <= a or x1 >= b:
            continue  # Saltar intervalos que no intersectan [a, b]

        # Recorta el intervalo de integración al intervalo de puntos de datos
        x1 = max(x1, a)
        x2 = min(x2, b)

        # Utiliza la interpolación de Lagrange para estimar la integral dentro del intervalo
        integral += lagrange_interpolation(x_data, y_data, x1) * (x2 - x1)

    return integral

# Ejemplo de uso:
if __name__ == "__main__":
    # Definir puntos de datos conocidos (x_data, y_data)
    x_data = np.array([0, 1, 2, 3, 4], dtype=float)
    y_data = np.array([0, 1, 8, 27, 64], dtype=float)

    # Define los limites de integracion
    a = 1.0
    b = 3.0

    # Integración numérica mediante polinomios interpolantes
    integral = interpolating_polynomial_integration(x_data, y_data, a, b)
    print(f"Approximate integral: {integral}")
