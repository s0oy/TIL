# Logistic Regression

# 1. 로지스틱 회귀?
주로 분류(Classification)에 사용하는 모델
특정 Class에 속할 확률을 계산해 분류

# 예를 들어
- 합격 / 불합격
- 정상 / 불량
- 스팸 / 정상 메일 


# 2. 시그모이드 함수
로지스틱 회귀는 선형 계산 결과를 0 ~ 1 사이 값으로 변환

z = (w1*x1 + w2*x2 + ... + b)
- 결과가 0.9라면 양성 클래스일 가능성이 높다고 판단
- 결과가 0.2라면 양성 클래스일 가능성이 낮다고 판단

# 이진 분류에서는 기본적으로 0.5를 기준으로 클래스를 나누는 경우가 많음


# 3. Python으로 분류 모델 만들기
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

data = {
    "공부시간": [1, 2, 3, 4, 5, 6, 2, 5, 3, 6],
    "출석률": [60, 70, 80, 85, 90, 95, 75, 98, 88, 100],
    "합격": [0, 0, 0, 1, 1, 1, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["공부시간", "출석률"]]
y = df["합격"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

model = LogisticRegression(max_iter=1000)     # LogisticRegression() -> 분류 모델 생성
                                              # max_iter=1000 -> 최적화 반복 횟수의 상한

model.fit(X_train, y_train)   # fit(X_train, y_train) -> 모델 학습

pred = model.predict(X_test)   # predict(X_test) -> 클래스 예측

print("예측:", pred)
print("실제:", y_test.to_list())
print("Accuracy:", accuracy_score(y_test, pred))   # accuracy_score() -> 정확도 계산
print(classification_report(y_test, pred, zero_division=0))


# 4. 예측값과 예측 확률 비교
print("클래스:", model.predict(X_test))       # predict() -> 예측 클래스 반환
print("확률:", model.predict_proba(X_test))   # predict_proba -> 각 클래스의 예측 확률 반환

# 예를 들어
이진분류에서 한 데이터의 확률이 [0.2, 0.8]이라면 클래스 0의 확률은 0.2, 클래스 1의 확률은 0.8


# 5. 로지스틱 회귀와 결정 트리
로지스틱 회귀 : 기본적으로 선형 결정 경계 학습
결정 트리 : 여러 조건을 이용해 데이터 분리

항목	   |   Logistic Regression	|     Decision Tree
방식	   |    확률 기반 선형 분류	   |    조건에 따른 분기
스케일링    |      대체로 권장	      |       보통 불필요
복잡한 패턴	|   기본적으로 선형 경계	|  비선형 패턴도 학습 가능
주요 설정	|     C, max_iter	    |  max_depth, min_samples_leaf


# 6. 분류 모델의 손실 함수
로지스틱 회귀는 보통 Log Loss (로스 손실) 사용
이진 분류에선 Binary Cross-Entropy라고도 불림

정답이 1인 데이터에 모델이 0.99의 확률을 부여하면 좋은 예측이지만, 0.01의 확률을 부여하면 큰 손실 발생
-> 모델은 정답 클래스에 높은 확률을 부여하도록 학습


# 7. 스케일링과 Pipeline
- 로지스틱 회귀는 입력 특성의 스케일에 영향을 받기 때문에 스케일링을 함께 사용하는 경우가 많음
- Pipeline을 사용하면 훈련 데이터에 맞춰 스케일링하고 모델을 학습한 뒤 
  테스트 데이터에도 동일한 변환을 적용해 예측 가능

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(max_iter=1000))
])

pipe.fit(X_train, y_train)

pred = pipe.predict(X_test)