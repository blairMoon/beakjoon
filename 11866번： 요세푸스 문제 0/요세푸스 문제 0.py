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
        index = (index + K - 1) % len(people) # index 먼저 구해준 뒤,
        result.append(people.pop(index)) # pop을 해야함 
        # pop이 된 상태에서 index 구하면 하나빠진 상태이기 때문에 index가 이상해짐

    return "<" + ", ".join(map(str, result)) + ">"

  
print(Josephus(N, K))