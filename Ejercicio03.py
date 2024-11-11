# función que calcule el área de un círculo y otra que calcule el volumen de
#un cilindro usando la primera función.
def area_circulo(radio):
    """función que calcule el área de un círculo
    Parámetros
    radio: Es el radio del círculo.
    Devuelve el área del círculo 
    """
    pi = 3.1416
    return pi * radio **2
print(area_circulo(2))
def volumen_cilindro(radio, altura):
    """función que calcule volumen de un cilindro usando la primera función.
    Parámetros
    radio: Es el radio de la base del cilindro.
    altura: Es la altura del cilindro.
    Devuelve el volumen del clindro
    """
    return area_circulo(radio)*altura
print(volumen_cilindro(2,8))