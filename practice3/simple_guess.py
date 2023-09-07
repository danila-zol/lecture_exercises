# Получаем любое челое число, 
# Вывод корня, если он целый
# Если дробный, вывести "трудно"
# С помощью функции guess

def guess(root):
    for n in range(root+1):
        if (n**2 == root):
            return n
    
    return None

root = guess(int(input("Enter N: ")))
print(root if root else "трудно")