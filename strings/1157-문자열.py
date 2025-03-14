
# 1157번 : 단어 공부
word = input().lower()      # input 받은 후 소문자로 변경
word_list = list(set(word)) # 해당되는 알파벳을 list에 넣기 위해서 set 함수 사용해서 중복되는 알파벳 제거 
cnt = []

for i in word_list:         # i = m, i, s, p 
    count = word.count(i)   # count 함수 사용해서 해당 알파벳의 개수 넣기 
    cnt.append(count)       # cnt = [4, 4, 1, 1] / [1, 3]

if cnt.count(max(cnt)) >= 2: # cnt 함수의 가장 큰 값이 두개 이상이면 ?출력 
    print("?")
    print(max(cnt))
else:
    print(word_list[(cnt.index(max(cnt)))].upper()) 
    # word_list의 index 값이랑 cnt의 index 값이 같기 때문에 
     

