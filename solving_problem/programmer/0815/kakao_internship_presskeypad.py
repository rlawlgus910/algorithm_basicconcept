def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12
    l_diff = 0
    r_diff = 0
    for num in numbers:  # 입력 받은 숫자 하나씩 비교하기
        # 입력 받은 숫자가 0인 경우 11로 바꾸기
        if num == 0:
            num = 11
        # 입력 받은 숫자가 1,4,7인 경우
        if num % 3 == 1:
            answer += 'L'  # 출력에 'L'추가
            left = num  # 왼손 위치 저장
        # 입력 받은 숫자가 3, 6, 9인 경우
        elif num % 3 == 0:
            answer += 'R'  # 출력에 'R'추가
            right = num  # 오른손 위치 저장
        # 입력 받은 숫자가 가운데열일 경우
        else:
            # 왼손과 입력값의 거리
            if left % 3 == 2:  # 왼손이 가운데에 있을 경우
                l_diff = abs((num // 3) - (left // 3))
            elif left % 3 == 1:  # 왼손이 1번째 열일 경우
                l_diff = abs((num // 3) - (left // 3)) + 1
            # 오른손과 입력값의 거리
            if right % 3 == 2:  # 오른손이 가운데에 있을 경우
                r_diff = abs((num // 3) - (right // 3))
            elif right % 3 == 0:  # 오른손이 3번째 열일 경우
                r_diff = abs((num // 3 + 1) - (right // 3)) + 1
            # 더 가까운 거리 구하기
            if l_diff < r_diff:  # 왼쪽이 더 가까운 경우
                answer += 'L'
                left = num
            elif l_diff > r_diff:  # 오른쪽이 더 가까운 경우
                answer += 'R'
                right = num
            else:  # 거리가 같은 경우
                if hand == 'right':  # 오른손잡이인 경우
                    answer += 'R'
                    right = num
                else:  # 왼손잡이인 경우
                    answer += 'L'
                    left = num

    return answer