# # 요세푸스 문제는 다음과 같다.

# # 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고,
# # 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다.
# # 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 
# # 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다.
# # 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 
# # 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.


# # N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

# # 나의 생각 
# # 노드와 링크드 리스트를 클래스로 먼저 구현하기 o
# # 인덱스 찾는 메서드 구현하기 o
# # N만큼 노드 append하기 
# # 마지막 노드와 첫번째 head 연결 짓기 
# # 인덱스 메서드로 제거하고 제거된 노드를 배열에 넣기 
# # 노드가 사라질 때까지 제거를 반복하기 (함수에서 구현)


# class Node: 
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Linked_list:
#     def __init__(self,value):
#         self.head = Node(value)
#     def print_all(self):
#         cur = self.head
#         while cur is not None: # 이거는 마지막 노드까지 순회하는 것
#             print(cur.data)
#             cur = cur.next
#     # def append_node(self,value):
#     #     cur = self.head
#     #     while cur.next is not None:
#     #         cur = cur.next
#     #     cur.next = Node(value)
#     #     if cur.next == None:
#     #         cur.next = self.head
#     def append_node(self,value):
        
#         cur = self.head
        
#         while cur.next != self.head: # 여기 원형 리스트의 조건이야 즉 next 노드가 첫 노드가 아니라면 옮겨라 이건데 마지막 노드를 찾아가는거지 
#             cur = cur.next
#         cur.next = Node(value)
#         if cur.next == None:
#             cur.next = self.head
#         # cur.next.next = self.head => 이렇게 원형을 연결시킬 수도 있어 이게 더 괜찮은 방법이야 
#         # 왜냐면 나중에 노드가 추가되거나 이러면 꼬일 수 있기 때문에 내가 위에 쓴 코드는 딱 정해진 노드에서 
#         # 마지막으로 실행될때만 가능한 코드거든! 
    
#     def find_index(self, index):
#         cur = self.head
#         for _ in range(1, index):
#             if cur is None:  # 리스트 길이를 초과한 경우 처리
#                 return None
#             cur = cur.next
#         return cur  # index번째 노드 반환

    


#     def delete_index(self, index ):
#         # index = index - 1
#         if index == -1:
#             delete_node = self.head
#             cur = self.head
#             while cur.next != self.head:  # 마지막 노드 찾기
#                 cur = cur.next
#             self.head = self.head.next  # head를 다음 노드로 변경
#             cur.next = self.head  # 원형 구조 유지
            
#         cur = self.head
#         print('cur.next.data',cur.next.data)
#         # print(index)
#         prev_node = self.find_index(index - 1)
#         print('prev_node',prev_node.data)
#         delete_node = prev_node.next
#         print('delete_node',delete_node.data)
#         # print('prev_node.next',prev_node.next.data)
#         prev_node.next = delete_node.next  # 노드 삭제
#         self.head = prev_node.next
#         print('prev_node.next',prev_node.next.data)
#         # self.head.next = 
#         # print('self.head.next.data',self.head.next.data)
#         print('self.head.data',self.head.data)

#         print("---------------------------------")
#         # cur.next = self.head  # 원형 구조 유지        
#         # return delete_node
    




# def josephus_problem(n, k):
#     # Linked_list(1)
#     # print(Linked_list.head)
#     linked_list_1 = Linked_list(1)
#     cur = linked_list_1.head
#     delete_node = []
    
#     for i in range(0, n+1) :
#         if i == 0 or i == 1:
#             continue
#         linked_list_1.append_node(i)
#         cur = cur.next
    
#     for _ in range(2):
        
#         linked_list_1.delete_index(k)

#     # print(delete_node)    
#     linked_list_1.print_all()



# # n, k = map(int, input().split())
# josephus_problem(7, 3)



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # 노드 추가
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # 리스트가 비어 있는 경우
            self.head = new_node
            self.head.next = self.head  # 굳이 리스트가 비어있을 때도 일관성을 위해서.. 원형 연결
        else:
            cur = self.head
            while cur.next != self.head:  # 마지막 노드 찾기
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head  # 새 노드의 next를 head로 연결

    # 노드 삭제
    def delete(self, prev, cur):
        if cur == self.head:  # 삭제 대상이 head인 경우
            if cur.next == self.head:  # 노드가 하나만 남은 경우
                self.head = None
            else:
                self.head = cur.next
        prev.next = cur.next  # 이전 노드의 next를 현재 노드의 next로 연결

    # 리스트 출력
    def print_all(self):
        result = []
        if not self.head:
            return result
        cur = self.head
        while True:
            result.append(cur.data)
            cur = cur.next
            if cur == self.head:  # 한 바퀴 돌았으면 종료
                break
        return result


def josephus_problem(n, k):
    # 원형 연결 리스트 생성
    circle = CircularLinkedList()
    for i in range(1, n + 1):
        circle.append(i)

    result = []
    cur = circle.head
    prev = None

    while circle.head:  # 리스트가 비어 있지 않을 때까지 반복
        # K-1번 이동
        for _ in range(k - 1):
            prev = cur
            cur = cur.next
            # 이 코드를 생각해 내는게 쉽지 않았을 거 같다 ㅠ 
            # 생각의 알고리즘 : 일단 인덱스로 접근하는 것이 쉽지 않으니까 하나씩 이동시켜보자! 
            # 3번째까지 도달하려면 두번 움직여야하네, 그리고 링크드리스트는 짝궁이서 움직여야하니까 prev랑 cur 둘다 옮겨주자 
            
        # K번째 사람 제거
        result.append(cur.data)  # 결과 리스트에 추가
        circle.delete(prev, cur)  # 삭제
        cur = prev.next  # 다음 노드로 이동

    return result

print(josephus_problem(7, 3))
