def convert_ab_to_int(a: str, b: str) -> (int, int):
    if ("q" in [a, b]):
        exit()
    a, b = int(a), int(b)
    return a, b

def divide_ab(a: int, b: int) -> float:
    if 3 in [a, b]:
        raise AttributeError("Я НЕНАВИЖУ ТРОЙКИ")
    return a / b

while True:
    try:
        a, b = input("Введите двы числа для их суммы: ").split()
        a, b = convert_ab_to_int(a, b) 
        ab_sum = a + b
        division_score = divide_ab(a, b)

    except ValueError as e:
        print(f"Ошибка {e}")
        print("Дружище, ты дурак, введи числа!!!")
        continue
    except ZeroDivisionError as e:
        print(f"Ошибка {e}")
        print("Дружище, давай без нулей")
        continue   
    except AttributeError as ex:
        print(f"Разработчик злой писюкан, потому что он, цитата: {ex}")
        print("Сделай пж как он просит")
        continue
    finally:
        print("мы в финале шоу танцы")
   
    print(f"Сумма {a} + {b} = {ab_sum}")
    print(f"Деление {a} / {b} = {division_score}")
    print()