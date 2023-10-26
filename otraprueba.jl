# Crear una matriz vacía (0x0)
matriz = Matrix{Int}(undef, 3, 3)

println(matriz)

# Definir algunas filas
fila1 = [1, 2, 3]
fila2 = [4, 5, 6]
fila3 = [7, 8, 9]

# Agregar fila1
matriz = vcat(matriz, fila1')

# Agregar fila2
matriz = vcat(matriz, fila2')

# Agregar fila3
matriz = vcat(matriz, fila3')

# Mostrar la matriz resultante
println(matriz)
