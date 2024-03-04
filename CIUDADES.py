# Solicitar al usuario el número de ciudades, días de la semana y semanas
num_ciudades = int(input("Ingrese el número de ciudades: "))
num_dias = int(input("Ingrese el número de días de la semana: "))
num_semanas = int(input("Ingrese el número de semanas: "))

# Definir nombres de ciudades, días de la semana y semanas
ciudades = [input(f"Ingrese el nombre de la ciudad {i+1}: ") for i in range(num_ciudades)]
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = [input(f"Ingrese el nombre de la semana {i+1}: ") for i in range(num_semanas)]

# Crear matriz 3D de temperaturas aleatorias
temperaturas = np.random.randint(10, 30, size=(num_ciudades, num_dias, num_semanas))

# Calcular promedio de temperaturas para cada ciudad y semana
for i, ciudad in enumerate(ciudades):
    print(f"\nPromedio de temperaturas para {ciudad}:")
    for j, semana in enumerate(semanas):
        promedio_semana = np.mean(temperaturas[i, :, j])
        print(f"{semana}: {promedio_semana:.2f} grados_Celsius")