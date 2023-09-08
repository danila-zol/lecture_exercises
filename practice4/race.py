from import_this import generate_race_data

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

RACE_DATA = generate_race_data(100)

racers_arr = [None for x in RACE_DATA.keys()]
for rd in RACE_DATA.values():
    racers_arr[rd['FinishedPlace'] - 1] = rd

win_message = f"Выиграл - {racers_arr[0]['RacerName']}!!! Поздравляем!!\n"
print(win_message + "-" * len(win_message) + "\n")

print("Первые три места:\n")
for rd in racers_arr[:3]:
    ts = rd["FinishedTimeSeconds"] % 60
    tm = rd["FinishedTimeSeconds"] % 3600 // 60
    th = rd["FinishedTimeSeconds"] // 3600
    print(f"Гонщик на {racers_arr.index(rd) + 1} месте:\n\
    \tИмя: {rd['RacerName']}\n\
    \tКоманда: {rd['RacerTeam']}\n\
    \tВремя: {th}:{tm}:{ts}\n")