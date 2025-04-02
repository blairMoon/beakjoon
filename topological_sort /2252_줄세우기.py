# 문제
# N명의 학생들을 키 순서대로 줄을 세우려고 한다. 각 학생의 키를 직접 재서 정렬하면 간단하겠지만,
# 마땅한 방법이 없어서 두 학생의 키를 비교하는 방법을 사용하기로 하였다. 
# 그나마도 모든 학생들을 다 비교해 본 것이 아니고, 일부 학생들의 키만을 비교해 보았다.

# 일부 학생들의 키를 비교한 결과가 주어졌을 때, 줄을 세우는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 32,000), M(1 ≤ M ≤ 100,000)이 주어진다. 
# M은 키를 비교한 횟수이다. 다음 M개의 줄에는 키를 비교한 두 학생의 번호 A, B가 주어진다. 이는 학생 A가 학생 B의 앞에 서야 한다는 의미이다.

# 학생들의 번호는 1번부터 N번이다.

# 출력
# 첫째 줄에 학생들을 앞에서부터 줄을 세운 결과를 출력한다. 답이 여러 가지인 경우에는 아무거나 출력한다.

from collections import deque




def topological_sort(n, m, edges):
  # n = 3, m = 2
  # edges = [(1, 3), (2, 3)]
  
  
    #  인접 리스트와 진입차수 배열 초기화
    graph = [[] for _ in range(n + 1)]      # 1번부터 n번까지 노드 (0은 빼고 학생 0은 없으니까 )
    # graph = [[], [], [], []] (index 0은 사용하지 않음)
    
    
    indegree = [0] * (n + 1)                # 각 노드의 진입차수
    # indegree = [0, 0, 0, 0] (초기 진입차수)

    # 간선 정보 입력 => 그래프 만들기 
    for a, b in edges:
      # 튜플 넣어준 친구들 돌기 
        graph[a].append(b)                  # a → b (a가 b보다 앞에 서야 함) 
        indegree[b] += 1                    # b의 진입차수 증가 
    # 1 → 3: graph = [[], [3], [], []], indegree = [0, 0, 0, 1]
    # 2 → 3: graph = [[], [3], [3], []], indegree = [0, 0, 0, 2]  
        
        
        
      

    #  진입차수 0인 노드를 큐에 삽입 => 줄 먼저 서야하는 친구들 준비시키기 
    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)                 # 줄 먼저 설 수 있는 애들
    # indegree = [0, 0, 0, 2]  
    # i = 1 → indegree[1] == 0 → queue = [1]
    # i = 2 → indegree[2] == 0 → queue = [1, 2]
    # i = 3 → indegree[3] == 2 → 넘어감
    
    
    
    result = []

    # 위상 정렬 => 결과값에 줄 세워주기 
    while queue:
      now = queue.popleft()    # 그냥 어느정도 방법을 정해놓기 위해서 popleft를 함         
    #  지금 줄 설 수 있는 학생 꺼냄
    # 처음: queue = [1, 2]
    # 1회차: now = 1 => queue = [2]
    # 2회차: now = 2 => queue = []
    # 3회차: now = 3

      result.append(now)                 
    # 꺼낸 학생 줄 세우기
    # 1회차: result = [1]
    # 2회차: result = [1, 2]
    # 3회차: result = [1, 2, 3]
    
    
      # 줄섰으니까 차수 하나씩 줄여주기 
      # graph = [[], [3], [3], []]
      for next_student in graph[now]: 
        # 현재 학생(now)이 앞에 서야 할 애들 찾기
        # now = 1 → graph[1] = [3] → next_student = 3
        # now = 2 → graph[2] = [3] → next_student = 3
        # now = 3 → graph[3] = [] → 반복 없음

        indegree[next_student] -= 1
        # next_student가 기다려야 할 사람 수 1 감소
        # 1회차: indegree[3] = 2 → 1
        # 2회차: indegree[3] = 1 → 0
        # 3회차: 없음

        if indegree[next_student] == 0:
          queue.append(next_student)
            # 이제 기다릴 사람 없으니까 줄 설 수 있음 → 큐에 넣음
            # 2회차: 3이 큐에 들어감 → queue = deque([3])

    return result
    
n, m = map(int, input().split()) 
# n: 학생 수  m: 조건수 
edges = [tuple(map(int, input().split())) for _ in range(m)]
# 조건 입력 받고 튜플로 넣어주기 
result = topological_sort(n, m, edges)
print(*result)