k = int(input("Введіть к-сть кошиків винограду1: "))
m = float(input("Введіть масу внограду1 в кг: "))
a = int(input("Введіть к-сть кошиків винограду2: "))
b = float(input("Введіть масу внограду2 в кг: "))
weight1 = k * m
weight2 = a * b
total_weight = weight1 + weight2
total_weight_kg = int(total_weight)
total_weight_g = round((total_weight - total_weight_kg) * 1000)
print("Дівчинка зібрала", total_weight_kg, "кг", total_weight_g, "г")
