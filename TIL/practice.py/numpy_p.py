# 1. NumPy?
# 수치 계산을 빠르게 처리하기 위한 라이브러리
import numpy as np

# 가장 기본
numbers = np.array([1, 2, 3, 4, 5])

print(numbers)        # [1 2 3 4 5]
print(type(numbers))  # <class 'numpy.ndarray'>

# 2. List vs NumPy 배열
# Python 리스트
numbers = [1, 2, 3]
print(numbers * 2)    # [1, 2, 3, 1, 2, 3] -> *2가 반복

# NumPy
# NumPy 배열에서는 숫자 하나하나에 계산 적용 가능
numbers = np.array([1, 2, 3])
print(numbers * 2)    # [2 4 6]

# 3. 기본 계산
import numpy as np

numbers = np.array([10, 20, 30, 40])

print(numbers + 10)   # [20 30 40 50]
print(numbers - 10)   # [ 0 10 20 30]
print(numbers * 2)    # [20 40 60 80]
print(numbers / 10)   # [1. 2. 3. 4.]

# 4. 배열끼리 계산
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(a + b)   # [11 22 33]
print(a * b)   # [10 40 90]

# 5. 평균/최대/최소
numbers = np.array([10, 20, 30, 40, 50])

print(np.mean(numbers))   # 30.0
print(np.max(numbers))    # 50
print(np.min(numbers))    # 10
print(np.sum(numbers))    # 150

# 6. 배열의 크기 확인
numbers = np.array([10, 20, 30, 40, 50])

print(numbers.shape)   # (5,) | shpae -> 배열의 구조
print(numbers.size)    # 5

# 7. 2차원 배열
data = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(data)         # [[1, 2, 3]
                    #  [4, 5, 6]]
print(data.shape)   # (2, 3) -> 2행 3열

# 8. 특정 데이터 가져오기
data = np.array([
    [80, 90, 70],
    [70, 80, 90],
    [90, 85, 95]
])

print(data[0])     # [80 90 70]
print(data[1])     # [70 80 90]
print(data[0][1])  # 90 -> 0번째 행의 1번째 값

# 문제1
# 다음 배열에서 모든 값에 10을 더해 출력
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers + 10)   # [20 30 40 50 60]

# 문제2
# 다음 배열의 평균, 최댓값, 최솟값 출력
import numpy as np

numbers = np.array([10, 30, 20, 50, 40])

print(np.mean(numbers))   # 30.0
print(np.max(numbers))    # 50
print(np.min(numbers))    # 10

# 문제3
# 다음 학생들의 점수가 있을 때
import numpy as np

scores = np.array([
    [80, 90, 70],
    [70, 80, 90],
    [90, 85, 95]
])

# 배열의 크기
print(scores.shape)   # (3, 3)

# 첫 번째 학생의 점수
print(scores[0])      # [80 90 70]

# 첫 번째 학생의 영어 점수 90
print(scores[0][1])   # 90