def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    """
    Metodo de Newton-Raphson para encontrar la raiz de una funcion.

    Parametros:
    - f: La funcion objetivo.
    - df: La derivada de la funcion objetivo.
    - x0: Suposicion inicial para la raiz.
    - tol: Tolerancia (detenerse cuando |f(x)| < tol).
    - max_iter: Maximo numero de iteraciones.

    Salida:
    - root: Raiz aproximada
    - iterations: Numero de iteraciones realizadas.
    """

    x = x0

    for i in range(max_iter):
        delta_x = f(x) / df(x)
        x -= delta_x

        if abs(delta_x) < tol:
            return x, i

    raise Exception("El metodo de Newton-Raphson no converge en las iteraciones dadas")

# Ejemplo de uso:
if __name__ == "__main__":
    # Define la funcion y su derivada.
    def target_function(x):
        return x**3 - 2*x**2 + 4*x - 8

    def derivative_function(x):
        return 3*x**2 - 4*x + 4

    # Suposicion inicial.
    x0 = 2.0

    root, iterations = newton_raphson(target_function, derivative_function, x0)
    print(f"Root: {root}")
    print(f"Iterations: {iterations}")
