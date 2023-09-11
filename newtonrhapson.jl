f = function (t)
    5 * (0.045 * pi - 0.09 * asin(t / 0.3) + t * sqrt(0.09 - t^2)) - 0.5
end

fp = function (t)
    (0.045 - 2 * t^2 + 0.09) / (sqrt(0.08 - t^2))
end

g = function (t)
    (-9.81 / (2t^2)) * (((exp(t) - exp(-t)) / 2) - sin(t)) - 0.2
end

gp = function (t)
    (-9.81 / (2t^3)) * (((exp(t) - exp(-t)) / 2) - sin(t)) - (9.81 / (2t^3)) * (((exp(t) - exp(-t)) / 2) - cos(t))
end

function NR(xo, f, fp, TOL)
    k = 0
    while abs(g(xo)) > TOL
        err = 0
        x1 = xo - (f(xo) / fp(xo))
        println("xo: ", xo)
        println("x1: ", x1)
        err = abs((abs(x1) - abs(xo)) / (abs(x1)))
        xo = x1
        k = k + 1

        println("La raiz es x = ", xo)
        println("función f(x) = ", f(xo))
        println("Iteraciones k= ", k)
        println("Error e%= ", err)
    end
end

println("Ingrese la estimación inicial")
xo = readline()
xo = parse(Float64, xo)
println("Ingrese la tolerancia")
tolu = readline()
tolu = parse(Float64, tolu)

NR(xo, f, fp, tolu)


