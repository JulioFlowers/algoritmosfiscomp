import numpy as np

def cholesky_decomposition(A):
    """
    La descomposición de Cholesky es un método para descomponer una matriz hermitiana
    definida positiva en el producto de una matriz triangular inferior y su transpuesta
    conjugada, que puede utilizarse para resolver sistemas de ecuaciones lineales.

    Realice la descomposición de Cholesky en una matriz hermitiana definida positiva.

    Parámetros:
    - A: La matriz hermitiana, positiva-definida (n x n).

    Devuelve:
    - L: La matriz triangular inferior (n x n) de la descomposición Cholesky.

    """

    n = len(A)
    L = np.zeros((n, n), dtype=float)

    for i in range(n):
        for j in range(i+1):
            if i == j:
                L[i][j] = np.sqrt(A[i][i] - np.sum(L[i][k]**2 for k in range(j)))
            else:
                L[i][j] = (A[i][j] - np.sum(L[i][k] * L[j][k] for k in range(j))) / L[j][j]

    return L

def cholesky_solve(A, b):
    """
    Resuelve un sistema de ecuaciones lineales utilizando la descomposición Cholesky.

    Parámetros:
    - A: La matriz de coeficientes hermitiana y definida positiva (n x n).
    - b: El vector del lado derecho (n x 1).

    Devuelve:
    - x: El vector solución (n x 1).
    """

    L = cholesky_decomposition(A)
    Lt = np.conjugate(L).T  # Transposición conjugada de L
    y = np.linalg.solve(L, b)
    x = np.linalg.solve(Lt, y)

    return x

# Ejemplo de uso:
if __name__ == "__main__":
    # Definir la matriz de coeficientes hermitiana y definida positiva A
    A = np.array([[16, 4, 8],
                  [4, 10, 9],
                  [8, 9, 26]], dtype=float)

    # Defina el vector del lado derecho b
    b = np.array([56, 68, 167], dtype=float)

    # Resolver el sistema de ecuaciones lineales mediante la descomposición de Cholesky
    solution = cholesky_solve(A, b)
    print("Solution:")
    print(solution)
