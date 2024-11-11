#Escribir una función que reciba un número entero positivo y devuelva su
#factorial. Realiza el ejercicio mediante bucles interactivos y mediante una
#función recursiva.
def factorial(n):
    """función que reciba un número entero positivo y devuelva su
    factorial.
    n: Es un entero positivo.
    Devuelve el factorial de n.
    """
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
print(factorial(5))