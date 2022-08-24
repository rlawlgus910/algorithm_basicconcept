import sys
sys.stdin = open('퍼펙트셔플_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(input().split())
    if N % 2 == 0:
        middle = N // 2
    else:
        middle = N // 2 + 1

    a_list = arr[:middle]
    b_list = arr[middle:]

    print(f'#{tc}', end=' ')
    for i in range(middle):
        print(a_list[i], end=' ')
        try:
            print(b_list[i], end=' ')
        except:
            continue

    print()