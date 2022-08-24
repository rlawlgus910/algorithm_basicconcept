# import sys
# sys.stdin = open('진기의최고급붕어빵_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())     # N명, M초에 붕어빵 K개

    bbangs = [0] * 11112
    bbang = 0
    for i in range(11112):
        if i % M == 0:
            bbang = (i // M) * K
        bbangs[i] += bbang

    people = list(map(int, input().split()))

    people.sort()

    ans = 'Possible'
    sold = 0
    for person in people:
        if bbangs[person] - sold >= 1:
            sold += 1

        else:
            ans = 'Impossible'
            break

    print(f'#{tc} {ans}')