# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
import math

(M, N) = map(int, input().split())

def cal_factor(n, m):
    numbers = []
    prime_number = [2, 3, 5, 7]
    for i in range(n, m+1):
        numbers.append(i)
    for i in prime_number:
        for j in range(2, math.floor(m/2)+1):
            try:
                numbers.remove(i*j)
            except:
                pass
            if i*j > m:
                break

    print(numbers)

while (M < 1 or M > 10000 or N < M or N > 10000):
    print("1부터 10000만까지의 숫자 중 작은 수부터 입력해주세요")
    (M, N) = map(int, input().split())

cal_factor(M, N)