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