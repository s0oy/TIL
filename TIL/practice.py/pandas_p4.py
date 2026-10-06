# 1. head() / tail()
# head() -> 앞부분 보여줌
print(df.head())   # -> 기본적으로 처음 5개 행
print(df.head(3))  # -> 처음 3개만

# tail() -> 뒷부분 보여줌
print(df.tail())   # -> 마지막 5개
print(df.tail(2))  # -> 마지막 2개

# CSV 같은 큰 데이터 불러온 뒤 아래 코드처럼 데이터가 제대로 들어왔는지 확인할 때 사용
df = pd.read_csv("data.csv")
print(df.head())


# 2. shape
# 데이터가 몇 행 x 몇 열인지 확인
print(df.shape)

# 예를 들어
(100, 5)   # -> 100행 5열

# 주의
df.shape   # -> 함수가 아닌 속성이라 () 안 붙임


# 3. columns
# 어떤 열이 있는지 확인
print(df.columns)

# ex
Index(['이름', '나이', '점수'], dtype='object')

# 필요하면 리스트로 만들 수도 있음
print(df.columns.tolist())     # ['이름', '나이', '점수']


# 4. dtypes
# 각 열의 데이터 타입 확인
print(df.dtypes)

# ex
이름    object  
나이     int64
점수     int64
dtype: object

# 대략적으로...
object → 문자열
int64   → 정수
float64 → 실수
bool    → True/False


# 5. info()
# 위의 정보를 한 번에 보여줌
df.info()

# ex
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   이름     5 non-null      object
 1   나이     5 non-null      int64
 2   점수     5 non-null      int64

# 특히 중요한 게
Non-Null Count   # -> 결측치가 있는지도 바로 확인 가능


# 6. describe()
# 수치형 데이터의 통계 정보를 한 번에 확인
print(df.describe())

# 예를 들어 점수가 70, 80, 90, 60, 100이라면 아래 등이 나옴

count  -> 데이터 개수
mean   -> 평균
std    -> 표준편차
min    -> 최솟값
25%    -> 1사분위수
50%    -> 중앙값
75%    -> 3사분위수 
max    -> 최댓값

# 예를 들어 아래 코드처럼하면 점수 하나만 분석할 수도 있음
df["점수"].describe()


# 7. 결측치

# 예를 들어 이럴 때 여기서 None -> 결측치 => 값이 비어 있음
data = {
    "이름": ["민수", "지수", "철수", "영희"],
    "점수": [80, None, 90, 70]
}

df = pd.DataFrame(data)


# 8. isnull()
# 결측치인지 확인
print(df.isnull())

# 결과는 대략 이런식
# True가 결측치
    이름     점수
0  False  False
1  False   True
2  False  False
3  False  False

# 열별 결측치 개수
print(df.isnull().sum())    # 각 열에 빈 값이 몇 개 있는지 확인

# ex
이름    0      # 이름 -> 결측치 0개
점수    1      # 점수 -> 결측치 1개
dtype: int64


# 9. fillna()
# 결측치를 특정 값으로 채움 / 빈 값을 채움

# 예를 들어 점수의 빈 값을 0으로 채우려면
df["점수"] = df["점수"].fillna(0)
#결과    # 80
        # 0
        # 90
        # 70

# 평균으로 채우는 것도 가능
df["점수"] = df["점수"].fillna(df["점수"].mean())  # 빈 점수를 전체 점수 평균으로 채움


# 10. dropna()
# 결측치가 있는 행 자체를 삭제 / 빈 값이 있는 데이터를 삭제
df = df.dropna()

# 예를 들어 
민수 80
지수 NaN
철수 90
영희 70

df = df.dropna()  -> 민수 80
                     철수 90
                     영희 70