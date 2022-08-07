# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

N = int(input("개수를 입력하세요"))
N_nums = input("수를 입력하세요").split()

while len(N_nums) != N:
    print("개수를 정확히 입력하세요")
    N = int(input("개수를 입력하세요"))
    N_nums = input("수를 입력하세요").split()

M = int(input("개수를 입력하세요"))
M_nums = input("수를 입력하세요").split()

while len(M_nums) != M:
    print("개수를 정확히 입력하세요")
    M = int(input("개수를 입력하세요"))
    M_nums = input("수를 입력하세요").split()

result = []

for i in M_nums:
    if i in N_nums:
        result.append(1)
    else:
        result.append(0)

print(result)