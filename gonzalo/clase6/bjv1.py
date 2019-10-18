import random

#carta_jugador  = 0
#carta_banca    = 0
puntos_jugador = 0
puntos_banca   = 0

total_puntos_jugador = 0
total_puntos_banca   = 0

ya_hay_blackjack = False

# cargar un palo con 10 cartas del 1 al 10, y con las cuatro últimas q valen 10 (baraja francesa)
palo = list(range(1,10))
for diez in range(4):
    palo.append(10)

baraja = palo + palo + palo + palo


def repartir_carta_jugador():
    # dar carta
    carta_jugador = random.choice(baraja)
    # quitar carta de la baraja
    baraja.remove(carta_jugador)
    return carta_jugador

def repartir_carta_banca():
    # dar carta
    carta_banca   = random.choice(baraja)
    # quitar carta de la baraja
    baraja.remove(carta_banca)
    return carta_banca

def mostrar_puntuacion_jugador(num_puntos_jugador):
    # mostrar puntuacion
    print(" Tu puntuación es: ", num_puntos_jugador)

def seguir_jugando():
    otra_carta = input(" ¿Quieres otra carta ?")
    if otra_carta.upper() == 'S':
        return True
    else:
        return False

#def sigue_jugando_banca():
#    while total_puntos_banca < 15:
#        repartir_carta_banca()
#        acumular_puntuacion_banca()

def evaluar_si_blackjack():
    if total_puntos_jugador == 21 and total_puntos_banca == 21:
        print(" Tú y la Banca tenéis puntuación 21. Gana la Banca ")
        return True
    elif total_puntos_jugador > 21 and total_puntos_banca < 21:
        print(" La puntuación de la Banca es: ", total_puntos_banca)
        print(" Tu puntuación es: ", total_puntos_jugador)
        print(" Ha ganado la Banca ")
        return True
    elif total_puntos_jugador < 21 and total_puntos_banca > 21:
        print(" La puntuación de la Banca es: ", total_puntos_banca)
        print(" Tu puntuación es: ", total_puntos_jugador)
        print(" Has GANADO !!! ")
        return True
    elif total_puntos_jugador > 21 and total_puntos_banca > 21:
        print(" La puntuación de la Banca es: ", total_puntos_banca)
        print(" Tu puntuación es: ", total_puntos_jugador)
        print(" FIN de JUEGO - Nadie gana ")
        return True
    else:
        if total_puntos_jugador == 21:
            print(" Tu puntuación es: ", total_puntos_jugador)
            print(" La puntuación de la Banca es: ", total_puntos_banca)            
            print(" Has GANADO!!! ")
            return True
        if total_puntos_banca == 21:
            print(" Tu puntuación es: ", total_puntos_jugador)            
            print(" La puntuación de la Banca es: ",total_puntos_banca)
            print(" Ha ganado la Banca ")
            return True
        else:
            return False


def quien_esta_mas_cerca_blackjack():
    if total_puntos_banca > 21:
        print(" La puntuación de la banca es: ", total_puntos_banca)
        print(" Tu puntuación es: ", total_puntos_jugador)
        print(" Has GANADO!!! ")
    else:
        if total_puntos_banca < total_puntos_jugador:
            print(" La puntuación de la banca es: ", total_puntos_banca)
            print(" Tu puntuación es: ", total_puntos_jugador)
            print(" Has GANADO!!! ")
        else:
            print(" La puntuación de la Banca es: ", total_puntos_banca)
            print(" Tu puntuación es: ", total_puntos_jugador)
            print(" Ha ganado la Banca ")



# =============================================================================

print("                                     ")
print("                                     ")
print("#  ################################ #")
print("#  -------------------------------  #")
print("#  EMPIEZA el juego del BLACK JACK  #")
print("#  -------------------------------  #")
print("#  ################################ #")
print("                                     ")
print("                                     ")


# PRIMER  reparto de cartas
puntos_jugador = repartir_carta_jugador()
puntos_banca = repartir_carta_banca()
total_puntos_jugador = puntos_jugador + total_puntos_jugador
total_puntos_banca   = puntos_banca + total_puntos_banca
mostrar_puntuacion_jugador(total_puntos_jugador)


# SEGUIR  jugando

# Juegan los dos:  Jugador  y  Banca
while seguir_jugando():
    puntos_jugador = repartir_carta_jugador()
    puntos_banca = repartir_carta_banca()
    #
    total_puntos_jugador = puntos_jugador + total_puntos_jugador
    total_puntos_banca  = puntos_banca + total_puntos_banca
    #
    mostrar_puntuacion_jugador(total_puntos_jugador)
    if evaluar_si_blackjack():
        ya_hay_blackjack = True
        break
    else:
        ya_hay_blackjack = False

if ya_hay_blackjack == False:
    while total_puntos_banca < 15:
        puntos_banca = repartir_carta_banca()
        total_puntos_banca  = puntos_banca + total_puntos_banca
        
    quien_esta_mas_cerca_blackjack()



