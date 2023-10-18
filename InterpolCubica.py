import numpy as np

def cubic_spline_interpolation(x_data, y_data, x_interp):
    """
    Realiza la interpolación spline cúbica (sin usar SciPy xd)

    Parametros:
    - x_data: Una matriz de coordenadas x de puntos de datos conocidos.
    - y_data: Una matriz de coordenadas y de puntos de datos conocidos.
    - x_interp: La coordenada x donde se desea interpolar.

    Returns:
    - y_interp: El valor interpolado en x_interp.
    """

    n = len(x_data)
    if n < 4:
        raise ValueError("La interpolación spline cúbica requiere al menos 4 puntos de datos.")

    h = np.diff(x_data)
    delta_y = np.diff(y_data)

    A = np.zeros((n, n))
    b = np.zeros(n)

    for i in range(1, n - 1):
        A[i, i - 1] = h[i - 1]
        A[i, i] = 2 * (h[i - 1] + h[i])
        A[i, i + 1] = h[i]
        b[i] = 3 * (delta_y[i] / h[i] - delta_y[i - 1] / h[i - 1])

    # Condiciones límite naturales
    A[0, 0] = 1
    A[n - 1, n - 1] = 1

    # Resuelve el sistema lineal tridiagonal para las segundas derivadas
    second_derivatives = np.linalg.solve(A, b)

    for i in range(n - 1, 0, -1):
        if x_interp >= x_data[i]:
            break

    h_i = x_data[i + 1] - x_data[i]
    delta_x = x_interp - x_data[i]
    a = (second_derivatives[i + 1] - second_derivatives[i]) / (6 * h_i)
    b = second_derivatives[i] / 2
    c = (y_data[i + 1] - y_data[i]) / h_i - h_i * (second_derivatives[i + 1] + 2 * second_derivatives[i]) / 6
    y_interp = y_data[i] + (a * delta_x**3 + b * delta_x**2 + c * delta_x)

    return y_interp

# Ejemplo de uso:
if __name__ == "__main__":
    # Definir puntos de datos conocidos (x_data, y_data)
    x_data = np.array([0, 1, 2, 3, 4], dtype=float)
    y_data = np.array([0, 1, 8, 27, 64], dtype=float)

    # Definir la coordenada x en la que se desea interpolar
    x_interp = 2.5

    # Realizar interpolación spline cúbica
    y_interp = cubic_spline_interpolation(x_data, y_data, x_interp)
    print(f"Interpolated value at {x_interp}: {y_interp}")
