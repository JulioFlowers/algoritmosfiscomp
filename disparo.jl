using Plots
n = 100
a = 1
b = 2
h = (b - a) / n
x = a:h:b
y = zeros(length(x))
yr = zeros(length(x))
dy = zeros(1, n)
y[1] = 1
y[n] = 2
dy[1] = 0
p(x) = -2 / x
q(x) = 2 / (x^2)
r(x) = sin(log(x)) / (x^2)
fr(x) = 1.1392070132x - 0.03920701320 / (x^2) - 3 / 10 * sin(log(x)) - 1 / 10 * cos(log(x))
u1 = zeros(1, n)
u2 = zeros(1, n)
v1 = zeros(1, n)
v2 = zeros(1, n)
u1[1] = 1
u2[1] = 0
v1[1] = 0
v2[1] = 1

for i in 1:n-1
    k11 = h * u2[i]
    k12 = h * (p(x[i]) * u2[i] + q(x[i]) * u1[i] + r(x[i]))
    k21 = h * (u2[i] + k12 / 2)
    k22 = h * (p(x[i] + h / 2) * (u2[i] + k12 / 2) + q(x[i] + h / 2) * (u1[i] + k11 / 2) + r(x[i] + h / 2))
    k31 = h * (u2[i] + k22 / 2)
    k32 = h * (p(x[i] + h / 2) * (u2[i] + k22 / 2) + q(x[i] + h / 2) * (u1[i] + k21 / 2) + r(x[i] + h / 2))
    k41 = h * (u2[i] + k32)
    k42 = h * (p(x[i + 1]) * (u2[i] + k32) + q(x[i + 1]) * (u1[i] + k31) + r(x[i + 1]))
    u1[i + 1] = u1[i] + (k11 + 2 * k21 + 2 * k31 + k41) / 6
    u2[i + 1] = u2[i] + (k12 + 2 * k22 + 2 * k32 + k42) / 6
    
    dk11 = h * v2[i]
    dk12 = h * (p(x[i]) * v2[i] + q(x[i]) * v1[i])
    dk21 = h * (v2[i] + dk12 / 2)
    dk22 = h * (p(x[i] + h / 2) * (v2[i] + dk12 / 2) + q(x[i] + h / 2) * (v1[i] + dk11 / 2))
    dk31 = h * (v2[i] + dk22 / 2)
    dk32 = h * (p(x[i] + h / 2) * (v2[i] + dk22 / 2) + q(x[i] + h / 2) * (v1[i] + dk21 / 2))
    dk41 = h * (v2[i] + dk32)
    dk42 = h * (p(x[i + 1]) * (v2[i] + dk32) + q(x[i + 1]) * (v1[i] + dk31))
    v1[i + 1] = v1[i] + (dk11 + 2 * dk21 + 2 * dk31 + dk41) / 6
    v2[i + 1] = v2[i] + (dk12 + 2 * dk22 + 2 * dk32 + dk42) / 6
end

for i in 1:n
    y[i] = u1[i] + (2 - u1[n]) / v1[n] * v1[i]
    yr[i] = fr(x[i])
end


plot(x, y, label="y(x)", linewidth=2)
plot!(x, yr, label="yr(x)", linestyle=:dash, linewidth=2)
xlabel!("x")
ylabel!("y")
title!("Comparación de y(x) y yr(x)")
