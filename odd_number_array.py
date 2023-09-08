from re import findall

user_narr = findall(r"[0-9.]+", input("Input number array: "))
user_narr = [float(x) for x in user_narr]

wrong_narr = []
el1 = None
el2 = None


for n in user_narr:
    el2 = n
    if el1 is not None:
        diff = el1 - el2
        # if (diff > 0 and diff > 1) or (diff < 0 and diff < -1):
        if diff > 1 or diff < -1:
            wrong_narr.append(user_narr.index(n))
        el1 = n
    else:
        el1 = n

if len(wrong_narr) != 0:
    print(wrong_narr[0] if len(wrong_narr) == 1 else wrong_narr)
else:
    print("Not found")