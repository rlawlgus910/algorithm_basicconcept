# import sys
# sys.stdin = open('자기방으로돌아가기_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    rooms = [[] for _ in range(201)]

    for i in range(N):
        a, b = map(int, input().split())
        if a % 2 == 0:
            start = a // 2
        else:
            start = a // 2 + 1

        if b % 2 == 0:
            goal = b // 2
        else:
            goal = b // 2 + 1

        if start < goal:
            for room in range(start, goal + 1):
                rooms[room].append(i)
        else:
            for room in range(goal, start + 1):
                rooms[room].append(i)

    ans = 0
    for i in range(201):
        a = len(rooms[i])
        if a > ans:
            ans = a

    print(f'#{tc} {ans}')