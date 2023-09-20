import numpy as np

def doolittle_lu_decomposition(A):
    """
    Para hacer una descomposicion LU usando el metodo de Doolitle.

    Parametros:
    - A: El input de la matriz cuadrada.

    Salida:
    - L: Matriz triangular inferior.
    - U: Matriz triangular superior.
    """

    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        L[i][i] = 1

        for k in range(i, n):
            U[i][k] = A[i][k] - sum(L[i][j] * U[j][k] for j in range(i))
        
        for j in range(i + 1, n):
            L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

    return L, U

# Example usage:
if __name__ == "__main__":
    # Define the square matrix A
    A = np.array([[2, -1, 1],
                  [-1, 3, 2],
                  [1, 2, 4]], dtype=float)

    L, U = doolittle_lu_decomposition(A)
    print("Matrix A:")
    print(A)
    print("Matriz triangular inferior L:")
    print(L)
    print("Matriz triangular superior U:")
    print(U)
