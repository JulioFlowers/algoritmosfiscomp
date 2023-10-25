def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    """
    Metodo de la secante para encontrar la raiz de una funcion.

    Parametros:
    - f: La funcion
    - x0, x1: Suposiciones iniciales para la raiz.
    - tol: Tolerancia (detenerse cuando |f(x)| < tol).
    - max_iter: Maximo numero de iteraciones.

    Salida:
    - root: Raiz aproximada.
    - iterations: Numero de iteraciones realizadas.
    """

    for i in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)

        if abs(f_x1) < tol:
            return x1, i

        if abs(f_x0 - f_x1) < tol:
            raise Exception("Se detuvo el metodo de la secante porque el denominador es demasiado pequeño")

        x_new = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        x0, x1 = x1, x_new

    raise Exception("El metodo de la secante no converge en el numero de iteraciones dado")

# Ejemplo de uso:
if __name__ == "__main__":
    # Define la funcion, pe: f(x) = x^3 - x^2 + 2
    def target_function(x):
        return x**3 - x**2 + 2

    # Suposiciones iniciales
    x0 = 0
    x1 = 1

    root, iterations = secant_method(target_function, x0, x1)
    print(f"Root: {root}")
    print(f"Iterations: {iterations}")
