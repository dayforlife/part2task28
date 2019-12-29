def myfunc():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
    for i in numbers:
        x = numbers.index(i)
        if i > 0:
            numbers[x] = 1
        elif i < 0:
            numbers[x] = -1
    print(numbers)
myfunc()