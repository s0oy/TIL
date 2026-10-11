# 모델 학습 원리와 성능 개선

# 1. 가중치와 편향 (Weight & Bias)
# ML 모델은 입력 데이터와 학습 가능한 값을 이용해 예측
hat{y} = wx + b

- x : 입력 데이터
- w : 가중치 (Weight)
- b : 편향 (Bias)
- hat{y} : 모델이 예측한 값

# 예를 들어 공부시간으로 시험점수를 예측한다고 할 때
hat{y} = 10x + 40
# 공부시간이 3시간이라면 예측 점수는 다음과 같음
hat{y} = 10 * 3 + 40 = 70

# 여기서 가중치 w = 10은 공부시간이 1시간 늘어날 때 예측점수가 얼마나 변하는지 나타냄
# 편향 b = 40은 입력값이 0일 때의 예측값


# 2. 손실 함수 (Loss Function)
모델의 예측이 실제 정답과 얼마나 다른지 수치로 나타내는 함수
# 예측 오차를 제곱해 평균 내기 때문에 큰 오차에 더 큰 페널티 줌

# 예를 들어 실제 시험점수가 80점인데 모델이 70점이라고 예측한다면 오차는 -10점

일반적으로 모델을 학습할 때는 이 손실을 줄이는 방향으로 가중치와 편향 조정


# 3. 경사하강법 (Gradient Descent)
- 손실 함수가 작아지는 방향으로 가중치와 편향을 조금씩 수정하는 최적화 방법
- 현재 위치에서 경사가 내려가는 방향을 찾아 조금 이동하고 이 과정을 반복해 낮은 지점을 찾아가는 것

# 학습 과정
1. 가중치와 편향 초기화
2. 현재 가중치로 예측
3. 예측값과 실제값으로 손실 계산
4. 손실이 줄어드는 방향 계산
5. 가중치와 편향 수정
6. 손실이 줄어들 때까지 반복

# Python으로 직접 구현

# 이 데이터는 y = 2x + 1 관계를 가지고 있음
# 학습이 잘 진행되면 가중치는 약 2, 편향은 약 1에 가까워지고, x = 6일 때 예측값은 13에 가까워짐
import numpy as np

# 입력 데이터와 정답
X = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([3, 5, 7, 9, 11], dtype=float)

# 초기 가중치와 편향
w = 0.0
b = 0.0

learning_rate = 0.01   # 한 번에 얼마나 크게 수정할지 
epochs = 1000          # 전체 데이터를 사용해 업데이트하는 반복 횟수

for epoch in range(epochs):
    # 예측  
    pred = w * X + b    # pred : 현재 모델의 예측값

    # MSE 손실의 미분값
    dw = (2 / len(X)) * np.sum((pred - y) * X)   # dw : 가중치에 대한 손실의 미분값
    db = (2 / len(X)) * np.sum(pred - y)         # db : 편향에 대한 손실의 미분값

    # 가중치와 편향 업데이트
    w -= learning_rate * dw    # 가중치 수정
    b -= learning_rate * db

print("가중치:", w)
print("편향:", b)
print("예측값:", w * 6 + b)


# 4. 학습률 (Learning Rate)
가중치와 편향을 1번 업데이트할 때 얼마나 크게 이동할지 결정하는 값

# 경사하강법에서 learning_rate로 성정
학습률 너무 작음 -> 손실이 줄어드는 속도가 느릴 수 있음
학습률 적절 -> 비교적 안정적으로 손실 줄일 수 있음
학습률 너무 큼 -> 최적점을 지나치거나 손실이 진동·발산할 수 있음


# 5. 정규화 (Regularization)
모델이 지나치게 복잡해지는 것을 억제해 과적합을 줄이는 방법

# Ridge Regression (L2 정규화)
가중치의 제곱을 페널티로 추가

- 가중치가 지나치게 커지는 것을 억제
- 가중치를 정확히 0으로 만드는 것이 목적 X
- alpha가 커지면 일반적으로 정규화의 영향이 강해짐

from sklearn.linear_model import Ridge

model = Ridge(alpha=1.0)
model.fit(X_train, y_train)

pred = model.predict(X_test)

# Lasso Regression (L1 정규화)
가중치의 절댓값을 페널티로 추가

- 일부 가중치를 정확히 0으로 만들 수 있음
- 특성 선택 효과가 나타날 수 있음
- 특성이 많을 때 유용할 수 있지만 항상 Ridge보다 좋은 것은 아님

from sklearn.linear_model import Lasso

model = Lasso(alpha=0.1, max_iter=10000)
model.fit(X_train, y_train)

pred = model.predict(X_test)