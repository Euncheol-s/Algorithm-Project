# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
import math

numbers = []

def is_prime(num):
    if num < 2:
        return False
    i = 2
    while i*i <= num:
        if(num % i == 0):
            return False
        i += 1
    return True

def cal_factor(n, m):
    for i in range(n, m+1):
        if (is_prime(i)):
            numbers.append(i)

(M, N) = map(int, input().split())
while (M < 1 or M > 10000 or N < M or N > 10000):
    print("1부터 10000만까지의 숫자 중 작은 수부터 입력해주세요")
    (M, N) = map(int, input().split())

cal_factor(M, N)
print(numbers)