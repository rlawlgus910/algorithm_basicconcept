import sys
sys.stdin = open('Magnetic_input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for j in range(100):
        stack = [0]
        for i in range(100):
            if arr[i][j] == 1 and (stack[-1] == 0 or stack[-1] == 2):
                stack.append(1)
            elif arr[i][j] == 2 and stack[-1] == 1:
                stack.append(2)

        ans += (len(stack) - 1) // 2

    print(f'#{tc} {ans}')
