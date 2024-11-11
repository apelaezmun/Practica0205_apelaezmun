
def calcu_cuadrado(lista):
    """Función función que reciba una muestra de números en una lista y
    devuelva su media.
    Parámetros
    Nums: Lista de números
    Devuelve el cuadrado de los numeros de la lista.
    """
    return [x**2 for x in lista]
lista = [1, 7, 10, 17, 20]
print(calcu_cuadrado(lista))