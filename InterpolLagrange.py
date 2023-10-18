import numpy as np

def lagrange_interpolation(x_data, y_data, x_interp):
    """
    Realiza la interpolación de Lagrange.

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

    y_interp = 0

    for i in range(n):
        L_i = 1
        for j in range(n):
            if j != i:
                L_i *= (x_interp - x_data[j]) / (x_data[i] - x_data[j])
        y_interp += y_data[i] * L_i

    return y_interp

# Ejemplo de uso:
if __name__ == "__main__":
    # Definir puntos de datos conocidos (x_data, y_data)
    x_data = np.array([0, 1, 2, 3, 4], dtype=float)
    y_data = np.array([0, 1, 8, 27, 64], dtype=float)

    # Definir la coordenada x en la que se desea interpolar
    x_interp = 2.5

    # Realizar la interpolación de Lagrange
    y_interp = lagrange_interpolation(x_data, y_data, x_interp)
    print(f"Interpolated value at {x_interp}: {y_interp}")
