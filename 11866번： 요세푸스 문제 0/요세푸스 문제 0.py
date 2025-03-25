#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11866                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: catherine621 <boj.kr/u/catherine621>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11866                          #+#        #+#      #+#     #
#    Solved: 2025/03/25 10:58:00 by catherine621  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #



N, K = map(int(input()).split())

def Josephus(N,K):
  is_vaild = True
  result = []
  start = 1
  while len(result) < N:
    if start < N:
      result.append(start + K)   