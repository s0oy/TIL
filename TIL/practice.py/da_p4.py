# 데이터 전처리

# 1. Pandas 데이터 전처리
# 분석이나 ML 하기 전에는 데이터의 결측값, 중복값, 이상한 값 등을 정리해야 함

import pandas as pd
import numpy as np

data = {
    "품목": ["사과", "배", "사과", "포도", "배", "포도"],
    "월": [1, 1, 2, 2, 3, 3],
    "가격": [3000, 2500, np.nan, 4000, 2700, 4200],
    "판매량": [10, 15, 12, 8, 15, 9]
}

df = pd.DataFrame(data)

print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

- 결측값 처리
# 주의할 점 -> 결측값을 무조건 0으로 채우면 안 됨
#             데이터의 의미에 따라 평균, 중앙값, 별도 표시, 삭제 등을 선택해야 함

# 열마다 결측값 개수 확인
print(df.isnull().sum())    # isnull() -> 결측값인지 확인

# 가격의 결측값을 가격 평균으로 채우기
df["가격"] = df["가격"].fillna(df["가격"].mean())

# 결측값이 남아 있는 행 제거
df = df.dropna()

# 자료형 확인
print(df.dtypes)

- 중복값 처리
# 전체 행이 똑같은 경우만 제거하고 싶을 땐 이렇게 하면 됨
# 이름이 같다는 이유만으로 삭제하면 서로 다른 기록을 잃을 수도 있음

# 중복 행 확인
print(df.duplicated())

# 중복 행 제거
df = df.drop_duplicates()

- 데이터 타입 확인 및 변경
print(df.dtypes)

df["가격"] = df["가격"].astype(int)
# astype() -> 숫자로 변환 가능한 값에만 사용해야 함
#             결측값이 남아 있거나 숫자가 아닌 문자열이 있다면 오류 날 수 있음


# 2. groupby()와 agg() - 그룹별 분석
# groupby() -> 데이터를 그룹별로 나눠 계산 시 사용
# agg() -> 여러 통계량을 한 번에 계산 시 유용

# 품목별 평균 가격
print(df.groupby("품목")["가격"].mean())

# 품목별 평균·최고·최저 가격
print(
    df.groupby("품목")["가격"].agg(
        ["mean", "max", "min"]
    )
)

# 품목별 가격 평균과 판매량 합계
print(
    df.groupby("품목").agg(
        평균가격=("가격", "mean"),
        총판매량=("판매량", "sum")
    )
)

# 2-1. transform()은 왜 필요?
# groupby().mean() -> 그룹별 요약 결과 반환
# transform() -> 원래 행 수를 유지하면서 그룹 통계를 각 행에 붙일 수 있음

# 각 기록의 가격이 같은 품목의 평균보다 얼마나 높은지 또는 낮은지 계산 가능
df["품목평균가격"] = (
    df.groupby("품목")["가격"].transform("mean")
)

df["평균대비차이"] = df["가격"] - df["품목평균가격"]

print(df)


# 3. 데이터 결합 - merge() & concat()

# 예를 들어 가격 데이터와 품목 정보가 따로 있다고 할 때
# merge() -> 공통된 열을 기준으로 데이터 결합 => 키를 기준으로 결합
- how = "inner" : 양쪽에 모두 있는 키만 유지
- how = "left" : 왼쪽 데이터 전체 유지
- how = "right" : 오른쪽 데이터 전체 유지
- how = "outer" : 양쪽의 키 모두 유지

prices = pd.DataFrame({
    "품목코드": [101, 102, 103],
    "가격": [3000, 2500, 4000]
})

products = pd.DataFrame({
    "품목코드": [101, 102, 103],
    "품목명": ["사과", "배", "포도"]
})

result = pd.merge(
    prices,
    products,
    on="품목코드",
    how="left"
)

print(result)

# count() -> 행이나 열 방향으로 데이터 이어 붙이는 데 사용
january = pd.DataFrame({
    "월": [1, 1],
    "가격": [3000, 2500]
})

february = pd.DataFrame({
    "월": [2, 2],
    "가격": [3100, 2600]
})

all_data = pd.concat(
    [january, february],
    ignore_index=True
)

print(all_data)


# 4. 날짜 데이터 처리
# 시계열 데이터, 즉 시간에 따라 기록된 데이터는 날짜를 올바른 자료형으로 변환하는게 중요

df = pd.DataFrame({
    "날짜": ["2026-01-01", "2026-02-15", "2026-03-20"],
    "가격": [3000, 3200, 3100]
})

df["날짜"] = pd.to_datetime(df["날짜"])

df["연도"] = df["날짜"].dt.year
df["월"] = df["날짜"].dt.month

print(df)

# 날짜 범위로 데이터 필터링
result = df[
    (df["날짜"] >= "2026-02-01")
    & (df["날짜"] < "2026-04-01")
]

print(result)


# 5. 데이터 시각화 - Matplotlib
# 분석 결과를 그래프로 확인
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "월": [1, 2, 3, 4, 5, 6],
    "가격": [3000, 3200, 2900, 3500, 3700, 3400]
})

plt.plot(df["월"], df["가격"], marker="o")   # plt.plot() -> 시간에 따른 변화
plt.xlabel("Month")
plt.ylabel("Price")
plt.title("Monthly Price")
plt.grid(True)
plt.show()

plt.bar()       # 항목별 비교
plt.scatter()   # 두 변수 사이의 관계
plt.hist()      # 데이터 분포