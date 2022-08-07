# 땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.
#달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.
#달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

(A, B, V) = map(int, input().split())

def snail_climbing_iter():
    present_height = 0  # 현재 높이
    isDay = True        # 낮 여부
    days = 1            # 일수

    # 목표 높이에 도달할 때 까지 반복
    while present_height < V:
        if(isDay):
            present_height += A
            isDay = False
        else:
            present_height -= B
            isDay = True
            days += 1
    print(days)

snail_climbing_iter()
