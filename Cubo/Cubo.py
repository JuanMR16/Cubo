def calcular_volumen_cubo(lado1, lado2, lado3):
    # El volumen de un cubo es el producto de sus tres lados
    volumen = lado1 * lado2 * lado3
    return volumen

lado1 = float(input("Ingresa la longitud del Lado 1: "))
lado2 = float(input("Ingresa la longitud del Lado 2: "))
lado3 = float(input("Ingresa la longitud del Lado 3: "))

volumen = calcular_volumen_cubo(lado1, lado2, lado3)
print(f"El volumen del cubo es: {volumen}")