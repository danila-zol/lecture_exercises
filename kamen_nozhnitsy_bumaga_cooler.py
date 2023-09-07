sides = {
    "камень" : 4,
    "ножницы" : 2,
    "бумага" : 1
}

players = input().lower().split()

match sides[players[0]] ^ sides[players[1]]:
    case 6:
        winner = "камень"
    case 3:
        winner = "ножницы"
    case 5:
        winner = "бумага"
    case _:
        winner = None

for p in players:
    if p == winner:
        print(f"Побеждает игрок {players.index(p)}")
    elif winner == None:
        print("Ничья")


