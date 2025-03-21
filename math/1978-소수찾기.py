# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.



count = int(input())
nums = list(map(int, input().split()))

def is_prime(nums):
    prime_list_len = 0
    
    for n in nums:
        if n != 1:
            is_prime = True
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_list_len += 1

    print(prime_list_len)

is_prime(nums)