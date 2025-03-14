# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.



total = 0

n = input()
# 숫자는 리스트로 바로 변환활 수 없음 
number = input()
number_list  = list(number)
for i in number:
    total += int(i)

print(total)    
n = input()
nums = input()
total = 0
for i in nums :
    total += int(i)  # total= total+int(i)
print(total)
num = input()
numbers = list(map(int,input()))

print(sum(numbers))