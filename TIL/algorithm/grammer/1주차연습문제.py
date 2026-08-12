## 1. 리스트 [5, 3, 8, 1, 9, 2]를 오름차순 정렬하고, 짝수만 걸러서 새 리스트에 담아보기
num = [5, 3, 8, 1, 9, 2]
num.sort()  # 오름차순 정렬
evens = [n for n in num if n % 2 == 0]
print(evens)

## 2. 딕셔너리에 학생 3명의 이름과 점수를 저장하고, 평균 점수를 f-string으로 출력해보기
student = {"영희":95,"명수":78, "진철":88}
avg = sum(student.values()) / len(student)
print(f"평균 점수: {avg:.1f}")

## 3. 문자열 "Hello, Python World!"에서 슬라이싱만 이용해서 "Python"만 추출해보기
s = "Hello, Python World!"
print(s[7:13])

## 4. 리스트를 거꾸로 뒤집는 방법을 슬라이싱과 .reverse() 두 가지로 각각 해보기
nums = [1, 2, 3, 4, 5]

# 슬라이싱
reversed1 = nums[::-1]

# .reverse()
nums.reverse()

## 5. 1~100 사이 숫자 중 3의 배수이면서 5의 배수인 것들만 리스트로 만들어보기 (컴프리헨션 사용)
result = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]
print(result)

## 6. 리스트 [1, 2, 3, 4, 5]를 받아서 짝수 합/홀수 합을 각각 반환하는 함수 만들기
def sum_even_odd(lst):
    even_sum = sum(n for n in lst if n % 2 == 0)
    odd_sum = sum(n for n in lst if n % 2 != 0)
    return even_sum, odd_sum

e, o = sum_even_odd([1, 2, 3, 4, 5])
print(f"짝수 합: {e}, 홀수 합: {o}")

## 7. 딕셔너리 {"철수": 90, "영희": 85, "민수": 70}을 순회하면서 70점 미만이면 "재시험 대상"이라고 출력하기
scores = {"철수": 90, "영희": 85, "민수": 70}
for name, score in scores.items():
    if score < 70:
        print(f"{name}: 재시험 대상")
    else:
        print(f"{name}: 통과")

## 8. 임의의 개수의 숫자를 받아서 평균을 반환하는 함수를 *args로 만들어보기
def avg(*args):
    return sum(args) / len(args)

print(avg(10, 20, 30))

## 9. 문자열 "apple,banana,apple,grape,banana"를 , 기준으로 나눈 뒤, 중복 없이 정렬된 리스트로 만들어보기 (split + set 활용)
s = "apple,banana,apple,grape,banana"
result = sorted(set(s.split(",")))
print(result)

## 10. 사용자에게 숫자를 입력받아 짝/홀수를 판별하되, 숫자가 아닌 값을 입력하면 "숫자를 입력하세요"라고 출력하는 코드를 try/except로 작성해보기
try:
    num = int(input("숫자 입력: "))
    if num % 2 == 0:
        print("짝수입니다")
    else:
        print("홀수입니다")
except ValueError:
    print("숫자를 입력하세요")