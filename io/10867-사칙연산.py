# 문제
# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 

# 입력
# 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)

# 출력
# 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.



num1, num2 = map(int, input().split())
# 더하기
def plus(num1,num2):
    result = num1 + num2
    return result
# 뺴기
def subtract(num1,num2):
    result = num1 - num2
    return result
# 곱하기
def multiply(num1,num2):
    result = num1 * num2
    return result

# 나누기
def divide(num1,num2):
    result = num1 // num2
    return result

# 나머지 
def mod(num1,num2):
    result = num1 % num2
    return result


# 조인함수 
result = "\n".join([
    str(plus(num1, num2)),
    str(subtract(num1, num2)),
    str(multiply(num1, num2)),
    str(divide(num1, num2)),
    str(mod(num1, num2))
])
print(result)