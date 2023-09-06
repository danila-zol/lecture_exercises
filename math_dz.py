largest_n = int(input("Input an intger n: "))
divisible_three_sum = 0
divisible_five_sum = 0

for n in range(largest_n):
    if n % 3 == 0 and n % 5 == 0:
        pass
    elif n % 5 == 0:
        divisible_five_sum += n
    elif n % 3 == 0:
        divisible_three_sum += n

print(f"Sum of numbers divisible by 3: {divisible_three_sum}")
print(f"Sum of numbers divisible by 5: {divisible_five_sum}")
