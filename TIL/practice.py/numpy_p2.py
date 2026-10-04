# NumPy 인덱싱 + 조건 필터링
# 1. 여러 데이터 가져오기
import numpy as np

scores = np.array([
    [80, 90, 70],
    [70, 80, 90],
    [90, 85, 95]
])

print(scores[0:2])    # [[80 90 70]
                      #  [70 80 90]]   -> 0번 ~ 2번 전까지 -> 즉 0번, 1번만 가져옴

# 2. 특정 열 가져오기
# : -> 모든 행
print(scores[:, 0])   # [80 70 90]

# 3. 조건으로 데이터 골라내기
numbers = np.array([10, 20, 30, 40, 50])

print(numbers > 30)   # [False False False  True  True]

print(numbers[numbers > 30])   # [40 50]  -> 조건 필터링

# 4. 머신러닝에서 왜 중요?
# 데이터를 조건에 따라 골라낼 수 있음
# 예를 들어 학생 점수가
scores = np.array([55, 80, 90, 40, 75])

# 여기서 70점 이상인 학생들만 뽑고 싶으면
result = scores[scores >= 70]
print(result)    # [80 90 75] 

# 문제4
# 다음 코드에서 80점 이상인 점수만 출력
import numpy as np

scores = np.array([65, 80, 90, 55, 75, 95])

result = scores[scores >= 80]

print(result)    # [80 90 95]

# 문제5
# 다음 데이터가 있을때 모든 학생의 영어 점수만 출력
import numpy as np

scores = np.array([
    [80, 90, 70],
    [70, 80, 90],
    [90, 85, 95],
    [60, 75, 80]
])

print(scores[:, 1])   # [90 80 85 75]