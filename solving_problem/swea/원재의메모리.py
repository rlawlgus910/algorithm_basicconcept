# import sys
# sys.stdin = open('원재의메모리_input.txt')

T = int(input())
for tc in range(1, T + 1):
    origin = list(map(int, input()))
    n = len(origin)
    reset = [0] * n

    cnt = 0
    for idx in range(n):
        if origin[idx] != reset[idx]:
            if reset[idx] == 1:
                while idx < n:
                    reset[idx] = 0
                    idx += 1
            else:
                while idx < n:
                    reset[idx] = 1
                    idx += 1
            cnt += 1

    print(f'#{tc} {cnt}')
