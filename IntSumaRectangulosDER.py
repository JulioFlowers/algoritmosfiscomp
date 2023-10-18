def right_rectangular_rule(f, a, b, n):
    """
    Aproxima la integral de una función utilizando la regla rectangular DERECHA.

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

    for i in range(1, n + 1):
        x = a + i * h
        integral += f(x)

    integral *= h

    return integral

# Ejemplo de uso:
if __name__ == "__main__":
    # Define la funcion a integrar
    def my_function(x):
        return x**2

    # Define los límites de integración y el número de subintervalos
    a = 0.0
    b = 1.0
    n = 100

    # Realizar la integración numérica mediante la regla rectangular DERECHA
    integral = right_rectangular_rule(my_function, a, b, n)
    print(f"Approximate integral: {integral}")
