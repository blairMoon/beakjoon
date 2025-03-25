#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2630                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: catherine621 <boj.kr/u/catherine621>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2630                           #+#        #+#      #+#     #
#    Solved: 2025/03/25 15:54:00 by catherine621  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 0. 어떻게 저장할까...? 흠... 아무래도 한줄씩 저장하는 것이 좋을 거 같아. 
# 한줄 씩 저장하면 크기를 정해두면 직관적일텐데 ... 그건 아니겟지?
# 그럼 리스트마다 이름을 정해줘야 하는데...? 그게 쉽나 ? 그냥 한번에 받는게 맞나?
# 고민이네..
# 엔드조건은 어떻게 설정하지?
# 그리고 만약에 다 1이거나 0일 경우는 어떻게 알려주지?                      
# 1. 처음에 모두 1이거나 모두 0이거나 하면 한개만 나오니까 그거 예외처리 
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def fold_paper(x, y, n):
  total = 0
  
  # x부터 y까지 sum해본다 
  for i in range(y, y + n):
    for j in range(x, x + n):
      total += board[i][j]
      
      
      
  # 이게 end조건임!! 
  if total == n * n:
    return 1, 0 # 전체가 파랑색 색종이일때 
  elif total == 0:
    return 0, 1 # 전체가 흰색 색종이일때 
  
  else: 
    b1, w1 = fold_paper(x, y, n//2)
    b2, w2 = fold_paper(x + n//2, y, n//2)
    b3, w3 = fold_paper(x, y + n//2, n//2)
    b4, w4 = fold_paper(x + n//2, y + n//2, n//2)
    return b1 + b2 + b3 + b4, w1 + w2 + w3 + w4



blue, white = fold_paper(0, 0, n)
print(white)
print(blue)