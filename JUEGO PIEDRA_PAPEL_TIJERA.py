import random

def reglas(jugada_usuario, jugada_maquina): # ------ La funcion que impone las reglas del juego.
    if jugada_maquina == jugada_usuario:
        print("-- EMPATE --")
        return "empate"
    
    elif jugada_usuario == "tijera" and jugada_maquina == "papel":
        print(f"-- GANA {nombre} -- ")
        return "usuario"
    elif jugada_maquina == "tijera" and jugada_usuario == "papel":
        print("-- GANA MAQUINA -- ")
        return "maquina"

    elif jugada_usuario == "papel" and jugada_maquina == "piedra":
        print(f"-- GANA {nombre} -- ")
        return "usuario"
    elif jugada_maquina == "papel" and jugada_usuario == "piedra":
        print("-- GANA MAQUINA -- ")
        return "maquina"

    elif jugada_usuario == "piedra" and jugada_maquina == "tijera":
        print(f"-- GANA {nombre} -- ")
        return "usuario"
    elif jugada_maquina == "piedra" and jugada_usuario == "tijera":
        print("-- GANA MAQUINA -- ")
        return "maquina"


puntos_usuario = 0
puntos_maquina = 0

nombre = input("¿Cual es tu nombre? ")

for i in range(3):
    print()

    print("----- JUEGO: PIEDRA, PAPEL O TIJERA -----")

    print()

    print("Elija una opcion:")
    print("- Piedra")
    print("- Papel")
    print("- Tijera")

    print()

    jugada_usuario = input(" ---> ").lower().strip()
    
    print()

    if jugada_usuario == "piedra":
        print("Elegiste piedra")
    elif jugada_usuario == "papel":
        print("Elegiste papel")
    elif jugada_usuario == "tijera":
        print("Elegiste tijera")
    else:
        print("Opcion no valida")

    print()

    jugada_maquina = random.choice(["piedra", "papel", "tijera"])

    print(f"{nombre} = {jugada_usuario} ---- Maquina = {jugada_maquina}")

    print()

    resultado = reglas(jugada_usuario, jugada_maquina)

    if resultado == "usuario":
        puntos_usuario += 1
    elif resultado == "maquina":
        puntos_maquina += 1

print()

print("---- RESULTADO FINAL ----")

print()

print(f"{nombre} = {puntos_usuario}, Maquina = {puntos_maquina}")

print()


if puntos_maquina < puntos_usuario:
  print(f"GANADOR = {nombre}")
elif puntos_maquina > puntos_usuario:
  print("GANADOR MAQUINA")
elif puntos_maquina == puntos_usuario:
  print("EMPATE")
else:
  pass

print()






