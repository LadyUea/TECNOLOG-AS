# Escritura de Archivo de Texto
with open("my_notes.txt", "w") as file:
    # Escribe al menos tres líneas de notas personales en el archivo
    file.write("Nota 1: Este es el primer apunte.\n")
    file.write("Nota 2: Aquí va el segundo apunte.\n")
    file.write("Nota 3: Tercer apunte para el archivo.\n")

# Lectura de Archivo de Texto
with open("my_notes.txt", "r") as file:
    # Lee el contenido del archivo línea por línea
    for line in file.readlines():
        # Muestra en la consola cada línea leída
        print(line.strip())

# Cierre de Archivos
# El archivo se cierra automáticamente al salir del bloque with