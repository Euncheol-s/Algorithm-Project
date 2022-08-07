# 스위치 켜고 끄기

"""1부터 연속적으로 번호가 붙어있는 스위치들이 있다. 스위치는 켜져 있거나 꺼져있는 상태이다.
<그림 1>에 스위치 8개의 상태가 표시되어 있다. ‘1’은 스위치가 켜져 있음을, ‘0’은 꺼져 있음을 나타낸다.
그리고 학생 몇 명을 뽑아서, 학생들에게 1 이상이고 스위치 개수 이하인 자연수를 하나씩 나누어주었다.
학생들은 자신의 성별과 받은 수에 따라 아래와 같은 방식으로 스위치를 조작하게 된다.
남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다. 즉, 스위치가 켜져 있으면 끄고, 꺼져 있으면 켠다. 
여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서,
그 구간에 속한 스위치의 상태를 모두 바꾼다. 이때 구간에 속한 스위치 개수는 항상 홀수가 된다.
입력으로 스위치들의 처음 상태가 주어지고, 각 학생의 성별과 받은 수가 주어진다.
학생들은 입력되는 순서대로 자기의 성별과 받은 수에 따라 스위치의 상태를 바꾸었을 때, 스위치들의 마지막 상태를 출력하는 프로그램을 작성하시오."""


number_of_switches = int(input())
status_of_switches = input().split()

while number_of_switches != len(status_of_switches):
    print("개수를 정확히 입력해주세요")
    number_of_switches = int(input())
    status_of_switches = input().split()

def change_switch(index):
    if(status_of_switches[index] == '1'):
        status_of_switches[index] = '0'
    else:
        status_of_switches[index] = '1'

number_of_students = int(input())
for i in range(number_of_students):

    (gender, card) = map(int, input().split())

    while(gender < 1 or gender > 2 or card < 1 or card > number_of_switches):
        print("다시 입력해주세요")
        (gender, card) = map(int, input().split())

    if gender == 1:
        j = 1
        while card <= number_of_switches:
            change_switch(card-1)
            j += 1
            card *= j
    else:
        limit = 0
        if card - 1 > number_of_switches - card:
            limit = number_of_switches
        else:
            limit = card - 1

        for j in range(1, limit+1):
            if status_of_switches[card-1-j] != status_of_switches[card-1+j]:
                change_switch(card-1)
                break
            else:
                change_switch(card-1-j)
                change_switch(card-1+j)
                if card-1-j == 0:
                    change_switch(card-1)

print(status_of_switches)
