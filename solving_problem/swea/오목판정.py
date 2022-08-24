import sys
sys.stdin = open('오목판정_input.txt')

def check(arr):
    global ans
    # 가로
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 'o':
                cnt += 1
                if cnt == 5:
                    ans = 'YES'
                    return
            else:
                cnt = 0
    
    # 세로
    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 'o':
                cnt += 1
                if cnt == 5:
                    ans = 'YES'
                    return
            else:
                cnt = 0

    # 대각석 우측방향
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ni = i
            nj = j
            cnt = 0
            while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o' and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                cnt += 1
                if cnt == 5:
                    ans = 'YES'
                    return
                ni += 1
                nj += 1

    # 대각선 좌축 방향
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            cnt = 0
            ni = i
            nj = j
            while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o' and visited[ni][nj] == 0:
                visited[i][j] = 1
                cnt += 1
                if cnt == 5:
                    ans = 'YES'
                    return
                ni += 1
                nj -= 1



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    ans = 'NO'
    check(arr)
    print(f'#{tc} {ans}')