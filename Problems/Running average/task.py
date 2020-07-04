s = [int(num) for num in input()]

print([(s[i] + s[i + 1]) / 2 for i in range(len(s) - 1)])
