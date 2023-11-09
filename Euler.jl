using ForwardDiff
using Plots

# Define la función que representa la EDO
function f(t, y)
    return t-y
end

# Define el método de Taylor de orden n de forma recursiva
function taylor_method_recursive(f, y0, t0, h, x_end, x_vals=[], y_vals=[])
   
    if t0 > x_end
        return x_vals, y_vals
    else
        push!(x_vals, t0)
        push!(y_vals, y0)

        dydx = ForwardDiff.derivative(t -> f(t, y0), t0)

        y1 = y0 + h * dydx
        x1 = t0 + h

        return taylor_method_recursive(f, y1, x1, h, x_end, x_vals, y_vals)
    end
    
end

# Condiciones iniciales
t0 = 0.0
y0 = 0.5

# Tamaño del paso, orden del método y punto final del intervalo
h = 0.00001
x_end = 2.0

# Llamar al método de Taylor de forma recursiva
x_vals, y_vals = taylor_method_recursive(f, y0, t0, h, x_end)

# Imprimir la solución
for i in 1:length(x_vals)
    println("En t = $(x_vals[i]): y = $(y_vals[i])")
end

y(t) = -(exp.(t)./2) .+ t .^ 2 .+ 2 .* t .+ 1
a = y(x_vals)

plot(x_vals, y_vals)
plot!(x_vals,a)