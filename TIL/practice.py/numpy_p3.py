# axis

# 이전에 평균 구할 때
# 모든 숫자를 대상으로 평균
import numpy as np

scores = np.array([
    [80, 90, 70],
    [70, 80, 90],
    [90, 85, 95]
])

print(np.mean(scores))   # 84.444...

# 그런데 학생별 평균을 구하고 싶다면?
import numpy as np

scores = np.array([
    [80, 90, 70],
    [70, 80, 90],
    [90, 85, 95]
])

print(np.mean(scores, axis=1))   # [80.         80.         90.        ]
# 학생 1 → (80 + 90 + 70) / 3 = 80
# 학생 2 → (70 + 80 + 90) / 3 = 80
# 학생 3 → (90 + 85 + 95) / 3 = 90

# axis=1
# 각 행(row)을 기준으로 계산
np.mean(scores, axis=1)  # -> 각 학생의 평균

# axis=0
# 각 열별 기준으로 계산
print(np.mean(scores, axis=0))   # [80.         85.         85.        ] -> 과목별 평균

# 문제6
# 다음 데이터가 있을때
import numpy as np

scores = np.array([
    [80, 90, 70],
    [70, 80, 90],
    [90, 85, 95],
    [60, 75, 80]
])

# 학생별 평균을 구해라
print(np.mean(scores, axis=1))    # [80. 80. 90. 71.66666667]

# 과목별 평균을 구해라
print(np.mean(scores, axis=0))    # [75. 82.5 83.75]

# 학생별 최고 점수를 구해라
print(np.max(scores, axis=1))     # [90 90 95 80]