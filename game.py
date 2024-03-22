import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo", "inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

# Número máximo de fallos permitidos
fails = 0

# Dificultad por defecto
dificultad = "d"

# Lista para almacenar las letras adivinadas
guessed_letters = []
print("¡Bienvenido al juego de adivinanzas!")
print("Sólo podrás tener 10 fallos")

# Selección de dificultad
print("Por favor, elige dificultad deseada (f = facil, m = medio, d = dificil)")
dificultad = input("Ingrese la dificultad: ").lower()

print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

# Definir la variable word_displayed según la dificultad
if dificultad == "f":
    word_displayed = "".join([char if char in "aeiou" else "_" for char in secret_word])
elif dificultad == "m":
    word_displayed = secret_word[0] + "_" * (len(secret_word) - 2) + secret_word[-1]
else:
    word_displayed = "_" * len(secret_word)

# Mostrar la palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

while fails < 10:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    
    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
    
    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)

    # Verificar si ingresó una letra
    if letter == "":
        print("Debes ingresar una letra")
        print(f"Cantidad de fallos: {fails}")

    # Verificar si la letra está en la palabra secreta
    elif letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
        print(f"Cantidad de fallos: {fails}")

        # Actualizar word_displayed para mostrar todas las instancias de la letra
        for i, char in enumerate(secret_word):
            if char == letter:
                word_displayed = word_displayed[:i] + char + word_displayed[i+1:]

    else:
        fails += 1
        print("Lo siento, la letra no está en la palabra.")
        print(f"Cantidad de fallos: {fails}")

    # Mostrar la palabra parcialmente adivinada
    print(f"Palabra: {word_displayed}")

    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break

else:
    print(f"¡Oh no! Has alcanzado 10 fallos.")
    print(f"La palabra secreta era: {secret_word}")
