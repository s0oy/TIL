# ML 기초 실습

# 1. ML 기본 구조
1. 데이터 준비
   - Pandas로 데이터 정리
2. X와 y 분리
   - 입력 특성과 예측할 정답 구분
3. 학습 및 예측
   - train_test_split -> fit -> predict
4. 성능 평가
   - 예측값과 실제값 비교


# 2. 전체 코드 이해하기
# 예제 : 공부시간, 출석률, 과제점수를 이용해 시험점수를 예측하는 회귀모델
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

data = {
    "공부시간": [2, 5, 4, 1, 6, 3, 5, 2, 4, 6],
    "출석률": [80, 95, 90, 70, 100, 85, 95, 75, 90, 98],
    "과제점수": [70, 90, 85, 60, 95, 80, 88, 65, 87, 96],
    "시험점수": [65, 92, 87, 55, 98, 78, 90, 60, 86, 97]
}

df = pd.DataFrame(data)

# 입력 데이터와 정답 분리
X = df[["공부시간", "출석률", "과제점수"]]   # X -> 예측에 사용할 입력 특성
y = df["시험점수"]                         # y -> 예측할 정답

# 학습용과 테스트용 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(    # train_test_split() -> 학습 데이터와 테스트 데이터 분리
    X, y, test_size=0.2, random_state=42   # test_size = 0.2 -> 데이터의 약 20% 테스트에 사용
                                           # random_state = 42 -> 실행할 때마다 같은 방식으로 분리되도록 난수 고정
)

# 모델 생성 및 학습
model = LinearRegression()
model.fit(X_train, y_train)    # model.fit() -> 학습 데이터로 모델 훈련

# 예측
pred = model.predict(X_test)   # model.predict() -> 입력 데이터의 예측값 생성

# 평가
mae = mean_absolute_error(y_test, pred)   # mean_absolute_error() -> 예측값과 실제값의 평균 절대 차이 계산

print("실제 점수:", y_test.to_list())
print("예측 점수:", pred)
print("평균 절대 오차:", mae)


# 3. 평가 지표 기초
- MAE : 실제값과 예측값의 절대 차이를 평균한 값, 작을수록 좋음
- MSE : 차이를 제곱한 뒤 평균한 값, 큰 오차에 더 큰 벌점을 줌
- R² : 모델이 데이터의 변동을 얼마나 설명하는지 나타내는 지표,
       일반적으로 1에 가까울수록 좋지만 테스트 데이터에서는 음수가 나올 수도 있음

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

print("MAE:", mean_absolute_error(y_test, pred))
print("MSE:", mean_squared_error(y_test, pred))
print("R²:", r2_score(y_test, pred))