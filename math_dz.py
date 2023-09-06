user_N = int(input("Input an intger n: "))

def divisible_sum(l_num, divisor):
    last_element = l_num - (l_num % divisor)
    element_count = l_num // divisor
    return ((divisor + last_element) * element_count) / 2

divisible_tf_sum = divisible_sum(user_N, 3) + divisible_sum(user_N, 5) - divisible_sum(user_N, 15)

print(f"Sum of dividable by 3 and 5: {divisible_tf_sum}")