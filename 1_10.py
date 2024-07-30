# /*
#  * Escribe un programa que muestre por consola (con un print) los
#  * números de 1 a 100 (ambos incluidos y con un salto de línea entre
#  * cada impresión), sustituyendo los siguientes:
#  * - Múltiplos de 3 por la palabra "fizz".
#  * - Múltiplos de 5 por la palabra "buzz".
#  * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#  */

def fizz_buzz():
    for i in range(1,101):
        if i%3==0 and i%5==0:
            print(i,"fizzbuzz")
        elif i%3==0:
            print(i,"fizz")
        elif i%5==0:
            print(i,"buzz")
            
            
# /*
#  * Escribe una función que reciba dos palabras (String) y retorne
#  * verdadero o falso (Bool) según sean o no anagramas.
#  * - Un Anagrama consiste en formar una palabra reordenando TODAS
#  *   las letras de otra palabra inicial.
#  * - NO hace falta comprobar que ambas palabras existan.
#  * - Dos palabras exactamente iguales no son anagrama.
#  */

def anagram(word1 : str, word2 : str) ->bool:
    if word1.lower() == word2.lower():
        return False
    return sorted(word1.lower())==sorted(word2.lower())

# /*
#  * Escribe un programa que imprima los 50 primeros números de la sucesión
#  * de Fibonacci empezando en 0.
#  * - La serie Fibonacci se compone por una sucesión de números en
#  *   la que el siguiente siempre es la suma de los dos anteriores.
#  *   0, 1, 1, 2, 3, 5, 8, 13...
#  */

def fibonacci():
    
    i=0
    new_number = 1
    number_anterior = 0
    
    while i<49:
        print(number_anterior)
        number = new_number
        new_number = number+number_anterior
        number_anterior = number 
        i+=1
        
        
# /*
#  * Escribe un programa que se encargue de comprobar si un número es o no primo.
#  * Hecho esto, imprime los números primos entre 1 y 100.
#  */

def primos():
    for i in range(1,101):
        
        if i >= 2:
            divisible = True
            for j in range(2, i):
                if i%j==0:
                    divisible = False
                    break
            
            if divisible:
                print(i, "es primo")

# /*
#  * Crea una única función (importante que sólo sea una) que sea capaz
#  * de calcular y retornar el área de un polígono.
#  * - La función recibirá por parámetro sólo UN polígono a la vez.
#  * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#  * - Imprime el cálculo del área de un polígono de cada tipo.
#  */

def area_poligono(clase):
    print(clase.area())
    
class Polygon:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

class Triangulo(Polygon):
    def __init__(self, base, altura):
        super().__init__(base, altura)
    def area(self):
        return (self.base * self.altura)/2
    
class Rectángulo(Polygon):
    def __init__(self, base, altura):
        super().__init__(base, altura)
    def area(self):
        return (self.base * self.altura)
    
class Cuadrado(Polygon):
    def __init__(self, base, altura):
        super().__init__(base, altura)
    def area(self):
        return (self.base * self.altura)


# /*
#  * Crea un programa que se encargue de calcular el aspect ratio de una
#  * imagen a partir de una url.
#  * - Url de ejemplo:
#  *   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
#  * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
#  *   imagen de 1920*1080px.
#  */
import requests
from PIL import Image
from io import BytesIO
def ratio_image(url):
    # Descargar la imagen
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Open the image using PIL
        img = Image.open(BytesIO(response.content))
        
        # Get the dimensions
        width, height = img.size
        i=2
        while i <= min(width,height):
            if width%i==0 and height%i==0:
                width/=i
                height/=i
                i=2
            i+=1
        print(f"{int(width)}:{int(height)}")
            
    else:
        print("Error en traer la imagen")
        
# /*
#  * Crea un programa que invierta el orden de una cadena de texto
#  * sin usar funciones propias del lenguaje que lo hagan de forma automática.
#  * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
#  */

def invertir(cadena : str):
    new_cadena = ''
    for i in range(len(cadena)):
        new_cadena+=cadena[len(cadena)-1-i]
    print(new_cadena)
    

# /*
#  * Crea un programa que cuente cuantas veces se repite cada palabra
#  * y que muestre el recuento final de todas ellas.
#  * - Los signos de puntuación no forman parte de la palabra.
#  * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
#  * - No se pueden utilizar funciones propias del lenguaje que
#  *   lo resuelvan automáticamente.
#  */

import re 

def count_palabras(cadena : str):
    patron = r'[^a-zA-Z0-9\s]'
    cadena = re.sub(patron,'',cadena)
    list_palabras = cadena.lower().split(" ")
    diccionario ={}
    for i in list_palabras:
        if i not in diccionario:
            diccionario[i]= 1
        else:
            diccionario[i]+=1
    
    print(diccionario)
    
# /*
#  * Crea un programa se encargue de transformar un número
#  * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
#  */

def decimal_a_binario(numero):
    if numero == 0:
        return "0"
    
    binario = ""
    while numero > 0:
        binario = str(numero % 2) + binario
        numero //= 2
    
    print(binario)


# /*
#  * Crea un programa que sea capaz de transformar texto natural a código
#  * morse y viceversa.
#  * - Debe detectar automáticamente de qué tipo se trata y realizar
#  *   la conversión.
#  * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
#  *   o símbolos y dos espacios entre palabras "  ".
#  * - El alfabeto morse soportado será el mostrado en
#  *   https://es.wikipedia.org/wiki/Código_morse.
#  */
 
def texto_a_morse(texto : str):
    # Diccionario de código Morse
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.', ' ': ' '
    }
    
    patron = r'[^a-zA-Z0-9\s]'
    texto = re.sub(patron,'',texto)
    texto = texto.upper()
    print(texto)
    texto_morse = ""
    for i in texto:
        if i==" ":
            texto_morse = texto_morse + "  "
        else:
            texto_morse = texto_morse + morse_dict[i]
    print(texto_morse)
        
    #print(new_cadena)
if __name__=="__main__":
    #fizz_buzz() 
    #print(anagram("hola","hola"))
    #fibonacci()
    #primos()
    #area_poligono(Triangulo(5, 5))
    #ratio_image("https://i.blogs.es/0ca9a6/aa/1366_2000.jpeg")
    #invertir("Hola mundo")
    #count_palabras("Hola, $/)Hola hola que (/&/mas como estan que")
    #decimal_a_binario(2)
    texto_a_morse("Hola")