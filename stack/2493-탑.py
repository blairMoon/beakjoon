# 문제
# KOI 통신연구소는 레이저를 이용한 새로운 비밀 통신 시스템 개발을 위한 실험을 하고 있다.
# 실험을 위하여 일직선 위에 N개의 높이가 서로 다른 탑을 수평 직선의 왼쪽부터 오른쪽 방향으로 차례로 세우고,
#  각 탑의 꼭대기에 레이저 송신기를 설치하였다. 모든 탑의 레이저 송신기는 레이저 신호를 지표면과 평행하게 수평 직선의 왼쪽 방향으로 발사하고, 
# 탑의 기둥 모두에는 레이저 신호를 수신하는 장치가 설치되어 있다. 하나의 탑에서 발사된 레이저 신호는 가장 먼저 만나는 단 하나의 탑에서만 수신이 가능하다.

# 예를 들어 높이가 6, 9, 5, 7, 4인 다섯 개의 탑이 수평 직선에 일렬로 서 있고, 
# 모든 탑에서는 주어진 탑 순서의 반대 방향(왼쪽 방향)으로 동시에 레이저 신호를 발사한다고 하자.
#  그러면, 높이가 4인 다섯 번째 탑에서 발사한 레이저 신호는 높이가 7인 네 번째 탑이 수신을 하고, 
# 높이가 7인 네 번째 탑의 신호는 높이가 9인 두 번째 탑이, 높이가 5인 세 번째 탑의 신호도 높이가 9인 두 번째 탑이 수신을 한다.
#  높이가 9인 두 번째 탑과 높이가 6인 첫 번째 탑이 보낸 레이저 신호는 어떤 탑에서도 수신을 하지 못한다.

# 탑들의 개수 N과 탑들의 높이가 주어질 때, 각각의 탑에서 발사한 레이저 신호를 어느 탑에서 수신하는지를 알아내는 프로그램을 작성하라.

# 입력
# 첫째 줄에 탑의 수를 나타내는 정수 N이 주어진다. N은 1 이상 500,000 이하이다. 
# 둘째 줄에는 N개의 탑들의 높이가 직선상에 놓인 순서대로 하나의 빈칸을 사이에 두고 주어진다. 탑들의 높이는 1 이상 100,000,000 이하의 정수이다.

# 출력
# 첫째 줄에 주어진 탑들의 순서대로 각각의 탑들에서 발사한 레이저 신호를 수신한 탑들의 번호를 하나의 빈칸을 사이에 두고 출력한다. 
# 만약 레이저 신호를 수신하는 탑이 존재하지 않으면 0을 출력한다.

# import sys
# input = sys.stdin.readline


# N = int(input())
# tops = list(map(int, input().split()))


# def top_stack(N):
#     result = [0] * N
#     while tops:
#         cur_top = tops.pop()
#         for i in range(len(tops) - 1, -1, -1):
#             if cur_top <= tops[i]:
#                 result[len(tops)] = i + 1
#                 break
                
#     print(' '.join(map(str,result)))


# top_stack(N)
N = int(input())
tops = list(map(int, input().split()))
stack = []         # index만 저장 # 제일 큰 탑 넣어두기 
result = [0] * N

for i in range(N):
                    # 제일 높은 탑      # 현재 탑 
    while stack and tops[stack[-1]] < tops[i]: # 만약 지금 탑이 더 크면 더 이상 스택의 탑은 필요가 없으니까 없애버려 
        stack.pop()
    # 조건이 중요한 이유: 한번만 하는게 아니라 현재 탑보다 제일 높은 탑이 작을 때까지! 
    # 아니야 이거 한번 도는게 아니라 나보다 스택의 마지막값이 클때까지 시행하는 거임 
    # 만약에 스택마지막 값이 계속 나보다 작으면 클때까지 돌아야 함



        
    if stack: # 만약 지금 현재 탑보다 큰 탑이 존재한다면
        result[i] = stack[-1] + 1 # 그게 몇번째 탑인지 넣어주면 돼. 근데 Index기준이니까 + 1 해줘  

    stack.append(i) 
    # 그리고  그 다음 탑이 현재 탑보다 작을 수도 있잖아. 
    # 그니까 일단 넣어둬. 물론 지금 탑보다 큰 탑이 stack에 이미 큰 탑이 있을 수가 있지만, 거리가 가까운게 일단 중요하니까 
    # 더 큰 값이 있어도 일단 가까운 거리에 있는 탑이 크면 그걸 쏜단 말이지 

print(*result) # 리스트에서 바로 빼주는 거!! 

# top_heights = [6, 9, 5, 7, 4]


# def get_receiver_top_orders(heights):
#     answer = [0] * len(heights)
#     while heights:
#         height = heights.pop()
#         for idx in range(len(heights) - 1, -1, -1):
#             if height <= heights[idx]:
#                 answer[len(heights)] = idx + 1
#                 break
#     return answer


# print(get_receiver_top_orders(top_heights))

# def get_receiver_top_orders(heights):
#     answer = [0] * len(heights)
#     while heights:
#         height = heights.pop()
#         for idx in range(len(heights) - 1, -1, -1):
#             if height <= heights[idx]:
#                 answer[len(heights)] = idx + 1
#                 break
#     return answer


# # 사용자 입력
# N = int(input())
# top_heights = list(map(int, input().split()))

# # 함수 호출 및 출력
# result = get_receiver_top_orders(top_heights)
# print(' '.join(map(str, result)))




N = int(input())
tops = list(map(int, input().split()))
stack = []         # index만 저장
result = [0] * N

for i in range(N):
    while stack and tops[stack[-1]] < tops[i]: # stack (최댓값이 있고, 그 최댓값이 현재 탑보다 작으면 pop)
        stack.pop()
    
    if stack: # 최댓값이 있으면 그 result에 해당 번호 넣어줘 
        result[i] = stack[-1] + 1  # 인덱스니까 +1

    stack.append(i) #최댓값이 있어도  일단 넣어봐야지 그 전 게 작을 수도 있잖아 

print(*result)