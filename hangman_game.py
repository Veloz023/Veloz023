import time
import random

jugar_negativo = "No", "no", "nO", "NO", "n", "N"
jugar_positivo = "Si", "si", "sI", "SI", "s", "S"
ahorcado = (
    r'''
        +---+
        |   |
            |
            |
            |
            |
    ===========''',
    r'''
       +---+
       |   |
       O   |
           |
           |
           |
    ==========''',
    r'''
       +---+
       |   |
       O   |
       |   |
           |
           |
    ==========''',
    r'''
       +---+
       |   |
       O   |
      /|   |
           |
           |
    ==========''',
    r'''
       +---+
       |   |
       O   |
      /|\  |
           |
           |
    ==========''',
    r'''
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
    ==========''',

    r'''
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
    =========='''
)


def eleccion_img(f):
    print(ahorcado[f])


# Bienvenida al jugador
# pequeña imagen para hacer mas llamativa el juego

print("\n")
print("Bienvenido al juego del ahorcado :)")
eleccion_img(6)
print("\n")
print("-----------------------------------------------------------------------")
nombre = input("¡Hola Bienvenido! ¿Como te llamas? ")
print("-----------------------------------------------------------------------")
time.sleep(2)


# Esta es la funcion donde se escoge la palabra aleatoria/random

def lista_categorias(categoria):
    if categoria == 1:
        frutas = random.choice(open("frutas_verduras.txt", "r").readline().strip().upper().split(" "))
        return frutas
    elif categoria == 2:
        paises = random.choice(open("paises.txt", "r").readline().strip().upper().split(" "))
        return paises
    elif categoria == 3:
        animales = random.choice(open("animales.txt", "r").readline().strip().upper().split(" "))
        return animales
    else:
        videojuegos = random.choice(open("videojuegos.txt", "r").readline().strip().upper().split(" "))
        return videojuegos


# Esta funcion es la encargada de escoger la palabra random de acuerdo
# a la seleccion del usuario

def palabras():
    print("-----------------------------------------------------------------------")
    print("\n""Estas son las categorias disponibles:")
    print("\t1. Frutas y Verduras")
    print("\t2. Paises")
    print("\t3. Animales")
    print("\t4. Videojuegos")
    print("-----------------------------------------------------------------------")
    print("\n")
    seleccion = int(input("Elige la que mas te guste: "))
    print("-----------------------------------------------------------------------")
    lista_palabras = lista_categorias(seleccion)
    return lista_palabras


# Inicio del programa


intentos = 8
victorias = 0
derrotas = 0
partidas = 0
for x in range(intentos):
    partidas = partidas + 1
    play = input(nombre + " ¿Quieres jugar? ")
    if play in jugar_negativo:
        print("Gracias por participar")
        print(":D")
        break
    elif play in jugar_positivo:
        # Declaracion de variables dentro del bucle por posible rejuego
        # Se establecen las variables que dan vida al juego
        letras_probadas = []
        letras = " "
        vidas = 6
        fallos = 0

        # Obtencion de palabra random
        palabra = palabras()

        # Bucle de reconocimiento e impresion de la palabra clave
        while vidas > 0:
            intentos = 0
            eleccion_img(fallos)
            for letra in palabra:

                if letra in letras:
                    print(letra, end=" ")

                else:
                    print("_", end=" ")
                    intentos = intentos + 1

                    # Sentencia de reconocimiento de victoria del jugador
            if intentos == 0:
                eleccion_img(fallos)
                print("Felicidades, ganaste!")
                victorias = victorias + 1
                break

            print(" ")
            print(" ")

            # Recoleccion de letras insertadas
            # Se analiza la letra ingresada con el usuario
            # Se valida que la letra este dentro de la palabra aleatoria

            while True:
                print("Letras probadas: ", end=" ")
                print(letras_probadas)
                tu_letra = input("introduce una letra: ")
                letras += tu_letra.upper()
                tu_letra = tu_letra.upper()
                if len(tu_letra) != 1:
                    print("Por favor, introduce una letra.")
                elif tu_letra in letras_probadas:
                    print("Ya has probado esa letra. Elige otra: ")
                elif tu_letra not in 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ':
                    print("Por favor ingresa una letra:")
                else:
                    letras_probadas.append(tu_letra)
                    break

            # Se valida que las letras dentro de la palabra clave
            # Si la palabra no es correcta se imprime los fallos/errores del usuario

            if tu_letra not in palabra:
                vidas = vidas - 1
                vidas2 = str(vidas)
                fallos = fallos + 1
                eleccion_img(fallos)
                print("Te equivocaste.")
                print("Vidas restantes:", end=" ")
                print(vidas2)
                print(" ")

            # Sentencia  de perdida total de vidas
            # Se imprime la palabra correcta

            if vidas == 0:
                eleccion_img(fallos)
                print("¡Te quedaste sin vidas!")
                print("La palabra era: ", "---", end=" ")
                print(palabra, end=" ")
                print("---")
                derrotas = derrotas + 1

        # Pantalla final y posible rejuego
        # Se imprime la victorias y derrotas

        print("-----------------------------------------------------------------------")
        print("Estos son tus resultados hasta el momento")
        print("Victorias:", victorias)
        print("Derrotas:", derrotas)
        print("Partidas hasta el momento: ", partidas)
        print("-----------------------------------------------------------------------")

        # Bucle de procesamiento de decision
        # Se retorna a la funcion de palabras para repetir el ciclo de juego
        if victorias < 5 and derrotas < 3:
            time.sleep(1)
            eleccion_img(0)
        else:
            print("El juego ha terminado")
            if victorias == 5:
                time.sleep(1)
                print("\n")
                print("-----------------------------------------------------------------------")
                print("¡Felicidades has ganado! :D")
                print("Estos son tus resultados:")
                print("Victorias:", victorias)
                print("Derrotas:", derrotas)
                print("-----------------------------------------------------------------------")
                print("\n")
            else:
                time.sleep(1)
                print("\n")
                print("-----------------------------------------------------------------------")
                print("¡Lo sentimos has perdido :(!")
                print("Estos son tus resultados:")
                print("Victorias:", victorias)
                print("Derrotas:", derrotas)
                print("-----------------------------------------------------------------------")
                print("\n")
    else:
        print("Hubo un error con tu respuesta")
        eleccion_img(6)
        break
