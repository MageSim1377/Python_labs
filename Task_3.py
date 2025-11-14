numberStr = input("Enter list of nunmbers: ")

numbers = numberStr.split()

for i in range(len(numbers)):
    numbers[i] = float(numbers[i])

for i in range(len(numbers)):
    for j in range(len(numbers) - 1):
        if numbers[j] < numbers[j + 1]:
            t = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = t

print(numbers[1])