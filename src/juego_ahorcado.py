import random

def elige_palabra(fichero="palabras.txt"):
    """
    Devuelve una palabra aleatoria tomada de un fichero de texto.

    Parámetros:
        fichero: ruta al archivo que contiene las palabras (una por línea).

    Devuelve:
        Una palabra (str) elegida al azar del fichero.
    """
    with open(fichero, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    # Quitar saltos de línea y espacios
    palabras = [linea.strip() for linea in lineas if linea.strip() != ""]
    return random.choice(palabras)


def normalizar(cadena):
    """
    Normaliza una cadena de texto realizando las siguientes operaciones:
        - convierte a minúsculas
        - quita espacios en blanco al principio y al final
        - elimina acentos y diéresis        
    
    Parámetros:
      cadena: cadena de texto que hay que sanear
    
    Devuelve:
      Cadena de texto con la palabra normalizada
    """
    cadena = cadena.lower().strip()
    cadena = cadena.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("ü", "u")

    return cadena

def enmascarar(palabra_secreta, letras_usadas=""):
    '''Devuelve una cadena de texto con la palabra enmascarada. 
    Las letras que no están en letras_usadas se muestran como guiones bajos (_).

    Parámetros:
    - palabra_secreta: cadena de texto con la palabra que se debe enmascarar
    - letras_usadas: cadena de texto con las letras que se deben mostrar (por defecto cadena vacía)

    Devuelve:
      Cadena de texto con la palabra enmascarada
    '''
    cadena = ""

    for char in palabra_secreta:
        if normalizar(char) in letras_usadas:
            cadena += char
        else:
            cadena += "_"

    return cadena


def ha_ganado(palabra_enmascarada: str):
    '''Devuelve True si el jugador ha ganado (es decir, si no quedan letras por descubrir en la palabra enmascarada).

    Parámetros:
    - palabra_enmascarada: cadena de texto con la palabra enmascarada 

    Devuelve:
    - True si el jugador ha ganado, False en caso contrario
    '''
    return True if "_" not in palabra_enmascarada else False


def mostrar_estado(palabra_enmascarada: str, intentos_restantes: int, letras_usadas=""):
    estado = "Estado: " + " ".join(palabra_enmascarada)
    if letras_usadas != "":
        letras = "Letras usadas: " + letras_usadas
    else:
        letras = "Letras usadas: ninguna"
    intentos = "Intentos restantes: " + str(intentos_restantes)

    print(estado + "\n" + letras + "\n" + intentos)

def pedir_letra(letras_usadas):
    while True:
        pedido = input("Introduce una letra: ")

        if not pedido.isalpha():
            print("   Debes introducir una letra")
        elif len(pedido) != 1:
            print("   Debes introducir una única letra")
        elif pedido in letras_usadas:
            print("   Esa letra ya la has usado anteriormente")
        else:
            break
    return normalizar(pedido)

def jugar():
    intentos = 6
    letras_usadas = ""
    palabra = elige_palabra()
    palabra_enmascarada = enmascarar(palabra, letras_usadas)

    print("¡Bienvenido al juego del ahorcado!\n")

    while not ha_ganado(palabra_enmascarada):
        mostrar_estado(palabra_enmascarada, intentos, letras_usadas)
        letra = pedir_letra(letras_usadas)
        letras_usadas += letra
        if letra in normalizar(palabra):
            print("✅ ¡Bien!\n")
        else:
            print("❌ La letra no está en la palabra.\n")
            intentos -= 1
        palabra_enmascarada = enmascarar(palabra, letras_usadas)
    print(f"🎉 ¡Has ganado! La palabra era: {palabra_enmascarada}")
jugar()

# TODO: Escribe el programa principal