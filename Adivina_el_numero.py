#Juego de adivina el numero
import random


def jugar():
    print("=" * 40)
    print("🎯 ¡ADIVINA EL NÚMERO! 🎯")
    print("=" * 40)

    # Configuración del juego
    numero_min = 1
    numero_max = 100
    intentos_maximos = 7

    numero_secreto = random.randint(numero_min, numero_max)
    intentos_usados = 0

    print(f"\nHe pensado un número entre {numero_min} y {numero_max}.")
    print(f"Tienes {intentos_maximos} intentos para adivinarlo.\n")

    while intentos_usados < intentos_maximos:
        intentos_restantes = intentos_maximos - intentos_usados

        try:
            entrada = input(f"Intento {intentos_usados + 1}/{intentos_maximos} - Ingresa tu número: ")
            intento = int(entrada)
        except ValueError:
            print("⚠️  Por favor, ingresa un número válido.\n")
            continue

        if intento < numero_min or intento > numero_max:
            print(f"⚠️  El número debe estar entre {numero_min} y {numero_max}.\n")
            continue

        intentos_usados += 1

        if intento == numero_secreto:
            print(f"\n🎉 ¡Felicidades! ¡Adivinaste el número {numero_secreto}!")
            print(f"Lo lograste en {intentos_usados} intento(s).")
            return True
        elif intento < numero_secreto:
            print("📈 Muy bajo. Intenta con un número más alto.\n")
        else:
            print("📉 Muy alto. Intenta con un número más bajo.\n")

        if intentos_usados < intentos_maximos:
            restantes = intentos_maximos - intentos_usados
            print(f"   Te quedan {restantes} intento(s).\n")

    print(f"\n😢 ¡Se acabaron los intentos! El número era {numero_secreto}.")
    return False


def main():
    seguir_jugando = True

    while seguir_jugando:
        jugar()

        respuesta = input("\n¿Quieres jugar de nuevo? (s/n): ").strip().lower()
        seguir_jugando = respuesta in ("s", "si", "sí", "y", "yes")

    print("\n¡Gracias por jugar! 👋")


if __name__ == "__main__":
    main()