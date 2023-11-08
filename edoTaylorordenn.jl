using Plots

#libreria para cualcular derivadas
using ForwardDiff

#recordemos w_i=y(x_i)
f(t,y) = t^2 + 2t + 1

function W(n,ti, wi, h, f)
    sum=0

    for i in 1:n
        
        if (i == 1)
            sum = f(ti,wi)
        end

        sum = ((h^(i-1))/(factorial(i)))*ForwardDiff.derivative(f(t, wi), ti, n-1)
    end

    return wi + h*sum
end

println("Ingrese el primer  y el ultimo termino del intervalo, separados por una coma (a,b)")
user_in = readline()
inv = split(user_in, ',')
inv= parse.(Float64, inv)
println(inv)

println("Ingrese el numero de puntos del intervalo")
n = readline()
n = parse(Int64, n)

h = (inv[end]-inv[1])/n

println("Ingrese y(a)")
w0 = readline()
w0 = parse(Float64, w0)

xs = inv[1]:h:inv[end]

function yHandler(j,n,ti,wo,h, f)

    if (j==1) 
        return W(n,ti,wo, h, f)

    else
        return yHandler((j-1),n,ti,wo,h, f)
    end
end

ys=[]

for (j, xi) in enumerate(xs)
    push!(ys, yHandler(j,n,xi,w0,h,f))
end

println(ys)