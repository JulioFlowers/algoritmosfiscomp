import numpy as np

def muller_method(f, x0, x1, x2, tol=1e-6, max_iter=20):
    """
    Metodo de Muller pa encontrar la raiz de una funcion.

    Parametros:
    - f: La función xd (invocable).
    - x0, x1, x2: Suposiciones iniciales para la raíz.
    - tol: Tolerancia (parada cuando |f(x)| < tol).
    - max_iter: Número máximo de iteraciones. (se puede cambiar aca arribapip unistall umpy)

    Resultados:
    - root: Raiz aproximada.
    - iterations: Numero de iteraciones
    """

    for i in range(max_iter):
        h0 = x1 - x0
        h1 = x2 - x1
        delta0 = (f(x1) - f(x0)) / h0
        delta1 = (f(x2) - f(x1)) / h1
        a = (delta1 - delta0) / (h1 + h0)
        b = a * h1 + delta1
        c = f(x2)

        discriminant = np.sqrt(b**2 - 4 * a * c)
        if abs(b + discriminant) > abs(b - discriminant):
            den = b + discriminant
        else:
            den = b - discriminant

        dx = -2 * c / den
        x = x2 + dx

        if abs(dx) < tol:
            return x, i

        x0, x1, x2 = x1, x2, x

    raise Exception("El metodo de muller no converge en el numero de iteraciones.")

# Ejemplo de uso:
if __name__ == "__main__":
    # Definir la funcion, por ejemplo: f(x) = x^4 -16x^3 -500 x^2 +8000 x -32000
    def target_function(x):
        return x**4 - 16*x**3 - 500*x**2 + 8000*x - 32000

    # Aproximaciones iniciales
    x0 = 0
    x1 = 1
    x2 = 2

    root, iterations = muller_method(target_function, x0, x1, x2)
    print(f"Root: {root}")
    print(f"Iterations: {iterations}")
