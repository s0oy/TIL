# X / y -> Train / Test -> ML

# 전체 흐름
DataFrame
   ↓
X / y 분리
   ↓
train_test_split
   ↓
학습 데이터 / 테스트 데이터
   ↓
ML 모델
   ↓
fit()
   ↓
predict()
   ↓
평가


# 1. 데이터 준비
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {
    "공부시간": [2, 5, 4, 1, 6, 3, 5, 2],
    "출석률": [80, 95, 90, 70, 100, 85, 95, 75],
    "과제점수": [70, 90, 85, 60, 95, 80, 88, 65],
    "시험점수": [65, 92, 87, 55, 98, 78, 90, 60]
}

df = pd.DataFrame(data)

X = df[["공부시간", "출석률", "과제점수"]]
y = df["시험점수"]


# 2. Train / Test 분리
# Train : 모델이 공부하는 데이터
# Test : 공부하지 않은 데이터로 시험 보는 것

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
# 각 의미
# X_train : 학습할 입력 데이터
# X_test : 테스트할 입력 데이터
# y_train : 학습할 정답
# y_test : 테스트할 정답


# 3. 모델 만들기
# 가장 기본적인 선형회귀 사용
model = LinearRegression()   # -> 아직 모델이 공부한 건 아님


# 4. 학습
model.fit(X_train, y_train)

# X_train + y_train
#        ↓
#     model.fit()
#        ↓
# 모델이 패턴 학습


# 5. 예측
# 테스트 데이터를 모델에게 줌
pred = model.predict(X_test)

# 모델이 시험점수 예측
# X_test
#  ↓
# model.predict()
#  ↓
# 예측 시험점수


# 6. 실제값과 비교
print("실제값:", y_test.values)
print("예측값:", pred)

# 예를 들어 아래 값처럼 나옴
# 실제값 : [92 55]
# 예측값 : [89.7 61.2]


# 7. 평가
# 회귀에서는 대표적으로 MAE 많이 사용
from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(y_test, pred)

print("MAE:", mae)

# 예를 들어, MAE가 '3.5'라면 모델의 예측이 실제값과 평균적으로 약 3.5점 차이 남