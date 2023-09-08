"""Data for students for practice 4
"""
import random
from typing import TypeAlias

FinishedPlace: TypeAlias = int
FinishedTimeSeconds: TypeAlias = str | int | float
RacerName: TypeAlias = str
RacerTeam: TypeAlias = str

RacerInfo: TypeAlias = dict[
    str, FinishedPlace | FinishedTimeSeconds | RacerName | RacerTeam
]
RaceInfo: TypeAlias = dict[int, RacerInfo]

"""
Выиграл - VOVA!!! Поздравляем!!
_______________________________

Первые три места:

Гонщик на 1 месте:
    Имя: Vova
    Команда: KAMAZ
    Время: 01:00:00 (H:M:S)
    
Гонщик на 2 месте:
    Имя: фыв
    Команда: ыфв
    Время: 02:00:00 (H:M:S)

"""

RANDOM_SEED = 1337
random.seed(RANDOM_SEED)

RACE_DATA: RaceInfo = {
    1: {
        'RacerName': 'Vova',
        'RacerTeam': 'KAMAZ',
        'FinishedPlace': 3,
        'FinishedTimeSeconds': 3600,
    },
    2: {
        'RacerName': 'Vova',
        'RacerTeam': 'VAZ',
        'FinishedPlace': 2,
        'FinishedTimeSeconds': 3321,
    },
    3: {
        'RacerName': 'Gennady',
        'RacerTeam': 'MAZ',
        'FinishedPlace': 1,
        'FinishedTimeSeconds': 3000,
    },
    4: {
        'RacerName': 'Grisha',
        'RacerTeam': 'KAMAZ',
        'FinishedPlace': 5,
        'FinishedTimeSeconds': 5041,
    },
    5: {
        'RacerName': 'Sergey',
        'RacerTeam': 'LG+BT',
        'FinishedPlace': 4,
        'FinishedTimeSeconds': 4144,
    },
}

def generate_race_data(n_racers: int) -> RaceInfo:
    teams = list(set(['KAMAZ', 'MAZ', 'PAZ', 'VAZ', 'TagAZ', 'ZAZ', 'GAZ']))
    names = list(set(['Vova', 'Sergey', 'Andrey', 'Ilya', 'Elena', 'Galya', 'Sasha']))
    places = list(range(1, n_racers + 1))
    places = random.sample(places, len(places))
    racers: list[RacerInfo] = [
        {
            'RacerName': random.choice(names),
            'RacerTeam': random.choice(teams),
            'FinishedPlace': places[-1],
            'FinishedTimeSeconds': random.randint(1000 * places[-1], 1000 * places.pop() + 500),
        } for i, _ in enumerate(range(1, n_racers + 1))
    ]
    
    racers = random.sample(racers, len(racers))
    
    data: RaceInfo = {
        ind: racer for ind, racer in enumerate(racers)
    }
    
    return data