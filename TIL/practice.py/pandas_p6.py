# Pandas 종합 실습

# 1. 데이터 준비
import pandas as pd

data = {
    "이름": ["민수", "지수", "철수", "영희", "수진", "현우", "유진", "준호"],
    "학년": [1, 2, 1, 3, 2, 3, 1, 2],
    "과목": ["Python", "Python", "ML", "ML", "Python", "ML", "Python", "ML"],
    "점수": [75, 92, 85, 68, 95, 78, 88, 60],
    "출석률": [90, 95, 85, 80, 100, 90, 95, 75]
}

df = pd.DataFrame(data)

# 2. 데이터 확인
# 가장 먼저 데이터가 제대로 들어왔는지 확인
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())

print(df.describe())


# 3. 조건으로 데이터 찾기
# Python 과목만
df[df["과목"] == "Python"]

# 점수 80점 이상
df[df["점수"] >= 80]

# Python이면서 80점 이상
df[(df["과목"] == "Python") & (df["점수"] >= 80)]

# 2학년 또는 3학년
df[df["학년"].isin([2, 3])]


# 4. 필요한 열만 선택

# 예를 들어 이름과 점수만 보고 싶으면
df[["이름", "점수"]]

# 조건과 같이 사용
df[df["점수"] >= 80][["이름", "점수"]]


# 5. 새로운 열 만들기
# 합격 여부
df["결과"] = df["점수"].apply(
    lambda x: "합격" if x >= 80 else "불합격"
)

# 등급
df["등급"] = df["점수"].apply(
    lambda x: "A" if x >= 90
    else "B" if x >= 80
    else "C"
)


# 6. 정렬
# 점수가 높은 순서
df = df.sort_values("점수", ascending=False)

# 낮은 순서
df = df.sort_values("점수")

# 여러 기준
# 과목별로 묶고, 그 안에서는 점수가 높은 순
df.sort_values(["과목", "점수"], ascending=[True, False])


# 7. 그룹별 분석
# 과목별 평균
df.groupby("과목")["점수"].mean()

# 학년별 평균
df.groupby("학년")["점수"].mean()

# 과목별 최고점
df.groupby("과목")["점수"].max()

# 과목별 학생 수
df["과목"].value_counts()


# 8. 출석률까지 같이 분석

# 예를 들어 출석률 90% 이상인 학생들의 평균 점수
df[df["출석률"] >= 90]["점수"].mean()


# 9. loc으로 원하는 데이터 뽑기
# loc -> 특히 조건 + 특정 열 선택을 같이 할 때 유용

# 예를 들어 점수 80이상인 학생의 이름과 점수
df.loc[df["점수"] >= 80, ["이름", "점수"]]


# 10. 데이터 저장
# 분석 결과를 CSV로 저장
result = df[df["점수"] >= 80]

result.to_csv("result.csv", index=False, encoding="utf-8-sig")


# 실습
import pandas as pd

data = {
    "이름": ["민수", "지수", "철수", "영희", "수진", "현우", "유진", "준호"],
    "학년": [1, 2, 1, 3, 2, 3, 1, 2],
    "과목": ["Python", "Python", "ML", "ML", "Python", "ML", "Python", "ML"],
    "점수": [75, 92, 85, 68, 95, 78, 88, 60],
    "출석률": [90, 95, 85, 80, 100, 90, 95, 75]
}

df = pd.DataFrame(data)

# 문제 1 - 기본 필터링
# 점수가 80점 이상인 학생의 이름과 점수만 출력
df[df["점수"] >= 80][["이름", "점수"]]

# 문제 2 - 조건 2개
# Python 과목이면서 점수가 80점 이상인 학생만 출력
# 이름, 과목, 점수 출력
df[(df["과목"] == "Python") & (df["점수"] >= 80)][["이름", "과목", "점수"]]

# 문제 3 - isin()
# 2학년 또는 3학년 학생만 출력
df[df["학년"].isin([2, 3])]

# 문제 4 - 새 컬럼
# 점수를 기준으로 "등급" 컬럼 만들기
# 90이상 -> A, 80이상 -> B, 그 외 -> C
df["등급"] = df["점수"].apply(
    lambda x: "A" if x >= 90 else "B" if x >= 80 else "C"
)

# 문제 5 - apply()
# 출석률을 기준으로 "출석평가" 컬럼 만들기
# 90이상 -> 우수, 80이상 -> 보통, 그 미만 -> 주의
df["출석평가"] = df["출석률"].apply(
    lambda x: "우수" if x >= 90 else "보통" if x >= 80 else "주의"
)

# 문제 6 - 정렬
# 점수가 높은 순서대로 전체 데이터 정렬
df[df.sort_values("점수", ascending=False)]

# 문제 7 - groupby()
# 과목별 평균 점수 구하기
df.groupby("과목")["점수"].mean()

# 문제 8 
# 출석률이 90 이상인 학생들의 평균 점수 구하기
df[df["출석률"] >= 90]["점수"].mean()

# 문제 9 - loc
# 점수가 80점 이상인 학생의 이름과 출석률만 출력
df.loc[(df["점수"] >= 80),["이름", "출석률"]]

# 문제 10 - 종합
# 다음 조건을 모두 만족하는 학생 찾기 -> Python 과목 + 점수 80 이상 + 출석률 90 이상
# 이름, 점수, 출석률 출력
df[(df["과목"] == "Python") & (df["점수"] >= 80) & (df["출석률"] >= 90)][["이름", "점수", "출석률"]]