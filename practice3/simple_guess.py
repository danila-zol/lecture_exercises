# Получаем любое челое число, 
# Вывод корня, если он целый
# Если дробный, вывести "трудно"
# С помощью функции guess
from math import floor

def guess(root):
    for n in range(root):
        if (n**2 == root):
            return n
    
    return None

root = guess(int(input("Enter N: ")))
if root:
    print(root)
else:
    print("трудно")