import numpy as np

def crout_lu_decomposition(A):
    """
    Hacer una descomposicion LU usando el metodo de Crout.

    Parametros:
    - A: La matriz cuadrada inicial.

    Salida:
    - L: Matriz triangular inferior.
    - U: Matriz triangular superior.
    """

    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        L[i][i] = 1

        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
        
        for j in range(i + 1, n):
            L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

    return L, U

# Ejemplo de uso:
if __name__ == "__main__":
    # Define la matrix cuadrada A
    A = np.array([[4, 3, 2],
                  [2, 2, 3],
                  [3, 5, 5]], dtype=float)

    L, U = crout_lu_decomposition(A)
    print("Matriz A:")
    print(A)
    print("Matriz triangular inferior L:")
    print(L)
    print("Matriz triangular superior U:")
    print(U)
