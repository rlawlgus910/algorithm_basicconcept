import sys
sys.stdin = open('기지국_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]

    # A기지국
    da = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    # B기지국
    db = [[0, 1], [0, 2], [0, -1], [0, -2], [1, 0], [2, 0], [-1, 0], [-2, 0]]
    # C기지국
    dc = [[0, 1], [0, 2], [0, 3], [0, -1], [0, -2], [0, -3], [1, 0], [2, 0], [3, 0], [-1, 0], [-2, 0], [-3, 0]]

    for i in range(N):
        for j in range(N):
            # A기지국
            if arr[i][j] == 'A':
                for k in range(4):
                    ni = i + da[k][0]
                    nj = j + da[k][1]
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'H':
                        arr[ni][nj] = 'X'

            # B기지국
            elif arr[i][j] == 'B':
                for k in range(8):
                    ni = i + db[k][0]
                    nj = j + db[k][1]
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'H':
                        arr[ni][nj] = 'X'

            # C기지국
            elif arr[i][j] == 'C':
                for k in range(12):
                    ni = i + dc[k][0]
                    nj = j + dc[k][1]
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'H':
                        arr[ni][nj] = 'X'



    ans = 0
    for i in range(N):
        # print(arr[i])
        ans += arr[i].count('H')
    print(f'#{tc} {ans}')