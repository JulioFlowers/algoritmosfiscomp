using Plots

# Definir la función de la EDO
function f(x, y)
    return -0.6*pi*0.1^2*sqrt(2*32.1)*(sqrt(x)/(8^2-x^2)*pi)
end

# Método de Runge-Kutta de orden 4
function runge_kutta_4(f, x0, y0, h, x_end)
    x_values = [x0]
    y_values = [y0]
    x = x0
    y = y0
    while x < x_end
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        y = y + (k1 + 2k2 + 2k3 + k4) / 6
        x += h
        push!(x_values, x)
        push!(y_values, y)
    end
    return x_values, y_values
end

# Parámetros iniciales
x0 = 0.0
y0 = 512*pi/3
h = 60
x_end = 100

# Resolver la EDO
x_values, y_values = runge_kutta_4(f, x0, y0, h, x_end)



# Graficar los resultados
plot(x_values, y_values, label="Solución numérica", xlabel="x", ylabel="y", legend=:topright)
