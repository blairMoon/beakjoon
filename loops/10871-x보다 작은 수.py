# 문제
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)

# 둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.

# 출력
# X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.

# for i in sequence:
#     if i >= X:
#         sequence.remove(i)
# 이렇게 쓰면 조건문 돌면서 리스트 요소가 삭제되는데 sequence에서는 원래 있던 리스트의 index 순서대로 돌기 때문에 다음 인덱스로 넘어감   

N, X = map(int, input().split())
nums = input().split()[:N]  # 앞에서 N개만 잘라서 받기

sequence = list(map(int, nums))

filtered_sequence = [ i for i in sequence if i < X]


print(" ".join(map(str,filtered_sequence)))