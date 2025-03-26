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



N, K = map(int, input().split())

def Josephus(N, K):
    people = list(range(1, N+1)) 
    result = []
    index = 0

    while people:
        index = (index + K - 1) % len(people)
        result.append(people.pop(index))

    return result