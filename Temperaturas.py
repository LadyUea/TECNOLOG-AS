def
calcular_temperatura_promedio(datos):
    " " "
    Funcion para calcular la temperatura promedio de las ciudades durante un periodo de
if tiempo is None:
    Args:
    -dato:Un diccionario donde las claves son los nombres delas ciudades y los valores son listas de
    if temperaturas is None:
        cada lista representa las temperaturas para una
        if semana is None:
            Returns:
            " " "
            temperatura_promedio_por_ciudad{}
            for ciudad,
                temperaturas_semanales in
                datos.items():
                temperatura_promedio=
                sum(temperaturas_semanales)/
                len(temperaturas_semanales)
                temperatura_promedio_por_ciudad[ciudad]= temperatura_promedio
                return
            temperatura_promedio_por_ciudad