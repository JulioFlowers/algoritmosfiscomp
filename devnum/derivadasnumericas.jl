#Perez Flores Julio Alfonso
#Taller Dirivacion numerica

#para graficar
using Plots

#funcion a derivar
fu = function (t)
    return exp(cos(t))
end

#derivada  2do orden centrada
g2c = function (f,h,t)
    return (f(t+h)-f(t-h))/(2*h)
end
#derivada  2do orden regresiva
g2r = function (f, h, t)
    return  (3*f(t) - 4*f(t-h)+f(t-2*h))/(2*h)
end
#derivada  2do orden progresiva
g2p = function (f, h, t)
   return return  return  (-3*f(t) + 4*f(t+h) - f(t+2*h))/(2*h)
end

#le pedimos el inicio del intervalo
println("Ingrese primer termino del intervalo,  a: ")
a = readline()
a = parse(Float64, a)

#le pedimos el fin del intervalo
println("Ingrese ultimo termino del intervalo, b: ")
b = readline()
b = parse(Float64, b)

#calcularemos h a partir de cuantos pasos quiere dar el usuario
println("En cuantos pasos quiere dividir el intervalo: ")
div = readline()
div = parse(Float64, div)

#delta h
ih= (b-a)/div

#=Definimos un intervalodo de numeros de a y cuyo paso 
va aumentando h, hasta llegar a b =#
interval = range(a,b, step = ih)

#=
Definimos tres arrays, para la imagen de F
para las derivadas centradas 
para las derivadas progresivas
para las derivadas regresivas
=#
imf = Any[]
dc = Any[]
dr  = Any[]
dp  = Any[]

#=Para cada punto del intervalo calculamos 
las derivas y lo guardamos en los arrays=#
for x in interval
    push!(imf, fu(x))
    push!(dc,g2c(fu,ih,x))
    push!(dr,g2r(fu,ih,x))
    push!(dp,g2p(fu,ih,x))
end

println("Derivadas centradas: ", dc)
println(dc)
println("")
println("Derivadas regresivas: ")
println(dr)
println("")
println("Derivadas progresivas", dc)
println(dc)
println("")

plot(interval, [imf dc dr dp], label=["f(x)" "d cent." "d. reg." "d.prog"])