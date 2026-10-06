# 11. groupby()
# 그룹별 데이터 분석
df.groupby("그룹 기준")["분석할 열"].mean()

# 예를 들어 학생들의 학년별 점수를 분석한다고 할 때
import pandas as pd

data = {
    "이름": ["민수", "지수", "철수", "영희", "수진"],
    "반": ["A", "A", "B", "B", "A"],
    "점수": [80, 90, 70, 85, 95]
}

df = pd.DataFrame(data)

# ① 반별 평균 점수
# 반을 기분으로 그룹을 나눈 다음, 각 그룹의 점수 평균을 계산
print(df.groupby("반")["점수"].mean())   # mean() -> 평균

# ② 반별 점수 합계
print(df.groupby("반")["점수"].sum())    # sum() -> 합계

# ③ 반별 학생 수 
print(df.groupby("반")["이름"].count())  # count() -> 해당 열에서 결측치가 아닌 값의 개수 셈

# ④ 여러 통계를 한 번에
# agg() -> 평균, 최댓값 등 한 번에 계산 가능
print(df.groupby("반")["점수"].agg(["mean", "max", "min", "count"]))

함수	의미
mean()	평균
sum()	합계
max()	최댓값
min()	최솟값
count()	결측치가 아닌 값의 개수
size()	그룹의 전체 행 개수


# 12. value_counts()
# 값 별 개수 세기
df["결과"].value_counts()

data = {
    "이름": ["민수", "지수", "철수", "영희", "수진"],
    "반": ["A", "A", "B", "B", "A"],
    "결과": ["합격", "합격", "불합격", "합격", "불합격"]
}

df = pd.DataFrame(data)

print(df["결과"].value_counts())
# 결과
# 합격     3
# 불합격   2

# 비율로 확인하기
print(df["결과"].value_counts(normalize=True))  # 결과를 비율로 반환

# 퍼센트로 보고 싶다면
print(df["결과"].value_counts(normalize=True) * 100)

# groupby()와 차이
# 둘 다 개수를 셀 수 있지만 단순히 값별 빈도를 확인할 때는 value_counts()가 편리
# 결과별 학생 수
df.groupby("결과")["이름"].count()


# 13. read_csv() - CSV 파일 읽기
# CSV는 데이터를 표 형태로 저장하는 파일 형식

# 예를 들어 scores.csv 파일이 다음과 같다고 할 때
이름,점수,반
민수,80,A
지수,90,A
철수,70,B

# Python에서 읽는 방법
# 파일이 Python 코드와 같은 폴더에 있다면 파일명만 적어도 됌
import pandas as pd

df = pd.read_csv("scores.csv")

print(df)

# 다른 폴더에 있다면 경로 지정해야 함
# 윈도우에서도 "/"를 경로 구분자로 사용 가능
df = pd.read_csv("C:/Users/kimso/Desktop/scores.csv")

# 읽은 데이터 확인하기
# 데이터를 불러온 직후 행 일부, 크기, 자료형, 결측치 확인 가능
df = pd.read_csv("scores.csv")

print(df.head())
print(df.shape)
print(df.dtypes)
print(df.isnull().sum())

# 한글이 깨지는 경우
# CSV 파일의 인코딩에 따라 다음처럼 읽어야 할 수 있음
# 한글이 깨진다고 무조건 둘 중 하나가 정답인건 아니고 파일의 실제 인코딩에 맞춰야 함
df = pd.read_csv("scores.csv", encoding="utf-8-sig")
df = pd.read_csv("scores.csv", encoding="cp949")


# 14. to_csv() - CSV 파일 저장
# 분석한 DataFrame을 CSV 파일로 저장할 수 있음
df.to_csv("result.csv", index=False)

index=True : 행 번호도 함께 저장
index=False : 행 번호는 저장하지 않음

# 한글이 포함된 CSV를 액셀에서 열 계획이라면 다음처럼 저장하는 것도 좋음
df.to_csv(
    "result.csv",
    index=False,
    encoding="utf-8-sig"
)

# 주의 : 파일을 저장할 때 같은 이름의 파일이 이미 있다면 덮어쓸 수 있음


# 15. loc - 조건으로 행/열 선택
# 행과 열을 이름으로 선택할 때 사용
data = {
    "이름": ["민수", "지수", "철수", "영희"],
    "나이": [20, 21, 20, 22],
    "점수": [80, 90, 70, 85]
}

df = pd.DataFrame(data)

# 특정 행 선택
print(df.loc[0])   # 인덱스가 0인 행

# 특정 행 + 특정 열
print(df.loc[0, "이름"])  # 민수

# 여러 행 + 특정 열
print(df.loc[0:2, "이름"])   # 0 ~ 2번 행의 이름

# 조건과 함께
print(df.loc[df["점수"] >= 80, ["이름", "점수"]])   # 80점 이상인 사람의 이름과 점수만 가져와라


# 16. iloc - 위치로 선택
# 번호/위치 기준
print(df.iloc[0])         # 첫 번째 행
print(df.iloc[0, 2])      # 첫 번째 행, 세 번째 열
print(df.iloc[:, 1])      # 모든 행의 두 번째 열
print(df.iloc[0:2, 0:2])  # 0 ~ 1번 행, 0 ~ 1번 열


# 17. rename() - 열 이름 변경

# 예를 들어
df = df.rename(columns={"점수": "성적"})   # 점수 -> 성적으로 바뀜

# 여러 개도 가능
df = df.rename(columns={
    "이름": "학생명",
    "점수": "성적"
})


# 18. drop() - 행/열 삭제

# 열 삭제
df = df.drop(columns=["나이"])    # '나이' 열 삭제
# 여러개
df = df.drop(columns=["나이", "점수"])

# 행 삭제
df = df.drop(index=0)    # 인덱스 0인 행 삭제


# 19. replace() - 값 바꾸기
# 특정 값을 다른 값으로 변경 가능

# 예를 들어
df["성별"] = df["성별"].replace({
    "남": "남성",
    "여": "여성"
})

# 전체 DataFrame에서도 가능
df = df.replace("미정", "없음")


# 20. duplicated() - 중복 데이터 확인
# 중복된 행인지 확인
print(df.duplicated())

# ex
False
False
True    # True가 중복된 데이터
False

# 중복 데이터 삭제
df = df.drop_duplicates()