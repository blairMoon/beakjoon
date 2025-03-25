# 문제
# 상근이는 나무 M미터가 필요하다. 근처에 나무를 구입할 곳이 모두 망해버렸기 때문에, 정부에 벌목 허가를 요청했다. 정부는 상근이네 집 근처의 나무 한 줄에 대한 벌목 허가를 내주었고, 상근이는 새로 구입한 목재절단기를 이용해서 나무를 구할것이다.

# 목재절단기는 다음과 같이 동작한다. 먼저, 상근이는 절단기에 높이 H를 지정해야 한다. 높이를 지정하면 톱날이 땅으로부터 H미터 위로 올라간다. 그 다음, 한 줄에 연속해있는 나무를 모두 절단해버린다. 따라서, 높이가 H보다 큰 나무는 H 위의 부분이 잘릴 것이고, 낮은 나무는 잘리지 않을 것이다. 예를 들어, 한 줄에 연속해있는 나무의 높이가 20, 15, 10, 17이라고 하자. 상근이가 높이를 15로 지정했다면, 나무를 자른 뒤의 높이는 15, 15, 10, 15가 될 것이고, 상근이는 길이가 5인 나무와 2인 나무를 들고 집에 갈 것이다. (총 7미터를 집에 들고 간다) 절단기에 설정할 수 있는 높이는 양의 정수 또는 0이다.

# 상근이는 환경에 매우 관심이 많기 때문에, 나무를 필요한 만큼만 집으로 가져가려고 한다. 이때, 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M이 주어진다. (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)

# 둘째 줄에는 나무의 높이가 주어진다. 나무의 높이의 합은 항상 M보다 크거나 같기 때문에, 상근이는 집에 필요한 나무를 항상 가져갈 수 있다. 높이는 1,000,000,000보다 작거나 같은 양의 정수 또는 0이다.

# 출력
# 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.



# 1. 나무개수 받기 (N), 필요 나무 길이 받기 (tree_sum)
# 2. 나무 길이 받기 (trees)
# 3. 순서대로 정렬하기 
# 4. while문 돌리기 (범위: tree_sum <= 나머지 )
# 5. for문 돌리면서 tree_remainder 더하기 
# 6. 만약에 tree_remainder가 작으면 -1을 하고 크면 + 1을 하고 다시 돌리기 




# def cut_trees(N,trees_sum):
#   trees = sorted(map(int,input().split()))
#   middle_tree = (trees[0] + trees[-1])//2
  
#   middle_tree_max = 0
  
#   while middle_tree < trees[-1]: 
#     tree_remainder_sum = 0
#     for tree in range(N - 1, -1, -1): 
#       if trees[tree] // middle_tree > 0: # 큰 수부터 하는게 맞지
#         tree_remainder_sum += trees[tree] % middle_tree # 다 더해보자 
#       # tree_remainder_sum += trees[tree] - middle_tree => 이게 더 정확한 코드 사실 몫과 나누기가 있는게 아니라 결국 그냥 뺴는 코드임 한번만 자르니까!

#       else: # 몫이 0이면 break 해서 시간 단축 
#         break 
#     if tree_remainder_sum >= trees_sum:  # 만약에 지금 다 더한게 그 상근이가 원하는 sum보다 크거나 같으면
#       if middle_tree > middle_tree_max: # 그리고 여태까지 넣어둔 middle_tree_max보다 크다면!!
#         middle_tree_max = middle_tree # middle_tree_max 바꿔줘
#       middle_tree += 1 # 그리고 더큰게 있을 지도 모르잖아 + 1 해봐 
#     else: 
#         if not middle_tree_max == 0 and middle_tree_max > tree_remainder_sum: # 만약에 일단 처음 0이 아니고 middle_tree_max가 큰게 존재하면
#           # 앞으로 1을 더해도 작은 수밖에 안나올거임 그니까 return해줘 이게 제일 큰수야 
#           return middle_tree_max 
#         middle_tree -= 1 # 그게 아니면 -1을 해주고 다시해야징 상근이 나무 못가져가면 안되잖어 
#   return middle_tree_max  # 만약 어쩔수 없이 중간에 return안되고 마지막 수까지 돌렸다면 그게 답인가보지 그거 return해 길이가 1인거 베고 싶었을 수도 잇지 
  



# # 위의 거를 이진탐색으로 풀면?
# def cut_trees_binary_search(N, trees_sum, trees):
#   start = 0
  
#   end = max(trees)
#   max_trees_sum = 0
#   while start <= end:
#     tree_remainder_sum = 0
#     mid = (start + end) // 2 
#     for tree in trees:
#       if tree > mid:
#         tree_remainder_sum += tree - mid 
#     #tree_remainder_sum = sum((tree - mid) for tree in trees if tree > mid) 위 코드를 이렇게 간단하게 쓸 수 있음!
#     if tree_remainder_sum >= trees_sum:
#       max_trees_sum = mid
#       start = mid + 1
#     else:
#       end = mid - 1
#   return max_trees_sum












# N, trees_sum = map(int,input().split())
# trees = sorted(map(int,input().split())) # input을 함수 안에서 받으면 재사용성이 떨어진대 ! 모두 받아서 하나로 합치는거면 밖에서 받도록!
# # print(cut_trees(N,trees_sum))
# print(cut_trees_binary_search(N,trees_sum))

tree_counter = {}
for height in map(int, input().split()):
    if height in tree_counter:
        tree_counter[height] += 1
    else:
        tree_counter[height] = 1
        
print(tree_counter)