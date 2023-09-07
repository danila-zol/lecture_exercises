sides = {
    "камень" : 0b100,
    "ножницы" : 0b010,
    "бумага" : 0b001
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
        print(f"Побеждает игрок {players.index(p) + 1}")
    elif winner == None:
        print("Ничья")
        break


