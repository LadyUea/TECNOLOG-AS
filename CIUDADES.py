import random

# Definir nombres de ciudades, días de la semana y semanas
ciudades = ['Ciudad A', 'Ciudad B', 'Ciudad C']
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = ['Semana 1', 'Semana 2', 'Semana 3']

# Crear matriz 3D de temperaturas aleatorias
temperaturas = [[[random.randint(10, 30) for _ in range(len(dias_semana))] for _ in range(len(ciudades))] for _ in range(len(semanas))]

# Calcular y mostrar el promedio de temperaturas para cada ciudad y semana
for i, ciudad in enumerate(ciudades):
    print(f"\nPromedio de temperaturas para {ciudad}:")
    for j, semana in enumerate(semanas):
        promedio_semana = sum(temperaturas[j][i]) / len(temperaturas[j][i])
        print(f"{semana}: {promedio_semana:.2f} gradosCelsius")