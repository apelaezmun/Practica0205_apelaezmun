#Escribir una función a la que se le pase una cadena <nombre> y muestre por
#pantalla el saludo ¡hola <nombre>!.
def saludar(nombre):
    """función a la que se le pase una cadena <nombre> y muestre por
    pantalla el saludo ¡hola <nombre>!.
    Parámetros
    nombre: Nombre de la persona
    Devuelve saludo ¡Hola (nombre)!.
    """
    print('¡Hola ' + nombre + '!')
    return
saludar('Anthony')