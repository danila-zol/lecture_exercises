
max_n = 256
for i in range(max_n + 1):
    unique_pair = [max_n - i, i]
    for i2 in range(max_n + 1):

        if i2 in unique_pair:
            continue

        unique_trinity = list(unique_pair)
        unique_trinity.append(i2)
        k = unique_trinity[0]
        n = unique_trinity[1]
        b = unique_trinity[2]

        if ( k ^ n == k and k ^ b == b ):
            print(f"Success!!!\nK: {k}\nN: {n}\nB: {b}")
        print(unique_trinity)
