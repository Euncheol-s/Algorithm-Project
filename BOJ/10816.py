# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다.
# 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

N = int(input())                # 상근이가 가지고 있는 카드의 개수
input_arr = input()             # 상근이가 갖고 있는 카드의 숫자 문자열을 저장
card_arr = input_arr.split()    # 상근이가 갖고 있는 카드의 숫자 배열(datatype = string)
M = int(input())                # 주어진 정수의 개수
input_arr = input()             # 주어진 정수의 숫자 문자열
num_arr = input_arr.split()     # 주어진 정수의 배열(datatype = string)
output_arr = [0 for i in range(M)] # 주어진 숫자가 상근이가 갖고 있는 카드에서 각각 몇개가 있는지 저장할 배열(M의 개수와 같은 길이를 가지고 0으로 초기화)

for i in range(N):
    n = int(card_arr[i])
    for j in range(M):
        m = int(num_arr[j])
        if n == m:
            output_arr[j] += 1

print(output_arr)