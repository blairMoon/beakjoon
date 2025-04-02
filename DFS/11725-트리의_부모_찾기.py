# 문제
# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

# 출력
# 첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.            




from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
N = int(input())  # 노드 개수
edges = [] 
# 2. edges 리스트 만들기 (N - 100 입력 받기) => 인접리스트를 써야겠다! 
for _ in range(N - 1):
    a, b = map(int, input().split())
    edges.append((a, b))  # 튜플 형태로 저장!

# 3. 인접리스트 만들기 # 일반 딕셔너리 사용 
# graph = {}
# for a, b in edges: 
#     if a not in graph:
#         graph[a] = [] # 이렇게 빈 리스트로 만들어 줘야 하는데 (라이브러리에서는 이걸 생략할 수 있음)
#     if b not in graph:
#         graph[b] = []
#     graph[a].append(b)  # a → b
#     graph[b].append(a)  # b → a 

# 3. 인접 리스트 만들기 # 라이브러리 사용
graph = defaultdict(list) # 선언
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)  # 무방향이니까 양쪽 다 넣기!
# 키가 없으면 자동으로 빈 리스트로 초기화됨!! 


# 무조건 defaultdict(list) 쓰는 걸 추천해!
# 특히 그래프 문제에서는 정말 코드가 깔끔해지고,
# 예외처리 안 해도 돼서 안정적이야!



parent = [0] * (N + 1) # 미리 넣어두는 이유: parent[3] = 1 이런식으로 바로 저장하고 싶은데 존재하지 않으면 이렇게 쓸 수 없으니 미리 0으로 초기화 해둠 

visited = [False] * (N + 1) # 노드 번호를 index번호로 바로 사용하려고 미리 넣어둠 

def dfs(node):
    visited[node] = True
    for neighbor in graph[node]: # 현재 노드의 인접한 친구들 돌기
        if not visited[neighbor]: # 만약에 방문한 적이 없는 노드면 지금 노드가 부모가 됨!
            # 깊이 탐색이 잖아 처음에서 깊게 내려가는거니까 당연히 데려온 사람이 부모일 수 밖에 없음 . 
            parent[neighbor] = node  # 부모 저장!
            dfs(neighbor)

dfs(1)  # 루트는 1이 됨

# 부모 노드 출력 (2번부터)
for i in range(2, N + 1):
    print(parent[i])