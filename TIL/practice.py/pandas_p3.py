# apply() 심화
# 1. apply()가 하는 일
# 열의 값을 하나씩 꺼내서 내가 만든 함수를 적용하는 것

# 예를 들어 점수가 아래와 같다면
75
90
85
60
95

df["점수"].apply(함수)
# 내부적으로 대략 아래와 같이 처리한다고 생각하면 됨
75 → 함수(75)
90 → 함수(90)
85 → 함수(85)
60 → 함수(60)
95 → 함수(95)


# 2. 일반 함수로 사용

# 예를 들어 점수에 5점을 더하고 싶다고 할 때
def add_five(score):
    return score + 5

df["수정점수"] = df["점수"].apply(add_five)  # 점수 하나씩 add_five()에 넣는다


# 3. lambda?
df["점수"].apply(lambda x: x + 5)

# 원래 식
def add_five(score):
    return score + 5

# 이걸 한 줄로
lambda score: score + 5

# 그래서 이렇게 할 수 있음
df["수정점수"] = df["점수"].apply(
    lambda score: score + 5
)

# 구조
lambda 변수: 결과

# ex
lambda x: x * 2  # x를 받아서 x * 2로 반환


# 4. lambda + 조건문

# 80점 이상이면 "합격", 아니면 "불합격"
df["결과"] = df["점수"].apply(
    lambda x: "합격" if x >= 80 else "불합격"
)

# 구조
lambda x: A if 조건 else B    # 조건 만족 -> A, 조건 불만족 -> B


# 5. 조건이 2개 이상

# 조건
# 90이상 -> A, 80이상 -> B, 80미만 -> C

# lambda로
df["등급"] = df["점수"].apply(
    lambda x: "A" if x >= 90
    else "B" if x >= 80
    else "C"
)

# 풀어서 생각하면
x >= 90?
 ├─ YES → A
 └─ NO
      ↓
   x >= 80?
    ├─ YES → B
    └─ NO → C


# 6. 꼭 lambda를 써야 하나?
# XX -> 조건이 복잡해질수록 일반 함수가 더 읽기 편함
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    else:
        return "C"

df["등급"] = df["점수"].apply(get_grade)

# 실무에서도 가독성이 중요하면 일반 함수를 쓰는 게 좋음
간단한 조건 -> lambda
복잡한 조건 -> def 함수


# 7. 여러 열을 이용해서 계산하기

# 예를 들어 데이터에 중간고사 기말고사 두 열이 있다고 할 때
# 평균을 새로운 열로 만들고 싶다면
df["평균"] = (df["중간고사"] + df["기말고사"]) / 2

# 이 경우는 굳이 apply()가 필요 없음 -> Pandas가 열끼리 계산해줌


# 여러 열 + 조건이 필요하다면?

# 예를 들어 평균이 80이상이고 출석률이 90이상이면 "우수" -> apply() 사용 가능
# 다만 이때는 행 전체를 가져와야 하기 때문에 axis=1이 등장
def check(row):
    if row["평균"] >= 80 and row["출석률"] >= 90:
        return "우수"
    else:
        return "일반"

df["평가"] = df.apply(check, axis=1)

# 문제1
# "보너스 점수" 열을 만들어라 -> 점수에 10점을 더한다
df["보너스점수"] = df["점수"].apply(lambda x: x + 10)

# 문제2
# "결과" 열을 만들어라 -> 80점이상 - "합격", 80점미만 - "불합격"
df["결과"] = df["점수"].apply(
    lambda x: "합격" if x >= 80 else "불합격"
)

# 문제3
# "등급" 열을 만들어라 -> 90점이상 - "A", 80점이상 - "B", 그 외 - "C"
df["등급"] = df["점수"].apply{
    lambda x: "A" if x >= 90
    else "B" if x >- 80
    else "C"
}