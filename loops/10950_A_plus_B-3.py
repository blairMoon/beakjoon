# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.

# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 출력
# 각 테스트 케이스마다 A+B를 출력한다.

# test_case = int(input())


# for i in range(test_case):
#     num1 , num2 = map(int, input().split())
#     print(num1 + num2)

test_case = int(input())
results = []  

for _ in range(test_case):
    num1, num2 = map(int, input().split())
    results.append(num1 + num2)  


print("\n".join(map(str, results)))