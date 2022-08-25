def check(arr):
    for i in range(N):
        ni = i
        nj = idx_list[i]
        # 대각선 방향 확인하기


def perm(n, k):
    if k == n:
        for ii in range(N):
            arr[ii][idx_list[ii]] = 1
        check(arr)

    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k + 1)
            arr[k], arr[i] = arr[i], arr[k]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    idx_list = list(range(N))
    perm(N, 0)