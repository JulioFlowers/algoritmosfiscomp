def false_position(f, a, b, tol=1e-6, max_iter=100):
    """
    Metodo de falsa posicion para encontrar la raiz de una funcion.

    Parametros:
    - f: Funcion (invocable)
    - a, b: Suposiciones iniciales oara la raiz. Tal que f(a) y f(b) tienen diferente signo.
    - tol: Tolerancia (detener cuando |f(x)| < tol).
    - max_iter: Numero maxico de iteraciones. 

    Salida:
    - root: Raiz aproximada.
    - iterations: Numero de iteraciones realizadas.
    """

    if f(a) * f(b) >= 0:
        raise ValueError("las suposiciones iniciales deben ser de signo diferente")

    for i in range(max_iter):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        
        if abs(f(c)) < tol:
            return c, i

        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

    raise Exception("el metodo de falsa posicion no converge dentro del numero de iteracionnes")

# Ejemplo de uso:
if __name__ == "__main__":
    # Define la funcion a evaluar p.e.: f(x) = x^3 - x^2 + 2
    def target_function(x):
        return x**3 - x**2 + 2

    # Suposiciones iniciales
    a = -2
    b = 2

    root, iterations = false_position(target_function, a, b)
    print(f"Root: {root}")
    print(f"Iterations: {iterations}")
