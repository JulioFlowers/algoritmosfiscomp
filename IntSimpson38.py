def simpsons_3_8_rule(f, a, b, n):
    """
    Aproxima la integral de una función utilizando la regla 3/8 de Simpson.
    
    Parámetros:
    - f: La función a integrar (invocable).
    - a: El límite inferior del intervalo de integración.
    - b: El límite superior del intervalo de integración.
    - n: Numero de subintervalos (debe de ser multiplo de 3).

    Devuelve:
    - integral: Valor aproximado de la integral.
    """

    if n % 3 != 0:
        raise ValueError("El número de subintervalos (n) debe ser múltiplo de 3 para la regla 3/8 de Simpson.")

    h = (b - a) / n
    integral = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        integral += 3 * f(x) if i % 3 == 0 else 2 * f(x)

    integral *= (3 * h) / 8

    return integral

# Ejemplo de uso:
if __name__ == "__main__":
    # Define la funcion a integrar
    def my_function(x):
        return x**2

    # Define los límites de integración y el número de subintervalos (debe ser múltiplo de 3)
    a = 0.0
    b = 1.0
    n = 9  # Nuemro de subintervalos apropiados para la funcion

    # Realizar la integración numérica mediante la regla 3/8 de Simpson
    integral = simpsons_3_8_rule(my_function, a, b, n)
    print(f"Approximate integral: {integral}")
