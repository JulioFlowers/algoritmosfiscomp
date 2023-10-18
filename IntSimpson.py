def simpsons_rule(f, a, b, n):
    """
    Aproxima la integral de una función utilizando la regla de Simpson.

    Parámetros:
    - f: La función a integrar (invocable).
    - a: El límite inferior del intervalo de integración.
    - b: El límite superior del intervalo de integración.
    - n: El número de subintervalos (debe ser par).

    devuelve:
    - integral: valor aproximado de la integral.
    """

    if n % 2 != 0:
        raise ValueError("El número de subintervalos (n) debe ser par para la regla de Simpson.")

    h = (b - a) / n
    integral = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        integral += 4 * f(x) if i % 2 != 0 else 2 * f(x)

    integral *= h / 3

    return integral

# Ejemplo de uso:
if __name__ == "__main__":
    # Define la funcion a integrar
    def my_function(x):
        return x**2

    # Defina los límites de integración y el número de subintervalos (deben ser pares)
    a = 0.0
    b = 1.0
    n = 4  # pon un número adecuado de subintervalos para la función

    # Realizar la integración numérica mediante la regla de Simpson
    integral = simpsons_rule(my_function, a, b, n)
    print(f"Approximate integral: {integral}")
