import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def laplace_solver(n, m, tolerance):
    # Inicializar la matriz u con ceros
    u = np.zeros((n + 1, m + 1), dtype=float)

    # Aplicar condiciones de contorno
    for i in range(1, 3):
        u[i, 0] = 2 * np.log(i)
        u[i, 1] = np.log(i**2 + 1)

    for j in range(2):
        u[1, j] = np.log(j**2 + 1)
        u[2, j] = np.log(j**2 + 4)

    # Iteraciones de Jacobi
    max_iterations = 10000
    for k in range(max_iterations):
        u_old = np.copy(u)

        for i in range(1, n):
            for j in range(1, m):
                u[i, j] = 0.25 * (u_old[i+1, j] + u_old[i-1, j] + u_old[i, j+1] + u_old[i, j-1])

        # Calcular la norma infinita para verificar la convergencia
        residual = np.max(np.abs(u - u_old))

        # Verificar convergencia
        if residual < tolerance:
            print(f"Convergencia alcanzada en la iteración {k + 1} con una tolerancia de {residual}.")
            break

    return u

# Parámetros
n = 3
m = 3
tolerance = 1e-4

# Resolver la ecuación de Laplace
solution = laplace_solver(n, m, tolerance)

# Mostrar la solución
print("Solución numérica:")
print(solution)

x = np.linspace(1, 2, n + 1)
y = np.linspace(0, 1, m + 1)

# Crear mallas 2D para x e y
X, Y = np.meshgrid(x, y)

# Graficar la superficie
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, solution, cmap='viridis')

# Configurar etiquetas y título
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('u(x, y)')
ax.set_title('Solución de la Ecuación de Laplace')

# Mostrar el gráfico
plt.show()