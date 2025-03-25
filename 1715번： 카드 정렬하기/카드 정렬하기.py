#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1715                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: catherine621 <boj.kr/u/catherine621>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1715                           #+#        #+#      #+#     #
#    Solved: 2025/03/25 20:07:28 by catherine621  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import heapq

n = int(input())
card_list = [int(input()) for i in range(n)]

def card_sort(n, card_list):
  heapq.heapify(card_list)
  total = 0
  while len(card_list) > 1:
    first = heapq.heappop(card_list)
    second = heapq.heappop(card_list)
    plus = first + second
    total += plus
    heapq.heappush(card_list, plus)
  
  print(total)
  
card_sort(n, card_list)