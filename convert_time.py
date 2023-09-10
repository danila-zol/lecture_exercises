user_timestamp = int(input())
tm = user_timestamp % 3600 // 60
th = user_timestamp // 3600
print(f"{th} час(а/ов) и {tm} минут(а/ы)")
