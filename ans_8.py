numbers = [2, 5, 6, 1, 3, 8, 9, 10]
length = len(numbers)

for i in range(length):
    for j in range(length):
        if numbers[i] < numbers[j]:
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp

print(numbers)