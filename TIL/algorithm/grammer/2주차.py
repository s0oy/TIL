## 1. 기본값 인자(Default Arguments)
def greet(name, greeting="안녕"):
    return f"{greeting}, {name}님!"

greet("철수")                 # "안녕, 철수님!"  ← 기본값 사용
greet("철수", "반가워")        # "반가워, 철수님!" ← 기본값 덮어씀
greet(name="철수", greeting="어서와")  # 키워드로 명시해서 호출

# 규칙: 기본값 없는 파라미터가 항상 앞에 와야 함
def f(a, b, c=10):   # OK
    pass

# def f(a, b=10, c):  ← 에러! 기본값 있는 인자 뒤에 기본값 없는 인자 못 옴

# 1-1. 함정 : 기본값으로 리스트/딕셔너리(mutable) 쓰지 말기
# 잘못된 예
def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2]  ← 기대와 다르게 이전 값이 남아있음!

# 기본값은 함수 정의 시 딱 1번만 만들어지고 계속 재사용되기 때문
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list


## 2. *args - 개수 정해지지 않은 위치 인자
def add_all(*args):
    print(args)        # 튜플로 받아짐: (1, 2, 3)
    return sum(args)

add_all(1, 2, 3)       # 6
add_all(1, 2, 3, 4, 5) # 15

# 일반 인자와 같이 쓸 수 있음 (일반 인자가 먼저)
def introduce(name, *hobbies):
    print(f"{name}의 취미: {hobbies}")

introduce("철수", "축구", "게임", "독서")
# 철수의 취미: ('축구', '게임', '독서')


## 3. **kwargs - 개수 정해지지 않은 키워드 인자
def print_profile(**kwargs):
    print(kwargs)   # 딕셔너리로 받아짐
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_profile(name="철수", age=25, city="서울")
# {'name': '철수', 'age': 25, 'city': '서울'}
# name: 철수
# age: 25
# city: 서울

# 3-1. 순서 규칙 (매우 중요)
# 함수 정의 시 파라미터 순서는 반드시 아래 순서를 지켜야 함
def func(일반인자, 기본값인자=값, *args, **kwargs):
    pass

# 예시
def order(item, qty=1, *extra_items, **options):
    print(item, qty, extra_items, options)

order("피자", 2, "콜라", "감자튀김", 매운맛=True)
# 피자 2 ('콜라', '감자튀김') {'매운맛': True}

# 3-2. 함수 호출 시 */**로 풀어서 넣기 (unpacking)
def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
add(*nums)         # add(1, 2, 3) 과 동일

info = {"a": 1, "b": 2, "c": 3}
add(**info)        # add(a=1, b=2, c=3) 과 동일


## 4. lambda - 이름 없는 한 줄 함수
# 간단한 함수를 짧게 표햔할 때 사용
# lambda 매개변수: 반환값
# 일반 함수
def square(x):
    return x ** 2

# 람다로 표현
square = lambda x: x ** 2
square(5)   # 25

add = lambda a, b: a + b
add(3, 4)   # 7

# 실제로 가장 많이 쓰이는 곳 - 정렬 기준(key) 지정
students = [("철수", 90), ("영희", 85), ("민수", 95)]

# 점수(두 번째 요소) 기준으로 정렬
students.sort(key=lambda x: x[1])
print(students)  # [('영희', 85), ('철수', 90), ('민수', 95)]

# 내림차순
students.sort(key=lambda x: x[1], reverse=True)

# map, filter와 함께 쓰기
# 요즘은 map/filter + lambda 조합보다 리스트 컴프리헨션([x**2 for x in nums]) 더 선호
nums = [1, 2, 3, 4, 5]

# map: 각 요소에 함수 적용
squared = list(map(lambda x: x ** 2, nums))   # [1, 4, 9, 16, 25]

# filter: 조건에 맞는 요소만 걸러냄
evens = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]


## 5. 재귀함수 (Recursion)
# 함수가 자기 자신을 호출하는 방식
# 종료 조건(base case)이 반드시 있어야 무한루프에 빠지지 않음
# 팩토리얼: 5! = 5*4*3*2*1
def factorial(n):
    if n == 1:          # 종료 조건 (base case)
        return 1
    return n * factorial(n - 1)   # 자기 자신 호출 (재귀 호출)

factorial(5)   # 120

# 5-1. 동작 흐름(factorial(3) ex)
# 팩토리얼의 시간 복잡도 : factorial(n)은 자기 자신을 n-1번 호출함 (n -> n-1 -> n-2 -> ... -> 1)
#                       호출 횟수가 n에 정비례하므로 시간 복잡도는 0(n)
#                       호출 스택도 n만큼 쌓이므로 공간 복잡도도 0(n)
factorial(3)
= 3 * factorial(2)
= 3 * (2 * factorial(1))
= 3 * (2 * 1)
= 6

# 5-2. 재귀 예시2 - 피보나치 수열
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(fibonacci(i), end=" ")
# 0 1 1 2 3 5 8 13 21 34

# 피보나치의 시간 복잡도 - 왜 느린가?
# fibonacci(n) 하나를 호출하면 내부에서 fibonacci(n-1)과 fibonacci(n-2)를 각각 또 호출함
# fib(2), fib(3) 같은 값을 똑같이 여러 번 중복 계산하는게 보임
# 호출 횟수가 대략 2^n에 가깝게 늘어나서 시간 복잡도는 0(2^n) - n이 조금만 커져도(예: n=40) 체감상
# 멈춘 것처럼 느껴질 정도로 느려짐
                fib(5)
              /        \
          fib(4)        fib(3)
         /     \        /     \
      fib(3)  fib(2)  fib(2)  fib(1)
      /   \    /  \    /  \
   fib(2) fib(1) ...  ...

# 5-3. 재귀 예시3 - 리스트 합 구하기
def sum_list(lst):
    if not lst:            # 빈 리스트면 종료
        return 0
    return lst[0] + sum_list(lst[1:])

sum_list([1, 2, 3, 4, 5])  # 15

# 주의사항
# 종료 조건 없으면 RecursionError: maximum recursion depth exceeded 에러 발생
# 재귀는 코드가 간결해지지만 반복문(for/while)보다 메모리를 더 많이 씀 (호출 스택이 쌓이기 때문)
# 피보나치처럼 같은 계산을 반복하는 경우 실전에서는 비효율적 -> 메모이제이션으로 개선 가능


## 6. 시간 복잡도 (Big-O)
# 코드가 입력 크기(n)에 따라 얼마나 느려지는지를 나타내는 표기법
# '정확한 실행 시간'이 아닌 'n이 커질 때 증가하는 추세'를 봄

# 자주 나오는 Big-O 종류 (빠른 순 -> 느린 순)
O(1)        상수 시간    — 입력 크기와 무관하게 항상 일정
O(log n)    로그 시간    — 매번 절반씩 줄어드는 경우 (이진 탐색 등)
O(n)        선형 시간    — 입력 크기만큼 딱 한 번씩 처리
O(n log n)  선형로그      — 효율적인 정렬 알고리즘 (병합정렬 등)
O(n^2)      제곱 시간    — 이중 반복문
O(2^n)      지수 시간    — 재귀로 경우의 수가 매번 2배씩 늘어남 (피보나치)

# 코드
# O(1) — 인덱스로 바로 접근, n이 커져도 시간 동일
def get_first(lst):
    return lst[0]

# O(n) — 리스트 크기만큼 한 번씩 순회
def find_max(lst):
    max_val = lst[0]
    for num in lst:          # n번 반복
        if num > max_val:
            max_val = num
    return max_val

# O(n^2) — 반복문 안에 반복문 (n번 * n번)
def has_duplicate(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):     # 이중 반복
            if i != j and lst[i] == lst[j]:
                return True
    return False

# O(log n) — 매번 탐색 범위를 절반으로 줄임
def binary_search(sorted_lst, target):
    low, high = 0, len(sorted_lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_lst[mid] == target:
            return mid
        elif sorted_lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1