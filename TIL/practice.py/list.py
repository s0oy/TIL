# 리스트
# 여러 값을 하나로 묶는 자료형
fruits = ["apple", "banana", "orange"]
print(fruits[0])   # apple

# Python은 0부터 시작

# 추가
fruits.append("melon")

# 삭제
fruits.remove("banana")

# 길이
len(fruits)

# 문제1
# 첫 번째 값 출력
numbers = [10, 20, 30, 40, 50]
print(numbers[0])    # 10

# 문제2
# 마지막 값 출력
numbers = [10, 20, 30, 40, 50]
print(numbers[4])    # 50

# 문제3 
# 60 추가
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
print(numbers)       # [10, 20, 30, 40, 50, 60]

# 문제4
# 20 삭제
numbers = [10, 20, 30, 40, 50]
numbers.remove(20)
print(numbers)       # [10, 30, 40, 50]

# 문제5
# 리스트 길이 출력
numbers = [10, 20, 30, 40, 50]
print(len(numbers))  # 5