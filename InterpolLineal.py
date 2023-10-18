def linear_interpolation(x, x0, x1, y0, y1):
    """
    Realiza una interpolación lineal entre dos puntos de datos.

    Parámetros:
    - x: El punto en el que se desea realizar la interpolación.
    - x0, x1: Las coordenadas x de los dos puntos de datos conocidos.
    - y0, y1: Los valores y en los dos puntos de datos conocidos.

    Devuelve:
    - valor_interpolado: El valor interpolado en x.
    """

    if x0 == x1:
        raise ValueError("x0 y x1 deben ser valores distintos.")

    if x < x0 or x > x1:
        raise ValueError("x está fuera del intervalo [x0, x1]..")

    interpolated_value = y0 + (x - x0) * (y1 - y0) / (x1 - x0)
    return interpolated_value

# Ejemplo de uso:
if __name__ == "__main__":
    # Defina los puntos de datos conocidos (x0, y0) y (x1, y1)
    x0, y0 = 2, 5
    x1, y1 = 4, 9

    # Defina el punto en el que desea realizar la interpolación lineal
    x = 3

    # Realizar la interpolación lineal
    interpolated_value = linear_interpolation(x, x0, x1, y0, y1)
    print(f"Interpolated value at {x}: {interpolated_value}")
