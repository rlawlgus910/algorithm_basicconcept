import sys
sys.stdin = open('정곤이의단조증가하는수_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_num = -1
    for i in range(N - 1):
        for i2 in range(i + 1, N):

            num = str(arr[i] * arr[i2])

            flag = 1
            for j in range(len(num) - 1):
                if int(num[j]) > int(num[j + 1]):
                    flag = 0
                    break

            if flag == 1:
                num = int(num)

                if num > max_num:
                    max_num = num


    print(f'#{tc} {max_num}')