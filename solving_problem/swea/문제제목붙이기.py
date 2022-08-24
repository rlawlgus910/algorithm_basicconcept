import sys
sys.stdin = open('문제제목붙이기_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    first = []
    for i in range(N):
        first.append(input()[0])

    first = set(first)
    first = sorted(first)

    if first[0] == 'A':
        cnt = 1
        for i in range(1, N-1):
            if ord(first[i - 1]) + 1 == ord(first[i]):
                cnt += 1
            else:
                break
    else:
        cnt = 0
    print(f'#{tc} {cnt}')