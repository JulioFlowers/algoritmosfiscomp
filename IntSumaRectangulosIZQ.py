def left_rectangular_rule(f, a, b, n):
    """
    Aproxima la integral de una función utilizando la regla rectangular izquierda.

    Se pueden crear funciones similares para la regla rectangular derecha o
    del punto medio ajustando la posición del rectángulo con respecto
    a los valores de la función.

    Parametros:
    - f: La función a integrar (invocable).
    - a: El límite inferior del intervalo de integración.
    - b: Límite superior del intervalo de integración.
    - n: El número de subintervalos (rectángulos).

    Devuelve:
    - integral: El valor aproximado de la integral.
    """

    h = (b - a) / n
    integral = 0.0

    for i in range(n):
        x = a + i * h
        integral += f(x)

    integral *= h

    return integral

# Ejemplo de Uso:
if __name__ == "__main__":
    # Define la funcion a integrar
    def my_function(x):
        return x**2

    # Define los límites de integración y el número de subintervalos
    a = 0.0
    b = 1.0
    n = 100

    # Realizar la integración numérica mediante la regla rectangular izquierda
    integral = left_rectangular_rule(my_function, a, b, n)
    print(f"Approximate integral: {integral}")
