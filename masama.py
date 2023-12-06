import numpy as np

# Funciones dadas
def Q(t):
    return 9 + 4 * np.cos(2 * 0.4 * t)

def c(t):
    return 5 * np.exp(-0.5 * t) + 2 * np.exp(0.15 * t)

def simpson_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    integral = h / 3 * (y[0] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-2:2]) + y[-1])
    return integral

# Intervalo de tiempo
t1 = 2  # min
t2 = 8  # max

# Tolerancia del 0.1%
tolerance = 0.001

# Inicializar el número de subdivisiones
n = 2

# Inicializar la masa calculada
M_calculated = 0

# Calcular la masa con la regla de Simpson hasta que la tolerancia sea alcanzada
while True:
    M_prev = M_calculated
    M_calculated = simpson_rule(lambda t: Q(t) * c(t), t1, t2, n)
    n *= 2
    if abs((M_calculated - M_prev) / M_calculated) < tolerance:
        break

# Imprimir el resultado
print(f"La masa transportada entre t1={t1} max y t2={t2} min es aproximadamente {M_calculated:.4f} mg. con n= {n}")
