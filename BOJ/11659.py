# Q. 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

(N, M) = map(int, input().split()) # N: 숫자의 개수, M: 합을 구할 횟수
while (N < 1 or N > 1000 or M < 1 or M > 1000):    # 조건: 1 <= N, M <= 1000
    print("1부터 1000사이의 숫자를 입력해주세요.")
    (N, M) = map(int, input().split())
nums = input().split()  # nums: N개의 숫자를 배열에 저장
result = []

for n in range(M):
    (i, j) = map(int, input().split())
    while(i < 1 or i > N or j < i or j > N):           # 조건: 1 <= i <= j <= N
        print("범위에 맞게 작은 수 부터 입력해주세요")
        (i, j) = map(int, input().split())   # 범위를 정하는 i, j를 받음
    sum_n = 0                   # 총합을 저장할 변수
    for m in range(i-1, j):   # i-1인덱스부터 j-1인덱스 까지 반복
        sum_n += int(nums[m])
    result.append(sum_n)

for n in result:
    print(n)