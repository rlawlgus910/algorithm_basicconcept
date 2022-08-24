import sys
sys.stdin = open('쉬운거스름돈_input.txt')

T = int(input())
arr = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for tc in range(1, T + 1):
    money = int(input())

    ans = [0] * 8

    if money >= 10000:
        ans[0] = money // 50000
        ans[1] = (money % 50000) // 10000
        money = (money % 50000) % 10000

    if money >= 1000:
        ans[2] = money // 5000
        ans[3] = (money % 5000) // 1000
        money = (money % 5000) % 1000

    if money >= 100:
        ans[4] = money // 500
        ans[5] = (money % 500) // 100
        money = (money % 500) % 100

    if money >= 10:
        ans[6] = money // 50
        ans[7] = (money % 50) // 10
        money = (money % 50) % 10

    print(f'#{tc}')
    for i in range(8):
        print(ans[i], end=' ')
    print()