# Cargar datos desde el archivo vorticidad.dat

using DelimitedFiles
using Plots

data = readdlm("vorticidad.dat")  # Asegúrate de que el formato sea adecuado

# Definir las dimensiones de la cuadrícula
nx = 20
ny = 18

# Definir las coordenadas de los puntos de interés
x1, y1 = 0.0, 0.4
x2, y2 = 0.0, -0.42

# Calcular las coordenadas normalizadas en la cuadrícula
i1 = Int(round((x1 + 1.5) / 3 * (nx - 1) + 1))  # +1 para índice basado en 1
j1 = Int(round((y1 + 1.56) / 3 * (ny - 1) + 1))
i2 = Int(round((x2 + 1.5) / 3 * (nx - 1) + 1))
j2 = Int(round((y2 + 1.56) / 3 * (ny - 1) + 1))

# Definir función para interpolación bilineal
function bilinear_interpolation(x, y, values)
    v1, v2, v3, v4 = values
    interp1 = (1 - x) * v1 + x * v2
    interp2 = (1 - x) * v3 + x * v4
    return (1 - y) * interp1 + y * interp2
end

# Realizar interpolación bilineal en los puntos de interés
vorticidad_punto1 = bilinear_interpolation(x1, y1, data[i1:i1+1, j1:j1+1])
vorticidad_punto2 = bilinear_interpolation(x2, y2, data[i2:i2+1, j2:j2+1])

# Imprimir resultados
println("Vorticidad en ($x1, $y1): $vorticidad_punto1")
println("Vorticidad en ($x2, $y2): $vorticidad_punto2")

# Calcular la vorticidad en el origen (0,0)
i_origen = Int(round((0.0 + 1.5) / 3 * (nx - 1) + 1))
j_origen = Int(round((0.0 + 1.56) / 3 * (ny - 1) + 1))
vorticidad_origen = data[i_origen, j_origen]

println("Vorticidad en el origen (0,0): $vorticidad_origen")


