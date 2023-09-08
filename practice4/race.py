from import_this import generate_race_data, RACE_DATA

# Output Structure

# Выиграл - VOVA!!! Поздравляем!!
# _______________________________

# Первые три места:

# Гонщик на 1 месте:
#     Имя: Vova
#     Команда: KAMAZ
#     Время: 01:00:00 (H:M:S)
    
# Гонщик на 2 месте:
#     Имя: фыв
#     Команда: ыфв
#     Время: 02:00:00 (H:M:S)

def sort_racers(race_data : RACE_DATA) -> list: 

    racers_arr = [None for x in race_data.keys()]
    for rd in race_data.values():
        racers_arr[rd["FinishedPlace"] - 1] = rd
    return racers_arr

def print_first_racer(racers_arr : list) -> None:

    win_message = f"Выиграл - {racers_arr[0]['RacerName']}!!! Поздравляем!!\n"
    print(win_message + "-" * (len(win_message) - 1) + "\n")

def print_top3_racers(racers_arr : list) -> None:

    print("Первые три места:\n")
    for rd in racers_arr[:3]:
        ts = rd["FinishedTimeSeconds"] % 60
        tm = rd["FinishedTimeSeconds"] % 3600 // 60
        th = rd["FinishedTimeSeconds"] // 3600
        print(f"Гонщик на {racers_arr.index(rd) + 1} месте:\n" +
            f"\tИмя: {rd['RacerName']}\n" +
            f"\tКоманда: {rd['RacerTeam']}\n" +
            f"\tВремя: {th}:{tm}:{ts}\n")
    


def print_scoreboard(race_data : RACE_DATA) -> None:
    racers_arr = sort_racers(race_data)
    print_first_racer(racers_arr)
    print_top3_racers(racers_arr)

if __name__ == "__main__":
    print_scoreboard(generate_race_data(100))