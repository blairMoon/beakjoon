# # 요세푸스 문제는 다음과 같다.

# # 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고,
# # 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다.
# # 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 
# # 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다.
# # 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 
# # 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.


# # N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.


# 생각 
# 1. n만큼 리스트 만들기 
# 2. k번째 사람 pop하기 
# 3. 


def josephus_problem(n, k):
    circle = []
    
    for i in range(1, n + 1):
        circle.append(i)
    
    index = 0
    return_num = []
    while circle:
        index = (index + (k - 1)) % len(circle)
                # 이동거리              # 순환구조 연결
        return_num.append(circle.pop(index))
    
    return f"<{', '.join(map(str, return_num))}>"
    



n, k = map(int, input().split())
print(josephus_problem(n,k))