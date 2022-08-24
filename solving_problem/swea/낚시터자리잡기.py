import sys
sys.stdin = open('낚시터자리잡기_input.txt')

def bfs(visited, v, g):    # v: 탐색시작점
    queue = []
    queue.append(v)
    while queue:
        idx = queue.pop()
        if visited[idx] == 0:
            visited[idx] =

    

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    visited = [0] * (N + 1)

    di1 = [0, 1, -1]
    di2 = [0, -1, 1]

    gates = []
    members = []
    for _ in range(3):
        g, m = map(int, input().split())
        gates.append(g)
        members.append(m)


