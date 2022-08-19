# N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

freq_zero_one = [0, 0]

def fibo(num):
    if num == 0:
        freq_zero_one[0] += 1
        return 0
    elif num == 1:
        freq_zero_one[1] += 1
        return 1
    else:
        return fibo(num - 1) + fibo(num - 2)

N = int(input())
result_arr = []

for i in range(N):
    M = int(input())
    fibo(M)
    result_arr.append(freq_zero_one)
    freq_zero_one = [0, 0]

for i in result_arr:
    for j in i:
        print(j, end=" ")
    print()