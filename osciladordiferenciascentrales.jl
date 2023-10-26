using Plots
using LinearAlgebra

function al(xi, h, n)::Float64
    return (12*(ep-(xi+n*h)^2)*(h^2))-30
end;

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


function matrixBuilder()

    M=Matrix{Int}(undef,0,n-1)

    #caso especial i=2
    alp = al(xf[1], h, 2) 

    iccoef= Float64[16.0, alp, 16.0, -1.0]
    aux= zeros(Float64,(n-5))
    icc = vec(vcat(iccoef,aux))'
    M=vcat(M,icc)
    
    
    for i in 3:(n-3)
        local alp = al(xf[1], h, i) 
        gcoef = [-1, 16, alp, 16, 1]
        aux= vcat(zeros(Float64,(i-3)), gcoef)
        local icc = vec(vcat(aux, zeros(Float64,((n-1)-(i+2)))))'
        M=vcat(M,icc)
    end
    
    #caso especial i=n-2
    alp = al(xf[1], h, (n-2)) 
    fccoef=[-1, 16, alp, 16]
    icc = vec(vcat(zeros(Float64,(n-5)), fccoef))'
    M=vcat(M,icc)

    #rellena para hacer cuadrada
    for i in 1:2
        M=vcat(M,vec(zeros(Float64, n-1))')
    end

    println(M)
    return M
end

function rvecBuilder()

    vec=[]

    #caso especial i=2
    push!(vec,(uxf[1]))

    vec = vcat(vec,zeros(Float64,(n-5)))

    #caso especial i=n-2
    push!(vec,(uxf[2]))

    #rellena para hacerla solucion de matrix cuadrada
    vec = vcat(vec,[0.0,0.0])

    return vec
end 

println("Ingrese el primer  y el ultimo termino del intervalo, separados por una coma (x0, xn)")
user_xf = readline()
xf = split(user_xf, ',')
xf= parse.(Float64, xf)
println(xf)


println("Ingrese  (U(xo), U(xn)) separados por una coma ")
user_uxf = readline()
uxf = split(user_uxf, ',')
uxf= parse.(Float64, uxf)
println(uxf)

println("Ingrese la cantidad de puntos en dividir el intervalo (n)")
n = readline()
n = parse(Int64, n)

println("Ingrese el valor de epsilon")
ep = readline()
ep = parse(Float64, ep)

h = (xf[2]-xf[1])/n

A= matrixBuilder()
b = rvecBuilder()
println(b)

x0 = zeros(Float64, length(b))

tolerancia = 1e-6
max_iteraciones = 100000

solucion = gauss_seidel(A, b, x0, tolerancia, max_iteraciones)
println("Solución: ", solucion)