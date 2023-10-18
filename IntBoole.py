def boole_rule(f, a, b, n):
    """
    Aproxima la integral de una función utilizando la regla de Boole.

    Parámetros:
    - f: La función a integrar (invocable).
    - a: El límite inferior del intervalo de integración.
    - b: Límite superior del intervalo de integración.
    - n: El número de subintervalos (debe ser múltiplo de 4).

    Devuelve:
    - integral: Valor aproxiamdo de la integral. 
    """

    h = (b - a) / n
    integral = 7 * (f(a) + f(b))

    for i in range(1, n, 4):
        x0 = a + i * h
        x1 = a + (i + 1) * h
        x2 = a + (i + 2) * h
        x3 = a + (i + 3) * h

        integral += 32 * (f(x0) + f(x2)) + 12 * f(x1) + 14 * f(x3)

    integral *= 2 * h / 45

    return integral

# Ejemplo de uso:
if __name__ == "__main__":
    # Define la funcion a integrar
    def my_function(x):
        return x**2

    # Define los límites de integración y el número de subintervalos (debe ser múltiplo de 4)
    a = 0.0
    b = 1.0
    n = 16

    # Realizar la integración numérica mediante la regla de Boole
    integral = boole_rule(my_function, a, b, n)
    print(f"Approximate integral: {integral}")
