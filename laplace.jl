using OffsetArrays

function laplace_solver(n, m, tolerance)
    # Inicializar la matriz u con ceros
    u = OffsetArray(zeros(Float32, n, m), 1:n, 1:m)

    # Aplicar condiciones de contorno
    for i in 1:2
        u[i, 1] = 2 * log(i)
        u[i, 2] = log(i^2 + 1)
    end

    for j in 1:2
        u[1, j] = log(j^2 + 1)
        u[2, j] = log(j^2 + 4)
    end

    # Iteraciones de Jacobi
    max_iterations = 10000
    for k in 1:max_iterations
        u_old = copy(u)

        for i in 2:n-1
            for j in 2:m-1
                u[i, j] = 0.25 * (u_old[i+1, j] + u_old[i-1, j] + u_old[i, j+1] + u_old[i, j-1])
            end
        end

        # Calcular la norma infinita para verificar la convergencia
        residual = maximum(abs.(u - u_old))

        # Verificar convergencia
        if residual < tolerance
            println("Convergencia alcanzada en la iteración $k con una tolerancia de $residual.")
            break
        end
    end

    return u
end

# Parámetros
n = 3
m = 3
tolerance = 1e-4

# Resolver la ecuación de Laplace
solution = laplace_solver(n, m, tolerance)

# Mostrar la solución
println("Solución numérica:")
println(solution)
