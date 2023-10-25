def bilinear_interpolation(x, y, x0, y0, x1, y1, f00, f01, f10, f11):
    """
    Realiza una interpolación bilineal.

    Parámetros:
    - x, y: Las coordenadas del punto donde se desea realizar la interpolación.
    - x0, y0, x1, y1: Las coordenadas de los cuatro puntos de la cuadrícula circundantes.
    - f00, f01, f10, f11: Los valores en los cuatro puntos de la cuadrícula.

    Devuelve:
    - interpolated_value: El valor interpolado en (x, y).
    """

    if x0 == x1 or y0 == y1:
        raise ValueError("Los puntos de la cuadrícula deben formar un rectángulo.")

    if x < x0 or x > x1 or y < y0 or y > y1:
        raise ValueError("El punto está fuera de la cuadricula")

    alpha = (x - x0) / (x1 - x0)
    beta = (y - y0) / (y1 - y0)

    interpolated_value = (1 - alpha) * (1 - beta) * f00 + alpha * (1 - beta) * f10 + (1 - alpha) * beta * f01 + alpha * beta * f11

    return interpolated_value

# Ejemplo de uso:
if __name__ == "__main__":
    # definir las coordenadas (x, y) en las que se desea interpolar
    x = 3.0
    y = 2.0

    # Define the coordinates of the four surrounding grid points
    x0, y0 = 2.0, 1.0
    x1, y1 = 4.0, 3.0

    # Definir las coordenadas de los cuatro puntos de la cuadrícula circundante
    f00, f01, f10, f11 = 5.0, 10.0, 15.0, 20.0

    # Realizar la interpolación bilineal
    interpolated_value = bilinear_interpolation(x, y, x0, y0, x1, y1, f00, f01, f10, f11)
    print(f"Interpolated value at ({x}, {y}): {interpolated_value}")
