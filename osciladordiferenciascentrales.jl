using Plots

function al(xi, h, n)::Float64
    return (12*(ep-(xi+n*h)^2)*(h^2))-30
end;

function gauss_seidel(A, b, x0, tol, max_iter)
    n = length(b)
    x = copy(x0)
    
    for k in 1:max_iter
        for i in 1:n
            sum1 = sum(A[i, j] * x[j] for j in 1:i - 1, init=zero(eltype(A)))
            sum2 = sum(A[i, j] * x[j] for j in i+1:n, init=zero(eltype(A)))
            x[i] = (b[i] - sum1 - sum2) / A[i, i]
        end
        
        # Comprobar convergencia
        if norm(A * x - b) < tol
            return x
        end
    end
    
    error("El método de Gauss-Seidel no convergió en $max_iter iteraciones.")
end

function matrixBuilder()

    matrix=[]

    #caso especial i=2
    alp = al(xf[1], h, 2) 
    iccoef= Float64[16.0, alp, 16.0, -1.0]
    icc = vcat(iccoef, zeros(Float64,(n-5)))
    push!(matrix, icc)
    
    
    for i in 3:(n-3)
        local alp = al(xf[1], h, i) 
        gcoef = [-1, 16, alp, 16, 1]
        aux= vcat(zeros(Float64,(i-3)), gcoef)
        local icc = vcat(aux, zeros(Float64,((n-1)-(i+2))))
        push!(matrix, icc)
    end
    
    #caso especial i=n-2
    alp = al(xf[1], h, (n-2)) 
    fccoef=[-1, 16, alp, 16]
    icc = vcat(zeros(Float64,(n-5)), fccoef)
    push!(matrix, icc)

    return hcat(matrix...)
end

function rvecBuilder()

    vec=[]

    #caso especial i=2
    push!(vec,(uxf[1]))

    vec = vcat(vec,zeros(Float64,(n-5)))

    #caso especial i=n-2
    push!(vec,(uxf[2]))

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
A
b = rvecBuilder()
x0 = zeros(Float64, length(b))

tolerancia = 1e-6
max_iteraciones = 100000

solucion = gauss_seidel(A, b, x0, tolerancia, max_iteraciones)
println("Solución: ", solucion)