# 1. 함수린?
# 반복해서 사용할 코드를 하나의 이름으로 묶는 것
def add(a, b):
    return a + b
result = add(10, 20)

print(result)   # 30

# 구조
# def 함수이름(매개변수):
#    실행할 코드
#    return 결과

# 2. 매개변수와 반환값
def square(x):
    return x * x

print(square(5))   # 25 
print(square(10))  # 100

# 문제 1
# 두 숫자를 받아서 더 큰 숫자를 반환하는 함수 만들기
def max_number(a, b):
    return(a, b)

print(max(10, 20))  # 20

# 문제 2
# 숫자를 받아서 짝수인지 홀수인지 반환하는 함수 만들기
def check_number(a):
    if a % 2 == 0:
        print("짝수")

check_number(10)   # 짝수

# 문제 3
# 리스트의 평균을 반환하는 함수 만들기
def add(numbers):
    total = sum(numbers)
    avg = total / len(numbers)

    return avg

numbers = [80, 90, 70, 100, 60]

result = add(numbers)

print(result)   # 80.0