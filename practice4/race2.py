from import_this import generate_race_data

def sort_racers(race_data) -> list: 
    sorted_rd = {}
    for v in race_data.values():
        fp = v["FinishedPlace"]
        sorted_rd[fp] = v

    return sorted_rd

sorted = sort_racers(generate_race_data(10))
print(sorted)