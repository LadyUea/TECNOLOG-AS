def calcular_promedio(lista):
    if len(lista) == 0:
        return None
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio
    temperaturas = [20,22,25,19,30],
    promedio_temperaturas = (
        calcular_promedio(temperaturas))
    if promedio_temperaturas is not None:
        print("El promedio de las temperaturas es:", promedio_temperaturas)
    else:
    print("La lista de temperaturas esta vacía.")





