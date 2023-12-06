using Plots

# Definir la función de la EDO
function f(x, y, a)
    return a * (sqrt(x) / (64 - x^2) * π)
end

# Método de Runge-Kutta de orden 4
function runge_kutta_4(f, x0, y0, a, h, x_end)
    x_values = [x0]
    y_values = [y0]
    x = x0
    y = y0
    while x < x_end
        k1 = h * f(x, y, a)
        k2 = h * f(x + h/2, y + k1/2, a)
        k3 = h * f(x + h/2, y + k2/2, a)
        k4 = h * f(x + h, y + k3, a)
        y = y + (k1 + 2k2 + 2k3 + k4) / 6
        x += h
        push!(x_values, x)
        push!(y_values, y)
    end
    return x_values, y_values
end

# Parámetros iniciales
x0 = 0
y0 = (pi/3)*512
a = -0.6*pi*0.01*sqrt(2*32.1) # Puedes ajustar este valor según tus necesidades
print(a)
h = 60
x_end = 100.0  # Puedes ajustar este valor según tus necesidades

# Resolver la EDO
x_values, y_values = runge_kutta_4(f, x0, y0, a, h, x_end)

# Graficar los resultados
plot(x_values, y_values, label="Solución numérica", xlabel="x", ylabel="y", legend=:topright)
