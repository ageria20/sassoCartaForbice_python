player1 = input("Inserisci il nome del giocatore 1: ")
player2 = input("Inserisci il nome del giocatore 2: ")

print(f"Giocatore 1: {player1}")
print(f"Giocatore 2: {player2}")

choices = ["rock", "paper", "scissors"]
choice1 = input("Scelta Giocatore 1: ")
choice2 = input("Scelta Giocatore 2: ")

punteggio1 = 0
punteggio2 = 0

if choice1 == choice2:
    print("Pareggio!")
elif choice1 == "sasso" and choice2 == "carta":
    print(f"{player2} ha vinto!")
    punteggio2 += 1
elif choice1 == "sasso" and choice2 == "forbici":
    print(f"{player1} ha vinto!")
    punteggio1 += 1
elif choice1 == "carta" and choice2 == "forbici":
    print(f"{player2} ha vinto!")
    punteggio2 += 1
elif choice1 == "carta" and choice2 == "sasso":
    print(f"{player1} ha vinto!")
    punteggio1 += 1
elif choice1 == "forbici" and choice2 == "sasso":
    print(f"{player2} ha vinto!")
    punteggio2 += 1
elif choice1 == "forbici" and choice2 == "carta":
    print(f"{player1} ha vinto!")
    punteggio1 += 1

