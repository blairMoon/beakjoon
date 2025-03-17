
# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.



import sys
input = sys.stdin.readline

N = int(input())
def sort3(N):
    count_list= [0] * 10001 # 인덱스 1~10000까지
    for i in range(N):
        num  = int(input())
        count_list[num] += 1
    for i in range(1, 10001):
        if count_list[i] > 0:
            for _ in range(count_list[i]):
                print(i)

sort3(N)

# 생각회로 

#  경우의 수가 좀 더 커짐 => 어떻게 하면 줄일 수 있을까? 
# 중복되는 수를 돌리는 걸 최소화 해야겠다 ! 
# 어떻게 최소화할 수 있지? 반복되는 수를 count해야겠다!! 
# set...? dictionary...? => key 찾는데 복잡도가 올라갈거 같다! 
# 리스트를 만들어서 count를 넣어줘야지 10000까지니까 리스트도 index 10000자리까지 만들어야지 
# 이제 index를 이용해서 출력해주면 끝! 