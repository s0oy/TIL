# # 1. 함수 - 실전
# def calculate_average(numbers):
#     return sum(numbers) / len(numbers)

# scores = [80, 90, 75, 95]

# result = calculate_average(scores)

# print(result)   # 85.0

# # 핵심 -> 아래 코드 + 함수 밖에서 결과를 받아서 사용하는 것
# # def 함수이름(매개변수):
# #    ...
# #    return 결과

# # 2. *arga
# # 인자를 여러 개 받을 때
# def add_all(*numbers):    # *numbers는 여러 값을 튜플로 받음
#     return sum(numbers)

# print(add_all(10, 20))          # 30
# print(add_all(10, 20, 30, 40))  # 100

# # 3. **kwargs
# # 이름을 붙여서 여러 값을 받을 때
# # 딕셔너리
# def show_info(**info):
#     print(info)

# show_info(name="명수", age=19, major="AI")  # {'name': '명수', 'age': 19, 'major': 'AI'}

# # 4. 예외처리
# # 프로그램에서 오류가 발생해도 프로그램이 바로 종료되지 않도록 할 수 있음
# try:
#     number = int(input("숫자 입력: "))
#     print(10 / number)

# except ValueError:
#     print("숫자를 입력하세요.")

# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")

# # 5. 파일 읽기
# # with을 쓰면 파일을 다 사용한 뒤 자동으로 닫아줌
# with open("data.txt", "r", encoding="utf-8") as file:
#     data = file.read()

# print(data)

# # 파일 저장
# with open("result.txt", "w", encoding="utf-8") as file:
#     file.write("분석 결과입니다.")

# 문제1
# 다음 코드의 출력값은?
def calculate(x, y):
    return x + y * 2

result = calculate(3, 4)
print(result)     # 11

# 문제2
# 다음 함수 완성
def get_max(numbers):
    # 가장 큰 값을 반환
    return max(numbers)

print(get_max([10, 30, 20]))   # 30

# 문제3
# *args를 이용해서 숫자들의 평균을 반환하는 함수 만들기
def average(*numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return avg

print(average(10, 20, 30))   # 20.0

# 문제4
# 아래 코드에서 0을 입력해도 프로그램이 종료되지 않고 
# "0으로 나눌 수 없습니다." 출력되도록 수정
# number = int(input("숫자: "))
# print(100 / number)

try:
    number = int(input("숫자: "))
    print(100 / number)

except ValueError:
    print("숫자를 입력하세요.")

except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")

# 문제5
# 리스트에서 짝수만 새로운 리스트로 만드는 코드 작성
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)   # [2, 4, 6, 8]