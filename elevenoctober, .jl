using LaTeXStrings
using Plots

#=esta funcion calcula los predictores y el siguiente paso par las
ecuaciones del sistema =#
function heun_method(f, u0, v0, y0, x0,k, h, N)
    u = zeros(N+1)
    v = zeros(N+1)
    y = zeros(N+1)
    x = zeros(N+1)

    u[1] = u0
    v[1] = v0
    y[1] = y0
    x[1] = x0

    for n in 1:N
        tn = (n-1) * h
        un_pred = u[n] + h * f(tn, u[n], v[n], y[n], x[n], k, h)[1]
        vn_pred = v[n] + h * f(tn, u[n], v[n], y[n], x[n], k, h)[2]
        yn_pred = y[n] + h * f(tn, u[n], v[n], y[n], x[n], k, h)[3]
        xn_pred = x[n] + h * f(tn, u[n], v[n], y[n], x[n], k, h)[4]

        un = u[n] + (h/2) * (f(tn, u[n], v[n], y[n], x[n], k, h)[1] + f(tn + h, un_pred, vn_pred, yn_pred, xn_pred, k, h)[1])
        vn = v[n] + (h/2) * (f(tn, u[n], v[n], y[n], x[n], k, h)[2] + f(tn + h, un_pred, vn_pred, yn_pred, xn_pred, k, h)[2])
        yn = y[n] + (h/2) * (f(tn, u[n], v[n], y[n], x[n], k, h)[3] + f(tn + h, un_pred, vn_pred, yn_pred, xn_pred, k, h)[3])
        xn = x[n] + (h/2) * (f(tn, u[n], v[n], y[n], x[n], k, h)[4] + f(tn + h, un_pred, vn_pred, yn_pred, xn_pred, k, h)[4])

        u[n+1] = un
        v[n+1] = vn
        y[n+1] = yn
        x[n+1] = xn
    end

    return u, v, y, x
end

#sistema de edos
function f(t, u, v, y, x, k, h)
    dx = h * u
    dv = h * ((-2u .* v .- sin.(y)) ./ (x .+ 1))
    dy = h * v
    du = h * ((1 .+ x) .* v.^2 .+ cos.(y) .- k .* x)

    return du, dv, dy, dx
end


# Parámetros iniciales
u0 = 0.0
v0 = 0.0
y0 = 0.1
x0 = 0.3
k=2.0

# Tamaño del paso y número de pasos
h = 0.1
N = 10

# Llamada al método de Heun
u, v, y, x = heun_method(f, u0, v0, y0, x0,k, h, N)

# Visualización de los resultados

plot(x, label=L"x(t)", title = "Sistmea K = $(k)", legend=:outerbottom)
savefig("xvst$(Int(k*10)).png" )
plot(y, label=L"\theta(t)", title = "Sistmea K = $(k)", legend=:outerbottom)
savefig("thetavst$(Int(k*10)).png" )

p2= plot(y,x, title = "Sistmea K = $(k)", label=L"$x(t)\ vs\ \ \theta(t)$", legend=:outerbottom)
savefig("xvstheta$(Int(k*10)).png" )

k = 2.5 

u, v, y, x = heun_method(f, u0, v0, y0, x0,k, h, N)

# Visualización de los resultados

plot(x, label=L"x(t)", title = "Sistmea K = $(k)", legend=:outerbottom)
savefig("xvst$(Int(k*10)).png" )
plot(y, label=L"\theta(t)", title = "Sistmea K = $(k)", legend=:outerbottom)
savefig("thetavst$(Int(k*10)).png" )

plot(y,x, title = "Sistmea K = $(k)", label=L"$x(t)\ vs\ \ \theta(t)$", legend=:outerbottom)
savefig("xvstheta$(Int(k*10)).png" )


k = 3    

u, v, y, x = heun_method(f, u0, v0, y0, x0,k, h, N)

# Visualización de los resultados

plot(x, label=L"x(t)", title = "Sistmea K = $(k)", legend=:outerbottom)
savefig("xvst$(Int(k*10)).png" )
plot(y, label=L"\theta(t)", title = "Sistmea K = $(k)", legend=:outerbottom)
savefig("thetavst$(Int(k*10)).png" )

plot(y,x, title = "Sistmea K = $(k)", label=L"$x(t)\ vs\ \ \theta(t)$", legend=:outerbottom)
savefig("xvstheta$(Int(k*10)).png" )