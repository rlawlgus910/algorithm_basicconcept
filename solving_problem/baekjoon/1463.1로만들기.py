def one(num):
    global cnt
    while True:
        while num % 3 == 0:
            num /= 3
            cnt += 1

        if num == 1:
            return

        while num % 2 == 0:
            num /= 2
            cnt += 1

        if num == 1:
            return

        num -= 1
        cnt += 1


        if num == 1:
            return

num = int(input())
cnt = 0
one(num)
print(cnt)
