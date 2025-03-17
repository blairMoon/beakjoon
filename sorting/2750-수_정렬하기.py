# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# N = int(input())

# def sort(N):
#     num_list = [int(input()) for i in range(N)]
#     for i in range(N - 1 ):
#         change_num = 0
#         for j in range(N - 1):
#             if num_list[j+1] < num_list[j]:
#                 change_num = num_list[j + 1]
#                 num_list[j + 1] = num_list[j]
#                 num_list[j] = change_num
#     return '\n'.join(map(str,num_list))

# print(sort(N))

# 리팩토링 코드 
def bubble_sort(arr):
    N = len(arr)
    for i in range(N - 1):
        for j in range(N - 1 - i):
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap
    return '\n'.join(map(str, arr))


N = int(input())
num_list = [int(input()) for _ in range(N)]
print(bubble_sort(num_list))


# 흐름 설명 : 어떻게 생각했는가? 
# 1. 먼저 버블 정렬을 생각했다. index를 기준으로 앞 뒤를 비교해서 큰 숫자를 뒤로 보내야지! 
# 2. 근데 생각해보니까 for문을 한번만 쓰면 첫번째 index만 결국 대소비교가 되겠네 
# 3. 모든 list에 있는 값들을 대소비교를 해줘야 겠네 
# 4. 그럼 for문을 2번 돌려야겟네 그럼 범위는 어떻게 잡지?? => 이게 제일 중요 
# 5. 일단 첫 for문 범위는 N - 1 (마지막 Index 전까지!!) 어차피 0~ 마지막 바로 전까지 돌면 이미 정렬되어 있을 테니까 index + 1까지 정렬되잖아 
# 6. 그럼 두번째 for문 범위는 N - 1 - i인데 이거는 왜그런거냐면 버블 정렬할때 가장 큰 수는 맨 뒤로 보냈잖아 그래서 마지막부터 범위를 한개씩 좁히는거야 
# i	내부 루프    range	   비교되는 인덱스	의미
# 0	range(4)	0~3	       전체 비교
# 1	range(3)	0~2	     마지막 인덱스는 제외
# 2	range(2)	0~1	      뒤에 2개 제외
# 3	range(1)	0          뒤에 3개 제외
# 이렇게 생각하면 될 거 같어 
# 그 이후는 파이썬 문법을 사용해서 if문 써서 index랑 Index + 1이랑 비교해서 Index + 1이 더 작으면 자리 바꿔주면 돼. 그걸 계속 반복하는거고 
# - i를 하면 점점 마지막 끝자리 수는 내비두겠지 
