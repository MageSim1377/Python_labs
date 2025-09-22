num = int(input("Enter number: "))

if num % 7 == 0:
    print('Magic number!')
else:
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    print(sum)