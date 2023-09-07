sides = {
    "камень" : 8,
    "ножницы" : 4,
    "бумага" : 1
}

players = input().lower().split()

match sides[players[0]] ^ sides[players[1]]:
    case 0b110:
        winner = "камень"
    case 0b011:
        winner = "ножницы"
    case 0b101:
        winner = "бумага"
    case _:
        winner = None

for p in players:
    if p == winner:
        print(f"Побеждает игрок {players.index(p)}")
    elif winner == None:
        print("Ничья")


