# 1. 변수와 자료형

# 변수 선언 (타입 명시 불필요)
name = "철수"        # str
age = 25             # int
height = 175.5       # float
is_student = True    # bool

# 여러 개 동시 할당
x, y, z = 1, 2, 3

# 타입 확인
print(type(age))  # <class 'int'>

# point : Python은 동적 타입 언어라 변수 선언 시 타입 안 써도 됨
#         But, type()으로 언제든 확인 가능


# 2. f-string(문자열 포맷팅)
# 가장 많이 쓰이는 문자열 조합 방법
# f"..." 안에 {}로 변수/표현식 바로 넣음

name = "철수"
age = 25

print(f"이름: {name}, 나이: {age}")
# 이름: 철수, 나이: 25

# 표현식도 바로 계산 가능
print(f"내년 나이: {age + 1}")

# 소수점 자리수 지정
pi = 3.14159265
print(f"파이: {pi:.2f}")  # 파이: 3.14

# 천 단위 콤마
big_num = 1234567
print(f"숫자: {big_num:,}")  # 숫자: 1,234,567

# 정렬 (폭 지정)
print(f"{name:>10}")  # 오른쪽 정렬, 폭 10
print(f"{name:<10}")  # 왼쪽 정렬
print(f"{name:^10}")  # 가운데 정렬


# 3. list
# 순서가 있고, 값 변경 가능(mutable)한 자료형

fruits = ["사과", "바나나", "포도"]

# 자주 쓰는 메서드
fruits.append("딸기")        # 맨 뒤에 추가
fruits.insert(1, "오렌지")   # 특정 위치에 삽입
fruits.remove("바나나")      # 값으로 삭제 (첫 번째 매칭)
fruits.pop()                 # 맨 뒤 요소 삭제 후 반환
fruits.pop(0)                 # 인덱스로 삭제 후 반환
fruits.sort()                 # 정렬 (원본 변경)
fruits.sort(reverse=True)     # 내림차순
fruits.reverse()              # 순서 뒤집기
fruits.index("사과")          # 값의 인덱스 찾기
fruits.count("사과")          # 특정 값 개수 세기
fruits.extend(["망고", "키위"])  # 리스트 합치기
len(fruits)                   # 길이

# 정렬된 새 리스트 (원본 유지)
sorted_fruits = sorted(fruits)

# append vs extend 차이
a = [1, 2]
a.append([3, 4])   # [1, 2, [3, 4]]  ← 리스트째로 추가됨
a2 = [1, 2]
a2.extend([3, 4])  # [1, 2, 3, 4]    ← 요소가 풀려서 추가됨


# 4. 딕셔너리(dictionary)
# 키-값 쌍으로 이루어진 자료형
# 주의 : person["없는키"]는 에러 발생 -> 안전하게 접근하려면 .get() 사용
person = {"name": "철수", "age": 25, "city": "서울"}

# 자주 쓰는 메서드
person.get("name")            # "철수" (키 없으면 None, 에러 안 남)
person.get("job", "무직")      # 키 없을 때 기본값 지정 가능
person.keys()                 # 키 전체 (dict_keys(['name','age','city']))
person.values()                # 값 전체
person.items()                 # (키, 값) 쌍 전체

person["job"] = "학생"         # 새 키 추가 or 값 변경
person.update({"age": 26})     # 여러 개 업데이트
person.pop("city")             # 키로 삭제 후 값 반환
del person["job"]               # 키로 삭제

"name" in person                # 키 존재 확인 → True/False

# for문으로 순회 (제일 많이 씀)
for key, value in person.items():
    print(f"{key}: {value}")


# 5. 슬라이싱(slicing)
# 리스트, 문자열 등에서 부분 추출 가능 [시작:끝:간격]
# 끝 인덱스는 항상 포함되지 않음 (미만) [a:b] -> a <= i < b
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

nums[2:5]     # [2, 3, 4]   ← 인덱스 2부터 4까지 (5는 미포함)
nums[:3]      # [0, 1, 2]   ← 처음부터 인덱스 2까지
nums[7:]      # [7, 8, 9]   ← 인덱스 7부터 끝까지
nums[:]       # 전체 복사
nums[::2]     # [0, 2, 4, 6, 8]  ← 2칸씩 건너뛰기
nums[::-1]    # [9, 8, 7, ..., 0]  ← 뒤집기
nums[-3:]     # [7, 8, 9]   ← 뒤에서 3개
nums[-3:-1]   # [7, 8]      ← 음수 인덱스도 가능

# 문자열도 동일하게 적용됨
s = "Python"
s[1:4]   # "yth"
s[::-1]  # "nohtyP"


# 6. 조건문 (if/elif/else)
# Python은 {} 대신 들여쓰기로 블록 구분
# 들여쓰기 안 맞으면 바로 에러
age = 20

if age >= 20:
    print("성인")
elif age >= 14:
    print("청소년")
else:
    print("어린이")

# 한 줄 조건문 (삼항 연산자)
result = "성인" if age >= 20 else "미성년자"

# 여러 조건 결합
score = 85
if score >= 80 and score < 90:
    print("B등급")

# in 으로 여러 값 체크
fruit = "사과"
if fruit in ["사과", "바나나", "포도"]:
    print("과일 목록에 있음")

# 비교/논리 연산자 정리
# ==  같다        !=  다르다
# >   초과         >=  이상
# <   미만         <=  이하
# and 그리고        or  또는       not 아님


# 7. 반복문
# for문 : 리스트, 문자열 등 순회 가능
# range() 활용
for i in range(5):        # 0,1,2,3,4
    print(i)

for i in range(2, 10, 2):  # 2,4,6,8 (시작,끝,간격)
    print(i)

# 리스트 순회
fruits = ["사과", "바나나", "포도"]
for fruit in fruits:
    print(fruit)

# 인덱스와 값 같이 필요할 때 → enumerate
for idx, fruit in enumerate(fruits):
    print(f"{idx}: {fruit}")

# 딕셔너리 순회
person = {"name": "철수", "age": 25}
for key, value in person.items():
    print(f"{key} -> {value}")

# 두 리스트 동시에 순회 → zip
names = ["철수", "영희"]
scores = [90, 85]
for name, score in zip(names, scores):
    print(f"{name}: {score}점")

# while문 : 조건이 True인 동안 반복
count = 0
while count < 5:
    print(count)
    count += 1

# 반복 제어
for i in range(10):
    if i == 3:
        continue   # 이번 반복만 건너뛰기
    if i == 7:
        break      # 반복문 전체 종료
    print(i)

# 리스트 컴프리헨션 : 간단한 반복문을 한 줄로
# 일반 for문
squares = []
for i in range(5):
    squares.append(i ** 2)

# 컴프리헨션으로 한 줄에
squares = [i ** 2 for i in range(5)]   # [0, 1, 4, 9, 16]

# 조건 포함
evens = [i for i in range(10) if i % 2 == 0]  # [0,2,4,6,8]


# 8. 기본 함수
# return이 없으면 None 반환
# 파라미터에 기본값 없는 것들은 기본값 있는 것보다 앞에 와야 함
# 함수 안에서 만든 변수(지역 변수)는 함수 밖에서 못 씀
def greet(name):
    return f"안녕하세요, {name}님!"

print(greet("철수"))

# 기본값 파라미터
def greet(name, greeting="안녕"):
    return f"{greeting}, {name}님!"

greet("철수")               # 기본값 사용
greet("철수", "반가워")      # 기본값 대신 전달

# 여러 값 반환 (튜플로 묶여서 반환됨)
def calc(a, b):
    return a + b, a - b, a * b

sum_, diff, prod = calc(10, 3)

# 가변 인자 (*args, **kwargs)
def add_all(*args):
    return sum(args)

add_all(1, 2, 3, 4)  # 10

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="철수", age=25)


# 9. 문자열(string) method
s = "  Hello, Python World!  "

s.strip()          # "Hello, Python World!"  ← 양쪽 공백 제거
s.lower()          # "hello, python world!"
s.upper()          # "  HELLO, PYTHON WORLD!  "
s.replace("Python", "Java")  # "  Hello, Java World!  "

# 나누기 / 합치기
words = "사과,바나나,포도".split(",")   # ["사과", "바나나", "포도"]
"-".join(words)                        # "사과-바나나-포도"

# 포함 여부 / 위치
"Python" in s          # True
s.find("Python")       # 인덱스 반환 (없으면 -1)
s.startswith("  He")   # True
s.endswith("!  ")      # True

# 개수 세기 / 채우기
"banana".count("a")    # 3
"5".zfill(3)           # "005"

# 형변환
str(123)      # "123"
int("123")    # 123
float("3.14") # 3.14


# 10. tuple & set
# tuple : 순서가 있고, 값 변경 불가(immutable)한 자료형
# 값이 바뀌면 안되는 고정 데이터(좌표, 설정값 등)에 사용
# 리스트보다 속도도 살짝 빠름
point = (3, 5)
x, y = point           # 튜플 언패킹

# 값 변경 불가 → 에러
# point[0] = 10   ← TypeError 발생

# 함수가 여러 값 반환할 때 사실 튜플로 반환하는 것
def calc(a, b):
    return a + b, a - b   # 사실 (a+b, a-b) 튜플임

# set : 순서 없고, 중복 불가한 자료형
# 중복 재거할 때, 교집합/합집합 같은 집합 연산이 필요할 때 유용
# ex) list(set(원본리스트))로 중복 제거
nums = {1, 2, 2, 3, 3, 3}
print(nums)   # {1, 2, 3}  ← 중복 자동 제거

nums.add(4)
nums.remove(1)

a = {1, 2, 3}
b = {2, 3, 4}
a & b   # 교집합 {2, 3}
a | b   # 합집합 {1, 2, 3, 4}
a - b   # 차집합 {1}


# 11 .예외처리 (try/except)
# 에러가 나도 프로그램이 멈추지 않게 방어
# except: 만 단독으로 쓰면 모든 에러 다 잡아버려서 디버깅 힘들어짐
#         어떤 에러인지 명시하는 습관 들이는게 좋음
# except ValueError:  # 특정 에러만 잡고 싶을 때
try:
    num = int(input("숫자 입력: "))
    result = 10 / num
except ValueError:
    print("숫자가 아닙니다.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
else:
    print(f"결과: {result}")   # 에러 없을 때만 실행
finally:
    print("실행 완료")          # 에러 여부와 상관없이 항상 실행

# 자주 만나는 에러 종류
ValueError        # 타입은 맞는데 값이 이상함 (예: int("abc"))
ZeroDivisionError  # 0으로 나눔
KeyError           # 딕셔너리에 없는 키 접근
IndexError         # 리스트 범위 벗어난 인덱스 접근
TypeError          # 타입이 안 맞는 연산