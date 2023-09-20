import numpy as np

def gauss_elimination(A, b):
    """
    Resolver un sistema de ecuaciones lineales usando el metodo de Gauss.

    Parametros:
    - A: La matriz coeficiente (n x n).
    - b: El vector del lado derecho (n x 1).

    Salida:
    - x: El vector solucion (n x 1).
    """

    n = len(A)
    augmented_matrix = np.hstack((A, b.reshape(-1, 1)))

    # Eliminacion
    for i in range(n):
        pivot_row = np.argmax(np.abs(augmented_matrix[i:, i])) + i
        augmented_matrix[[i, pivot_row]] = augmented_matrix[[pivot_row, i]]

        for j in range(i + 1, n):
            factor = augmented_matrix[j, i] / augmented_matrix[i, i]
            augmented_matrix[j, i:] -= factor * augmented_matrix[i, i:]

    # Sustitucion
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (augmented_matrix[i, -1] - np.dot(augmented_matrix[i, i+1:-1], x[i+1:])) / augmented_matrix[i, i]

    return x

# Ejemplo de uso:
if __name__ == "__main__":
    # Define la matriz coeficiente A y el vector derecho b
    A = np.array([[2, -1, 1],
                  [-1, 3, 2],
                  [1, 2, 4]], dtype=float)
    b = np.array([6, 25, -11], dtype=float)

    solution = gauss_elimination(A, b)
    print("Solution:")
    print(solution)
