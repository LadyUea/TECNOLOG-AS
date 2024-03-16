def calcular_descuento(valor_total, porcentaje_descuento=10):
    descuento = valor_total * (porcentaje_descuento / 100)
    return descuento

valor_compra_1 = 200
valor_compra_2 = 350
porcentaje_descuento = 15

descuento_1 = calcular_descuento(valor_compra_1)
descuento_2 = calcular_descuento(valor_compra_2, porcentaje_descuento)

# Cálculo del valor final a pagar
valor_final_1 = valor_compra_1 - descuento_1
valor_final_2 = valor_compra_2 - descuento_2

# Salida de resultados
print("Valor de la compra 1: $", valor_compra_1)
print("Descuento aplicado en la compra 1: $", descuento_1)
print("Valor final a pagar en la compra 1: $", valor_final_1)

print("Valor de la compra 2: $", valor_compra_2)
print("Descuento aplicado en la compra 2: $", descuento_2)
print("Valor final a pagar en la compra 2: $",valor_final_2)