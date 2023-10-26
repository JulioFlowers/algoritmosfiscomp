using LinearAlgebra

function gauss_seidel(A, b, x0, tol, max_iter)
    n = length(b)
    x = copy(x0)  # Copiamos el vector inicial para no modificarlo
    
    for iter in 1:max_iter
        for i in 1:n
            # Calcular la suma de los términos de A*x, excluyendo A[i,i]
            sum1 = 0.0
            for j in 1:n
                if j != i
                    sum1 += A[i, j] * x[j]
                end
            end
            
            # Actualizar x[i] usando el método de Gauss-Seidel
            x[i] = (b[i] - sum1) / A[i, i]
        end
        
        # Comprobar la convergencia
        if norm(A * x - b) < tol
            println("Convergencia alcanzada después de $iter iteraciones.")
            return x
        end
    end
    
    println("El método de Gauss-Seidel no convergió en $max_iter iteraciones.")
    return x
end

# Ejemplo de uso
A = [10.0 -1.0 2.0; -1.0 11.0 -1.0; 2.0 -1.0 10.0]
b = [6.0; 25.0; -11.0]
x0 = zeros(length(b))
tolerancia = 1e-6
max_iteraciones = 100

solucion = gauss_seidel(A, b, x0, tolerancia, max_iteraciones)
println("Solución aproximada: ", solucion)
