#Escribir una función que reciba un número entero positivo y devuelva su
#factorial. Realiza el ejercicio mediante bucles interactivos y mediante una
#función recursiva.
def factorial(n):
    """función que reciba un número entero positivo y devuelva su
    factorial.
    n: Es un entero positivo.
    Devuelve el factorial de n.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(8))