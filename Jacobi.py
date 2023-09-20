import numpy as np

def jacobi_method(A, b, x0, tol=1e-6, max_iter=100):
    """
    Resuelve un systema de ecuaciones lineales Ax=b usando el metodo de Jacobi.

    Parametros:
    - A: el coeficiente de la matriz (n x n). 
    - b: el vector del lado derecho (n x 1).
    - x0: La suposicion inicial de la solucion (n x 1).
    - tol: Tolerancia (detener cuando ||Ax - b|| < tol).
    - max_iter: maximo numero de iteraciones.

    Salida:
    - x: Solucion aproximada.
    - iterations: Numero de iteraciones realizadas.
    """

    n = len(A)
    x = x0.copy()

    for iteration in range(max_iter):
        x_new = np.zeros_like(x)

        for i in range(n):
            sigma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sigma) / A[i][i]

        if np.linalg.norm(np.dot(A, x) - b) < tol:
            return x, iteration

        x = x_new

    raise Exception("El metodo de Jacobi no converge en el numero de iteraciones propuesto")

# Ejemplo de uso:
if __name__ == "__main__":
    # Definir el coeficiente de la matriz A y el vector del lado derecho b
    A = np.array([[10, -1, 2],
                  [-1, 11, -1],
                  [2, -1, 10]], dtype=float)
    b = np.array([6, 25, -11], dtype=float)

    # Suposicion inicial de la solucion
    x0 = np.zeros(len(b), dtype=float)

    solution, iterations = jacobi_method(A, b, x0)
    print("Solution:")
    print(solution)
    print("Number of iterations:", iterations)
