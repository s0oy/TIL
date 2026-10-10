# 데이터 전처리

# 1. Pandas 데이터 전처리
# 분석이나 ML 하기 전에는 데이터의 결측값, 중복값, 이상한 값 등을 정리해야 함

import pandas as pd
import numpy as np

data = {
    "이름": ["민수", "지수", "철수", "영희", "민수"],
    "공부시간": [2, 5, np.nan, 1, 2],
    "점수": [70, 90, 85, np.nan, 70]
}

df = pd.DataFrame(data)
print(df)

# 결측값 처리
# 주의할 점 -> 결측값을 무조건 0으로 채우면 안 됨
#             데이터의 의미에 따라 평균, 중앙값, 별도 표시, 삭제 등을 선택해야 함

# 열마다 결측값 개수 확인
print(df.isnull().sum())    # isnull() -> 결측값인지 확인

# 공부시간 결측값을 평균으로 채우기
df["공부시간"] = df["공부시간"].fillna(     # fillna() -> 결측값 채우기
    df["공부시간"].mean()
)

# 점수 결측값이 있는 행 삭제
df = df.dropna(subset=["점수"])    # dropna() -> 결측값이 있는 행이나 열 삭제

# 중복값 처리
# 전체 행이 똑같은 경우만 제거하고 싶을 땐 이렇게 하면 됨
# 이름이 같다는 이유만으로 삭제하면 서로 다른 기록을 잃을 수도 있음

# 중복 행 확인
print(df.duplicated())

# 중복 행 제거
df = df.drop_duplicates()

# 데이터 타입 확인 및 변경
print(df.dtypes)

df["점수"] = df["점수"].astype(int)
# astype() -> 숫자로 변환 가능한 값에만 사용해야 함
#             결측값이 남아 있거나 숫자가 아닌 문자열이 있다면 오류 날 수 있음


# 2. 데이터 분석 실전 함수

# 점수 높은 순으로 정렬
df.sort_values("점수", ascending=False)

# 점수 평균
print(df["점수"].mean())

# 점수별 학생 수
print(df["점수"].value_counts())

# 공부시간별 평균 점수
print(df.groupby("공부시간")["점수"].mean())

# 공부시간이 3시간 이상인 학생만 선택
print(df.loc[df["공부시간"] >= 3, ["이름", "점수"]])