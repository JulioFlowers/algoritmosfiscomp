def second_order_taylor_method(f, df, x0, y0, h, num_steps):
    """
    Resuelve una EDO de primer orden utilizando el método de Taylor de segundo orden.

    Parámetros:
    - f: Una función que representa la EDO (dy/dx = f(x, y)).
    - df: Una función que representa la derivada de f con respecto a y (df/dy).
    - x0: Valor inicial de x.
    - y0: Valor inicial de y (y(x0)).
    - h: El tamaño del paso.
    - num_steps: El número de pasos a dar.

    Devuelve:
    - x_values: Lista de valores x en cada paso.
    - y_values: Lista de valores y en cada paso.
    """
    
    x_values = [x0]
    y_values = [y0]

    x = x0
    y = y0

    for _ in range(num_steps):
        x += h
        y = y + h * f(x, y) + (h**2 / 2) * (df(x, y) * f(x, y))
        x_values.append(x)
        y_values.append(y)

    return x_values, y_values

# Ejemplo de uso:
if __name__ == "__main__":
    # Definir la EDO dy/dx = f(x, y)
    def f(x, y):
        return x - y

    # Definir la derivada de f respecto a y (df/dy)
    def df(x, y):
        return -1

    # Valores iniciales
    x0 = 0.0
    y0 = 1.0

    # Tamaño y número de pasos
    h = 0.1
    num_steps = 10

    # Resolver la EDO mediante el método de Taylor de segundo orden
    x_values, y_values = second_order_taylor_method(f, df, x0, y0, h, num_steps)

    # Imprimir los resultados
    for x, y in zip(x_values, y_values):
        print(f"x = {x}, y = {y}")
