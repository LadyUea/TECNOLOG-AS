# Diccionario

informacion_personal = {
    'nombre':'Annie',
    'edad':25,
    'ciudad':'Durán',
    'provincia':'Guayas',
    'profesión':'Estudiante',
}
print('----------------------')
print('Diccionario Original')
print('----------------------')
for clave, valor in informacion_personal.items():
    print(f'{clave} : {valor}')

# Clave "ciudad" y modifícalo con una ciudad diferente.
informacion_personal['ciudad'] = 'Ventanas'
informacion_personal['provincia'] = 'Los Ríos'

# Nueva clave-valor al diccionario "profesion"
informacion_personal['profesión'] = 'Estudiante'

# Verifica si la clave "telefono" existe
if 'teléfono' not in informacion_personal:
    informacion_personal['teléfono'] = '0990434544'

# Elimina la clave "edad" del diccionario
# del información_personal['edad']
informacion_personal.pop('edad')

print('----------------------')
print('Diccionario Modificado')
print('----------------------')
for clave, valor in informacion_personal.items():
    print(f'{clave} : {valor}')