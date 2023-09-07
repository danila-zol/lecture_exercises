def my_personal_sum(num_list : list) -> int | float:
    answer = 0
    for n in num_list:
        answer += n
    return answer

print(my_personal_sum([3, 5, 1]))
print(sum([3, 5, 1]))