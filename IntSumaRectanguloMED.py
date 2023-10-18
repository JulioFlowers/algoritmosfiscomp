def midpoint_rectangular_rule(f, a, b, n):
    """
    Aproxima la integral de una función utilizando la regla rectangular del PUNTO MEDIO.

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
        x_mid = a + (i + 0.5) * h
        integral += f(x_mid)

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

    #Realizar la integración numérica mediante la regla rectangular de PUNTO MEDIO
    integral = midpoint_rectangular_rule(my_function, a, b, n)
    print(f"Approximate integral: {integral}")
