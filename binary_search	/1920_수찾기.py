#문제
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
# 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 
# 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

# 출력
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.



N = int(input())
N_list = sorted(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split())) 


def find_num(N_list , M_list):
  result = []
  for i in M_list:
    if i < N_list[0] or i > N_list[-1]:
        result.append(0)   # 아예 범위 밖이면 빠르게 0 처리
        continue # 밑코드 실행 X
    start = 0
    end = len(N_list) - 1
    
    
    while start <= end:
      mid = (start + end) // 2
      if N_list[mid] == i:
        result.append(1)
        break
      elif N_list[mid] < i:
        start = mid + 1
      else:
        end = mid - 1
    else:
      result.append(0)
  return result
      


result = find_num(N_list , M_list)
print(*result, sep='\n')


