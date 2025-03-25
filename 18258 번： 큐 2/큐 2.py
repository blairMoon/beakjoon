#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 18258                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: catherine621 <boj.kr/u/catherine621>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/18258                          #+#        #+#      #+#     #
#    Solved: 2025/03/25 01:30:05 by catherine621  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
input = sys.stdin.readline
class Que():
  def __init__(self):
    self.que = deque()
  
  def push(self, num):
    self.que.append(num)
  
  def pop(self):
    if self.empty():
      return -1
    return self.que.popleft()
  
  def empty(self):
    if len(self.que) == 0:
      return 1
    else: 
      return 0
    
  def size(self):
    return len(self.que)
  
  def front(self):
    if self.que:
      return self.que[0]
    else:
      return -1
  
  def back(self):
    if self.que:
      return self.que[-1]
    else:
      return -1
  


def run_que():
    N = int(input())
    que = Que()
    
    for _ in range(N):
        cmd = input().split()
        op = cmd[0]
        
        if op == 'push':
            que.push(int(cmd[1]))
        else:
            method = getattr(que, op) 
            print(method())
            
run_que()