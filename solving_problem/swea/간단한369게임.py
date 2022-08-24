N = int(input())

for i in range(1, N + 1):
    num = str(i)

    flag = 0
    len_num = len(num)
    for j in range(len_num):
        if num[j] == '3' or num[j] == '6' or num[j] == '9':
            flag += 1

    if flag > 0:
        print('-' * flag, end=' ')

    else:
        print(int(num), end=' ')
