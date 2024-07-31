# /*
#  * Crea un programa que comprueba si los paréntesis, llaves y corchetes
#  * de una expresión están equilibrados.
#  * - Equilibrado significa que estos delimitadores se abren y cieran
#  *   en orden y de forma correcta.
#  * - Paréntesis, llaves y corchetes son igual de prioritarios.
#  *   No hay uno más importante que otro.
#  * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
#  * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
#  */
import re
def balanceo(cadena : str):
    pattern = r'[^\[\]\(\)\{\}]'

    # Ejemplo de uso
    texto = "Esto es un [ejemplo] con (paréntesis) y {llaves}."
    resultado = re.sub(pattern, '', texto)
    for i in range(len(resultado)):
        resultado[i]
        




if __name__=="__main__":
    balanceo("Hola()")