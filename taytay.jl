using Plots

function taylor_series_2nd_order(f, f_prime, y0, h, x_range)
    n = length(x_range)
    y = zeros(n)
    y[1] = y0
    
    for i in 2:n
        x = x_range[i]
        y[i] = y[i-1] + h*f(x, y[i-1]) + 0.5*h^2*(f(x, y[i-1])*f_prime(x, y[i-1]) + f_prime(x, y[i-1])*f(x, y[i-1]))
    end
    
    return y
end

function taylor_series_4th_order(f, f_prime, y0, h, x_range)
    n = length(x_range)
    y = zeros(n)
    y[1] = y0
    
    for i in 2:n
        x = x_range[i]
        k1 = h*f(x, y[i-1])
        k2 = h*f(x + 0.5*h, y[i-1] + 0.5*k1)
        k3 = h*f(x + 0.5*h, y[i-1] + 0.5*k2)
        k4 = h*f(x + h, y[i-1] + k3)
        
        y[i] = y[i-1] + (k1 + 2*k2 + 2*k3 + k4)/6
    end
    
    return y
end

# Definir la ecuación diferencial y su derivada
f(x, y) = (x - 3*x^2*y) / x^3
f_prime(x, y) = (6*x*y - 1) / x^4

# Definir la solución exacta
exact_solution(x) = (0.5/ x^3) + (1.0 / (2*x))

# Parámetros
y0 = 1.0
h = 0.1
x_range = 1:0.1:3

# Calcular soluciones con los métodos de Taylor de segundo y cuarto orden
y_taylor_2nd = taylor_series_2nd_order(f, f_prime, y0, h, x_range)
y_taylor_4th = taylor_series_4th_order(f, f_prime, y0, h, x_range)
y_exact = exact_solution.(x_range)

# Graficar las soluciones
plot(x_range, y_taylor_2nd, label="Taylor 2nd Order", xlabel="x", ylabel="y", title="Solución de Ecuación Diferencial", lw=2)
plot!(x_range, y_taylor_4th, label="Taylor 4th Order", lw=2)
plot!(x_range, y_exact, label="Solución Exacta", lw=2, linestyle=:dash)
