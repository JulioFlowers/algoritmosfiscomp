function f(t)
    return (t^4)-(16*t^3)-(500*t^2)+8000*t-32000
end

function q(xo,x1,x2)  
    return (x2-x1)/(x1-xo)
end

function a(f,q,x2,x1,xo)
    return q*f(x2)-q*(1+q)f(x1)+(q^2)*f(xo)
end

function b(f,q,x2,x1,xo)
    return (2*q+1)f(x2)-((1+q)^2)*f(x1)+(q^2)*f(xo)
end

function c(f,q,x2)
    return (1+q)*f(x2)
end

function MM(f,x2,x1,xo, TOL)
    k=1
    while abs(f(x2)) > TOL
        err = 0
        
        Q = q(xo,x1,x2)
        A= a(f,Q,x2,x1,xo) 
        B= b(f,Q,x2,x1,xo) 
        C= c(f,Q,x2) 
    
        x3= x2-((x2-x1)*(2*C/max((B+sqrt((B^2)-(4*A*C))),(B-sqrt((B^2)-(4*A*C))))))
        err = abs((abs(x3) - abs(x2)) / (abs(x3)))
        xo=x1
        x1=x2
        x2=x3
        println("La raiz es x = ", x2)
        println("función f(x) = ", f(x2))
        println("Iteraciones k= ", k)
        println("Error e%= ", err)
        k = k + 1
    end
end

println("Ingrese la primera estimación (x0)")
xo = readline()
xo = parse(Float64, xo)

println("Ingrese la segunda estimación (x1)")
x1 = readline()
x1 = parse(Float64, x1)

println("Ingrese la tercera estimación (x2)")
x2 = readline()
x2 = parse(Float64, x2)

println("Ingrese la tolerancia")
tolu = readline()
tolu = parse(Float64, tolu)

MM(f,x2,x1,xo,tolu)