using Plots
using CSV
using DataFrames

# Ruta al archivo CSV
ruta_archivo = "datosinterlagrange.csv"

# Cargar el archivo CSV en un DataFrame
df = CSV.File(ruta_archivo) |> DataFrame

# Extraer la primera columna como un array de números flotantes
x_values = df.TEMP
yh2_values = df.H2
yco2_values = df.CO2
yo2_values = df.O2
yn2_values = df.N2

function lagrange_interpolation(x_values, y_values, x)
    n = length(x_values)
    result = 0.0

    for i in 1:n
        term = y_values[i]
        for j in 1:n
            if i != j
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
            end
        end
        result += term
    end

    return result
end

# Función para evaluar en una serie de puntos
function evaluate_interpolation(x_values, y_values, x_points)
    results = [lagrange_interpolation(x_values, y_values, x) for x in x_points]
    return results
end


# Puntos para evaluar la interpolación
x_points_to_evaluate = minimum(x_values):0.1:maximum(x_values)

# Evaluar la interpolación en los puntos dados
h2 = evaluate_interpolation(x_values, yh2_values, x_points_to_evaluate)
co2 = evaluate_interpolation(x_values, yco2_values, x_points_to_evaluate)
o2 = evaluate_interpolation(x_values, yo2_values, x_points_to_evaluate)
n2 = evaluate_interpolation(x_values, yn2_values, x_points_to_evaluate)

# Graficar los puntos de datos y la interpolación
#plot!(x_points_to_evaluate, resultsh2, label = "Interpolación de Lagrange H2", xlabel = "x [K]", ylabel = "y [kJ/kgK]", legend = :outerright)


plot(x_values, yh2_values, seriestype=:scatter, label="Datos H2",
    title="Calores especificos con interpolación de Lagrange H2",
    titlefont=font(14, "Computer Modern"),
    legendfont=font(8, "Computer Modern"),
    xtickfont=font(7, "Computer Modern"),
    ytickfont=font(7, "Computer Modern"),
    guidefont=font(10, "Computer Modern"),
    xlabel="Temperatura [K]",
    ylabel="cp [kJ/kgK]",
    legend=:bottomright)
plot!(x_points_to_evaluate, h2, label="Interpolación de Lagrange", xlabel="x", ylabel="y")
savefig("h2.png")

plot(x_values, yco2_values, seriestype=:scatter, label="Datos CO2",
    title="Calores especificos con interpolación de Lagrange CO2",
    titlefont=font(14, "Computer Modern"),
    legendfont=font(8, "Computer Modern"),
    xtickfont=font(7, "Computer Modern"),
    ytickfont=font(7, "Computer Modern"),
    guidefont=font(10, "Computer Modern"),
    xlabel="Temperatura [K]",
    ylabel="cp [kJ/kgK]",
    legend=:bottomright)
plot!(x_points_to_evaluate, co2, label="Interpolación de Lagrange", xlabel="x", ylabel="y")
savefig("co2.png")

plot(x_values, yo2_values, seriestype=:scatter, label="Datos O2",
    title="Calores especificos con interpolación de Lagrange O2",
    titlefont=font(14, "Computer Modern"),
    legendfont=font(8, "Computer Modern"),
    xtickfont=font(7, "Computer Modern"),
    ytickfont=font(7, "Computer Modern"),
    guidefont=font(10, "Computer Modern"),
    xlabel="Temperatura [K]",
    ylabel="cp [kJ/kgK]",
    legend=:bottomright)
plot!(x_points_to_evaluate, o2, label="Interpolación de Lagrange", xlabel="x", ylabel="y")
savefig("o2.png")

plot(x_values, yn2_values, seriestype=:scatter, label="Datos N2",
    title="Calores especificos con interpolación de Lagrange N2",
    titlefont=font(14, "Computer Modern"),
    legendfont=font(8, "Computer Modern"),
    xtickfont=font(7, "Computer Modern"),
    ytickfont=font(7, "Computer Modern"),
    guidefont=font(10, "Computer Modern"),
    xlabel="Temperatura [K]",
    ylabel="cp [kJ/kgK]",
    legend=:bottomright)
plot!(x_points_to_evaluate, n2, label="Interpolación de Lagrange", xlabel="x", ylabel="y")
savefig("n2.png")