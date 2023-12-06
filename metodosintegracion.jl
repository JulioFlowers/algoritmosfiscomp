using Plots

# Función a integrar
f(x) = exp(x) - 3x

# Límites de integración
a = 0.5
b = 1.6

# Número de divisiones para los métodos del trapecio y de Simpson
n_divisions = 100

# Paso de integración
h = (b - a) / n_divisions

# Método del Trapecio
function trapezoidal_rule(f, a, b, n)
    h = (b - a) / n
    result = (f(a) + f(b)) / 2.0
    for i in 1:n-1
        result += f(a + i * h)
    end
    result *= h
    return result
end

# Método de Simpson
function simpsons_rule(f, a, b, n)
    h = (b - a) / n
    result = f(a) + f(b)
    for i in 1:n-1
        result += 4 * f(a + i * h) + 2 * f(a + (i + 1) * h)
    end
    result *= h / 3
    return result
end

# Método de Cuadratura Gaussiana (2 puntos, para funciones cuadráticas exactas)
function gaussian_quadrature(f, a, b)
    x = [-1 / sqrt(3), 1 / sqrt(3)]
    w = [1.0, 1.0]
    result = sum(w[i] * f((b - a) / 2 * x[i] + (b + a) / 2) for i in 1:2)
    result *= (b - a) / 2
    return result
end

# Calcular las integrales con los tres métodos
trapezoidal_result = trapezoidal_rule(f, a, b, n_divisions)
simpsons_result = simpsons_rule(f, a, b, n_divisions)
gaussian_result = gaussian_quadrature(f, a, b)

# Mostrar resultados
println("Resultado con Trapecio: ", trapezoidal_result)
println("Resultado con Simpson: ", simpsons_result)
println("Resultado con Cuadratura Gaussiana: ", gaussian_result)

