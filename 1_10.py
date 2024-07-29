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
import numpy as np
def ratio_image(url):
    # Descargar la imagen
    response = requests.get(url)

    # Convertir los datos de la imagen en un array de NumPy
    image_array = np.array(bytearray(response.content), dtype=np.uint8)

    print(image_array)

if __name__=="__main__":
    #fizz_buzz() 
    #print(anagram("hola","hola"))
    #fibonacci()
    #primos()
    #area_poligono(Triangulo(5, 5))
    ratio_image("https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png")