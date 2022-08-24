import sys
sys.stdin = open('행렬찾기_input.txt')

T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    ans = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0 and visited[i][j] == 0:

                column = 0
                ni = i
                nj = j
                while ni < n and nj < n and arr[ni][nj] != 0:
                    visited[ni][nj] = 1
                    column += 1
                    nj += 1

                row = 0
                ni = i
                nj = j
                while ni < n and nj < n and arr[ni][nj] != 0:
                    visited[ni][nj] = 1
                    row += 1
                    ni += 1

                ans.append([row, column])

                for ai in range(i + 1, i + row):
                    for aj in range(j + 1, j + column):
                        visited[ai][aj] = 1


    for i in range(len(ans)):
        for j in range(len(ans) - 1 - i):
            if ans[j][0] * ans[j][1] > ans[j + 1][0] * ans[j + 1][1]:
                ans[j + 1], ans[j] = ans[j], ans[j + 1]
            elif ans[j][0] * ans[j][1] == ans[j + 1][0] * ans[j + 1][1]:
                if ans[j][0] > ans[j + 1][0]:
                    ans[j + 1], ans[j] = ans[j], ans[j + 1]

    print(f'#{tc}', end=' ')
    print(len(ans), end=' ')

    for i in range(len(ans)):
        for j in range(2):
            print(ans[i][j], end=' ')

    print()

