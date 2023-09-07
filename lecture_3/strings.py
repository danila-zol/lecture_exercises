from string import digits
# new_name = input("Type name: ")
# greet_message = "hello bob"
# greet_message = (
#     greet_message[:-3] + new_name
# )
# print(greet_message)

words = "<!--dsa das das-->"
words = (
    words.strip("<!-").strip("->")
)
words_array = words.split()
print(words_array)

leet = "C00L H4X00R"
for c in leet:
    if c in digits:
        print(c)

words2 = "Hello, Bob, are you bob? BOB!!!"
words2 = words2.lower().replace("bob", "gregory")
print(words2)