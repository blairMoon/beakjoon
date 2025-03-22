# 문제
# 정수를 저장하는 스택을 구현한 다음,
#  입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 다섯 가지이다.

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다.
#  만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 
# 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# 입력
# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다.
#  둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# 출력
# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.


# 1. push
# 2. pop
# 3. size
# 4. empty (1 ,0)
# 5. top (만약 없는 경우 -1)




class Stack():
    def __init__(self):
        self.stack = []
        
    
    def push(self, num):
        self.stack.append(num)

    def pop(self):
        if self.empty():
            return -1
        else:
            return self.stack.pop()
    
    def size(self):
        count = 0
        for i in self.stack:
            if type(i) == int:
                count += 1
        return count

    def empty(self):
        if len(self.stack) == 0:
            return 1
        else: 
            return 0

    def top(self):
        if self.empty() == 1:
            return -1
        else:
            return self.stack[-1]

def run_stack():
    N = int(input())
    fuc_p = [list(map(str, input().split())) for i in range(N) ]
    # 이렇게 굳이 리스트로 안만들고 split만 한 뒤 문자열도 인덱스가 가능하니까 
    # for문 안에서 가능 
    stack = Stack()
    for i in fuc_p:
        if i[0] == 'push':
            stack.push(int(i[1]))
        elif i[0] == 'pop':
            print(stack.pop())
        elif i[0] == 'size':
            print(stack.size())
        elif i[0] == 'empty':
            print(stack.empty())
        elif i[0] == 'top':
            print(stack.top())

    # 키가 겹치면 안되기 때문에 딕셔너리는 실패!
    # dic = {}
    # for i in range(N):
    #     fuc_p = list(map(str,input().split()))
    #     if len(fuc_p) == 1:
    #         dic[fuc_p[0]] = None
    #     else:
    #         dic[fuc_p[0]] = fuc_p[1]
    # print(dic)    
    
run_stack()