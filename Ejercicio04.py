#Escribir una función que reciba una muestra de números en una lista y
#devuelva su media.
def calcu_media(lista_numeros):
    """Función función que reciba una muestra de números en una lista y
    devuelva su media
    Parámetros
    Nums: Es una lista de números
    Devuelve la media.
    """
    if len(lista_numeros) != 0:
        suma = sum(lista_numeros)
        media = suma / len(lista_numeros)
        return media
    else:
        return 0
lista = [0, 1, 5, 9, 20, 32]
print(calcu_media(lista))