# Python -> NumPy -> Pandas 연결 + 실제 데이터 분석

# 1. Python -> NumPy

# 먼저 Python 리스트가 있다고 할 때
scores = [75, 82, 91, 68, 95]

# Python에서는 기본적으로 아래처럼 같이 계산 
sum(scores)
max(scores)
min(scores)

# NumPy로 바꾸면
import numpy as np

scores = [75, 82, 91, 68, 95]

arr = np.array(scores)

print(arr)
print(arr.mean())
print(arr.max())
print(arr.min())

# 중요한것
Python list -> np.array() -> NumPy 배열


# 2. NumPy에서 조건 필터

arr[arr >= 80]   # [82 91 95]

'arr >= 80' 이 조건을 먼저 만들고 'arr[arr >= 80]' 조건에 맞는 데이터만 가져오는 것


# 3. NumPy → Pandas

# 학생 이름까지 있다고 할 때
names = ["민수", "지수", "철수", "영희", "수진"]
scores = [75, 82, 91, 68, 95]

# NumPy로 점수를 처리할 수 있지만 이름과 점수를 같이 관리하려면 Pandas가 편리
import pandas as pd
import numpy as np

names = ["민수", "지수", "철수", "영희", "수진"]  # Python -> 데이터를 기본적으로 저장하고 반복/조건 등 처리
scores = [75, 82, 91, 68, 95]

arr = np.array(scores)   # NumPy -> 수치 데이터 계산

df = pd.DataFrame({      # Pandas -> 표 형태의 데이터 관리/분석
    "이름": names,
    "점수": arr
})

print(df)
#    이름  점수
# 0  민수  75
# 1  지수  82
# 2  철수  91
# 3  영희  68
# 4  수진  95


# 4. 3개를 연결해보기
import numpy as np
import pandas as pd

names = ["민수", "지수", "철수", "영희", "수진"]
scores = [75, 82, 91, 68, 95]
attendance = [90, 95, 85, 80, 100]

score_array = np.array(scores)
attendance_array = np.array(attendance)

df = pd.DataFrame({
    "이름": names,
    "점수": score_array,
    "출석률": attendance_array
})

print(df)

print(score_array.mean())    # NumPy -> 평균 계산
print(df[df["점수"] >= 80])   # Pandas -> 학생 필터링
print(df["점수"].mean())      # Pandas -> 평균 구하기


# 데이터 분석/ML 흐름
Python
↓
데이터를 불러오고 / 구조를 만들고
↓
NumPy
↓
숫자 배열 계산 / 수치 처리
↓
Pandas
↓
데이터 정리 / 필터 / 결측치 / 분석
↓
Scikit-learn
↓
ML 학습


# 문제 1
# 아래 코드에서 NumPy -> Pandas 연결 부분 작성해보기
import numpy as np
import pandas as pd

names = ["민수", "지수", "철수", "영희", "수진"]
scores = [75, 82, 91, 68, 95]

# 1. scores를 NumPy 배열로 변환
score_array = np.array(scores)

# 2. 이름과 점수를 가진 DataFrame 생성
df = pd.DataFrame({
    "이름": names,
    "점수": score_array
})

# 3. 점수 평균 출력
print(df["점수"].mean())

# 4. 점수가 80 이상인 학생 출력
print(df[df["점수"] >= 80])