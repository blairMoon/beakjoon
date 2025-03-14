# 문제
# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

# 입력
# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.

# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 
# 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

# 출력
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다. 정답과 출력값의 절대/상대 오차는 10-3이하이면 정답이다.
import sys

test_case = int(sys.stdin.readline() )

def average(test_case):
    for i in range(test_case):
        num_score = list(map(int, sys.stdin.readline().split()))
        score_array = []
        average = 0
        total = 0
        ratio = 0
        for j in num_score[1:]:
                total += j
        average = total/ num_score[0]
        high_people= 0
        for k in num_score[1:]:
            
            if k > average:
                high_people += 1    
        ratio = high_people/num_score[0] * 100
        
        print(f"{round(ratio, 3)}%") 

average(test_case)

# test_case = int(input())

# def average(test_case):
#     for i in range(test_case):
#         num_score = list(map(int, input().split()))
#         total = sum(num_score[1:])
#         average = total / num_score[0]
#         high_people = 0
#         for score in num_score[1:]:
#             if score > average:
#                 high_people += 1
        
#         ratio = high_people / num_score[0] * 100

        
#         print(f"{round(ratio, 3)}%") 

# average(test_case)
# => 리팩토링한 함수 