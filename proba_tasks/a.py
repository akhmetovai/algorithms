n = int(input())

if n > 0:
    rus = input().split()
    foreign = input().split()
    for i in range(n - 1):
        print(rus[i] + ' ' + foreign[i], end=' ')
        print(rus[n - 1] + ' ' + foreign[n - 1])
else:
    print()
