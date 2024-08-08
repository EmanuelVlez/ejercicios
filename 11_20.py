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
    stack = []
    pattern = r'[^\[\]\(\)\{\}]'
    resultado = re.sub(pattern, '', cadena)
    opening = "({["
    closing = ")}]"
    pairs = {")": "(", "}": "{", "]": "["}
    
    for char in resultado:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack.pop() != pairs[char]:
                return False
    
    return len(stack) == 0
        
# /*
#  * Crea una función que reciba dos cadenas como parámetro (str1, str2)
#  * e imprima otras dos cadenas como salida (out1, out2).
#  * - out1 contendrá todos los caracteres presentes en la str1 pero NO
#  *   estén presentes en str2.
#  * - out2 contendrá todos los caracteres presentes en la str2 pero NO
#  *   estén presentes en str1.
#  */

def delete_caracter(str1 : str, str2 : str):
    lista1 = str1.split(" ")
    lista2 = str2.split(" ")
    out1 = ""
    out2 = ""
    
    for letra in lista1:
        if letra not in lista2:
            out1+=f"{letra} "
        
    for letra in lista2:
        if letra not in lista1:
            out2+=f"{letra} "
        
    print("out1:", out1)
    print("out2:", out2)


# /*
#  * Escribe una función que reciba un texto y retorne verdadero o
#  * falso (Boolean) según sean o no palíndromos.
#  * Un Palíndromo es una palabra o expresión que es igual si se lee
#   * de izquierda a derecha que de derecha a izquierda.
#  * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
#  * Ejemplo: Ana lleva al oso la avellana.
#  */

def palindromo(texto : str):
    texto = (texto.replace(" ", "")).lower()
    new_texto = ""
    for i in range(len(texto)):
        new_texto+=texto[(len(texto)-1)-i]
    
    if texto == new_texto:
        return True
    else:
        return False
        
        


if __name__=="__main__":
    #print(balanceo("Hola([])"))
    #delete_caracter("hola que mas", "que mas lindo")
    print(palindromo("HOla"))