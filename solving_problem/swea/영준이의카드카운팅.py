import sys
sys.stdin = open('영준이의카드카운팅_input.txt')

T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=' ')
    arr = list(input())

    S = [0] * 14
    D = [0] * 14
    H = [0] * 14
    C = [0] * 14

    flag = 1
    for i in range(0, len(arr), 3):
        alpha = arr[i]
        num = int(arr[i+1] + arr[i+2])
        if alpha == 'S':
            S[num] += 1
            if S[num] > 1:
                print('ERROR', end='')
                flag = 0
                break
        elif alpha == 'D':
            D[num] += 1
            if D[num] > 1:
                print('ERROR', end='')
                flag = 0
                break
        elif alpha == 'H':
            H[num] += 1
            if H[num] > 1:
                print('ERROR', end='')
                flag = 0
                break
        elif alpha == 'C':
            C[num] += 1
            if C[num] > 1:
                print('ERROR', end='')
                flag = 0
                break

    if flag == 1:
        print(S.count(0) - 1, end=' ')
        print(D.count(0) - 1, end=' ')
        print(H.count(0) - 1, end=' ')
        print(C.count(0) - 1, end=' ')

    print()




