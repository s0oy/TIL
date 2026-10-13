# 모델 평가와 입계값

# 1. predict()와 predict_proba() 차이
predict() : 최종 분류 결과를 반환
predict_proba() : 각 클래스에 속할 확률을 반환

# 예를 들어 합격 여부를 예측하는 모델이 있다고 할 때
from sklearn.linear_model import LogisticRegression

X = [[1], [2], [3], [4], [5], [6]]
y = [0, 0, 0, 1, 1, 1]

model = LogisticRegression()
model.fit(X, y)

print(model.predict([[3.5]]))        # [0]
print(model.predict_proba([[3.5]]))  # [[0.6 0.4]]

# 실제 숫자는 학습된 모델에 따라 달라짐
# 여기서 [0.6, 0.4]라면 클래스 0일 확률이 60%, 클래스 1일 확률이 40%라는 뜻


# 2. 입계값 (Threshold)
일반적인 이진 분류에서는 양성 클래스의 예측 확률이 0.5 이상이면 1, 미만이면 0으로 분류
-> 이 기준을 임계값 

# 입계값을 직접 바꿀 경우 결과
import numpy as np

probabilities = np.array([0.2, 0.4, 0.55, 0.7, 0.9])

pred_05 = (probabilities >= 0.5).astype(int)
pred_07 = (probabilities >= 0.7).astype(int)

print("임계값 0.5:", pred_05)   # 임계값 0.5: [0 0 1 1 1]
print("임계값 0.7:", pred_07)   # 임계값 0.7: [0 0 0 1 1]

# 임계값을 높이면 1로 판정하는 기준이 더 엄격해짐
- 임계값 낮추면 : 더 많은 대상을 1로 분류하므로 Recall이 높아질 수 있지만, 오탐도 늘 수 있음
- 임계값 높이면 : 1로 분류하는 대상이 줄어 Precision이 높아질 수 있지만, 실제 양성을 놓칠 수 있음


# 3. Precision과 Recall 다시 이해하기

# 예를 들어 질병을 감지하는 모델이라고 할 때
- Precision : 질병이라고 예측한 사람 중 실제 환자의 비율
- Recall : 실제 환자 중 모델이 찾아낸 비율

# 질병을 놓치는 것이 특히 위험하다면 Recall이 중요할 수 있음
# 스팸 메일 분류에서 정상 메일을 스팸으로 잘못 분류하는 일을 줄이고 싶다면 Precision도 중요


# 4. 실전 코드 : 확률과 평가 지표 확인하기
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

data = load_breast_cancer()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=2000)
)

model.fit(X_train, y_train)

probabilities = model.predict_proba(X_test)[:, 1]

# 임계값을 0.5로 설정
predictions = (probabilities >= 0.5).astype(int)

print("Accuracy:", accuracy_score(y_test, predictions))
print("Precision:", precision_score(y_test, predictions))
print("Recall:", recall_score(y_test, predictions))
print("F1:", f1_score(y_test, predictions))

# 위 코드에서 [:, 1]은 각 데이터가 클래스 1에 속할 확률만 가져온다는 뜻
# 이 데이터셋에서는 클래스 1이 악성인지 양성인지 의미를 확인하려면 data.target_names도 출력해 봐야 함
# 이 예제에선 클래스 1이 benign이므로 Recall은 양성(benign) 클래스를 찾아내는 비율을 뜻함