import numpy as np
from scipy.interpolate import CubicSpline

# Definir puntos de datos conocidos
x_data = np.array([0, 1, 2, 3, 4], dtype=float)
y_data = np.array([0, 1, 8, 27, 64], dtype=float)

# Crear un interpolador de splines cúbicos
cubic_interp = CubicSpline(x_data, y_data)

# Defina el punto en el que desea realizar la interpolación cúbica
x_interp = 2.5

# Realiza la interpolación cúbica en x_interp
y_interp = cubic_interp(x_interp)

# Print el valor interpolado
print(f"Interpolated value at {x_interp}: {y_interp}")
