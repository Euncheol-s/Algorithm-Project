# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

N = int(input())                      # 수열 A의 길이
input_arr = input()                   # 수열 A를 이루는 수의 문자열
sequence_element = input_arr.split()  # 가장 긴 증가하는 부분 수열의 원소의 문자열
result_sequence = []                  # 가장 긴 증가하는 부분 수열의 원소를 저장할 배열

for i in range(N):
    if i == 0:
        result_sequence.append(int(sequence_element[i]))
    else:
        n = result_sequence.pop()
        m = int(sequence_element[i])
        if n < m:
            result_sequence.append(n)
            result_sequence.append(m)
        else:
            result_sequence.append(n)

print(result_sequence)
print(len(result_sequence))
