import numpy as np

def newton_interpolation(x_data, y_data, x_interp):
    """
    Realiza la interpolación por diferencias divididas de Newton.

    Parametros:
    - x_data: Una matriz de coordenadas x de puntos de datos conocidos.
    - y_data: Una matriz de coordenadas y de puntos de datos conocidos.
    - x_interp: La coordenada x donde se desea interpolar.

    Returns:
    - y_interp: El valor interpolado en x_interp.
    """

    n = len(x_data)
    if n != len(y_data):
        raise ValueError("El número de puntos de datos x e y debe ser igual.")

    # Calcular diferencias divididas
    divided_diff = np.zeros((n, n))
    divided_diff[:, 0] = y_data

    for j in range(1, n):
        for i in range(n - j):
            divided_diff[i][j] = (divided_diff[i + 1][j - 1] - divided_diff[i][j - 1]) / (x_data[i + j] - x_data[i])

    # Iniciar el valor interpolado
    y_interp = 0

    for j in range(n):
        term = divided_diff[0][j]
        for i in range(j):
            term *= (x_interp - x_data[i])
        y_interp += term

    return y_interp

# Ejemplo de uso:
if __name__ == "__main__":
    # Definir puntos de datos conocidos(x_data, y_data)
    x_data = np.array([0, 1, 2, 3, 4], dtype=float)
    y_data = np.array([0, 1, 8, 27, 64], dtype=float)

    # Definir la coordenada x en la que se desea interpolar
    x_interp = 2.5

    # Realizar la interpolación por diferencias divididas de Newton
    y_interp = newton_interpolation(x_data, y_data, x_interp)
    print(f"Interpolated value at {x_interp}: {y_interp}")
