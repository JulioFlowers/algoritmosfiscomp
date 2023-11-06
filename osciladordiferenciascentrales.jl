using Plots
using LinearAlgebra

function al(yi, h, n)::Float64
    return (12*(ep-(yi+n*h)^2)*(h^2))-30
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
    return 
end


function matrixBuilder()

    M=Matrix{Int}(undef,0,n-3)
    

    #caso especial i=2
    alp = al(y1, h, 2) 

    iccoef= Float64[alp, 16.0, -1.0]
    aux= zeros(Float64,(n-6))
    icc = vec(vcat(iccoef,aux))'
    M=vcat(M,icc)

    #caso especial i=3
    alp = al(y1, h, 3) 

    iccoef= Float64[16.0, alp, 16.0, -1.0]
    aux= zeros(Float64,(n-7))
    icc = vec(vcat(iccoef,aux))'
    M=vcat(M,icc)

    
    if (n-3 != 4)
    
        for i in 4:(n-4)
            local alp = al(y1, h, i) 
            gcoef = [-1.0, 16.0, alp, 16.0, -1.0]
            aux= vcat(zeros(Float64,(i-4)), gcoef)
            local icc = vec(vcat(aux, zeros(Float64,((n-3)-(i+1)))))'
            println(icc)
            M=vcat(M,icc)
        end

    end

    #caso especial i=n-3
    alp = al(y1, h, (n-3)) 
    fccoef=[-1.0, 16.0, alp, 16.0]
    icc = vec(vcat(zeros(Float64,(n-7)), fccoef))'
    M=vcat(M,icc)
    
    #caso especial i=n-2
    alp = al(y1, h, (n-2)) 
    fccoef=[-1, 16, alp]
    icc = vec(vcat(zeros(Float64,(n-6)), fccoef))'
    M=vcat(M,icc)

    return M
end

function rvecBuilder()

    vec=[]

    #caso especial i=2
    push!(vec,(uyf[1]-16*uyf[2]))

    #caso especial i=3
    push!(vec,uyf[2])

    vec = vcat(vec,zeros(Float64,(n-7)))

    #caso especial i=3
    push!(vec,uyf[3])

    #caso especial i=n-2
    push!(vec,(uyf[4]-16*uyf[3]))

    return vec
end 

println("Ingrese el primer  y el ultimo termino del intervalo, separados por una coma (x_{0}, x_{n})")
user_yf = readline()
yf = split(user_yf, ',')
yf= parse.(Float64, yf)
println(yf)

println("Ingrese (U_{o}, U_{1}, U_{n-1}, U_{n-2}) separados por una coma ")
user_uyf = readline()
uyf = split(user_uyf, ',')
uyf= parse.(Float64, uyf)
println(uyf)

println("Ingrese la cantidad de puntos en dividir el intervalo (n)")
n = readline()
n = parse(Int64, n)

println("Ingrese el valor de epsilon")
ep = readline()
ep = parse(Float64, ep)

h = (yf[2]-yf[1])/n 

y1= yf[1]+h

A= matrixBuilder()

b = rvecBuilder()
println(b)

x0 = zeros(Float64, length(b))

tolerancia = 1e-6
max_iteraciones = 1000000

solucion = gauss_seidel(A, b, x0, tolerancia, max_iteraciones)
println("Solución: ", solucion)

xs= range(yf[1], yf[2], step=h)
println(length(xs))

system = vcat(uyf[1:2],solucion,uyf[3:4])
println(system)
println(length(system))
plot(xs, system)