#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9012                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: catherine621 <boj.kr/u/catherine621>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9012                           #+#        #+#      #+#     #
#    Solved: 2025/03/23 01:35:50 by catherine621  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
def parentheses(N):
  for i in range(N):
    stack = []
    not_p = False
    p_str = list(map(str, input()))
    
    for j in p_str:
      if j == '(':
        stack.append(j)
      elif stack and j == ')':
        stack.pop()
      elif not stack and j == ')':
        not_p = True
        break
  if stack or not_p:
    print('NO')
  else:
    print( 'YES') 




# def parentheses(N):
#   for i in range(N):
#     stack = []
#     is_valid = True
#     p_str = str(input())
#     for j in p_str:
#       if j == '(':
#         stack.append(j)
#       elif  j ==')':
#         if stack:
#           stack.pop()
#         else:
#           is_valid = False
#           break
#     if is_valid == False or stack:
#       print('NO')
#     else:
#       print( 'YES') 
      
# N = int(input())
N = int(input())
parentheses(N)


# def is_vps(s):
#     stack = []
#     for ch in s:
#         if ch == '(':
#             stack.append(ch)
#         elif ch == ')':
#             if not stack:
#                 return False
#             stack.pop()
#     return not stack  # 스택이 비어있어야 True

# N = int(input())
# for _ in range(N):
#     line = input().strip()
#     print("YES" if is_vps(line) else "NO")