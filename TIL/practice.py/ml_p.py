# ML 기초

# 1. ML 기본 구조
1. 데이터 준비
   - Pandas로 데이터 정리
2. X와 y 분리
   - 입력 특성과 예측할 정답 구분
3. 학습 및 예측
   - train_test_split -> fit -> predict
4. 성능 평가
   - 예측값과 실제값 비교


# 2. 회귀와 분류의 차이
- 회귀 (Regression)
  - 숫자 값 예측
    - 농산물 가격 예측
    - 주택 가격 예측
    - 기온 예측
  - 대표 모델
    - LinearRegression
    - RandomForestRegressor

- 분류 (Classification)
  - 정해진 범주 예측
    - 합격 / 불합격
    - 정상 / 불량
    - 사과 / 배 / 포도
  - 대표 모델
    - LogisticRegression
    - DecisionTreeClassifier
    - RandomForestClassifier


# 3. 데이터 분리 - X, y, train/test
- X : 모델에 입력할 특성(Feature)
- y : 모델이 예측할 정답(Target)
- X_train, y_train : 학습용 데이터
- X_test, y_test : 평가용 데이터
- train_test_split() : 학습 데이터와 테스트 데이터 분리

from sklearn.model_selection import train_test_split

X = df[["공부시간", "출석률", "과제점수"]]
y = df["시험점수"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# 4. 회귀 모델 2개 비교하기
- models : 여러 모델을 이름과 함께 저장한 딕셔너리
- for name, model in models.items() : 모델을 하나씩 꺼내 반복
- n_estimators=100 : 랜덤 포레스트에 사용할 트리 개수
- model.fit() : 해당 모델 학습
- model.predict() : 테스트 데이터 예측

- LinearRegression : 입력 특성과 정답 사이의 관계를 선형식으로 표현
            기준 모델로 사용하기 좋고 해석도 비교적 쉬움

- RandomForest : 여러 결정 트리의 예측 결합
                 복잡한 관계도 학습할 수 있지만 데이터가 적거나 특성이 부적절하면 성능 좋지 않을 수도 있음

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

models = {
    "LinearRegression": LinearRegression(),
    "RandomForest": RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )
}

for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)

    print(f"\n{name}")
    print("MAE:", mean_absolute_error(y_test, pred))
    print("MSE:", mean_squared_error(y_test, pred))
    print("R2:", r2_score(y_test, pred))


# 5. 분류 모델 만들기
# 합격 여부 예측한다고 할 때
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
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
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y    # 학습용과 테스트용 데이터에 각 클래스가 가능한 한 비슷한 비율로 들어가게 도와줌
                  # 다만 데이터가 너무 적거나 특정 클래스가 극소수라면 분할에 실패할 수 있음
)

model = DecisionTreeClassifier(max_depth=3, random_state=42)   # max_depth=3 -> 결정 트리의 최대 깊이 제한
                                                               #                트리가 너무 복잡해지는 것을 막기 위한 설정 중 하나
model.fit(X_train, y_train)

pred = model.predict(X_test)

print("예측:", pred)
print("실제:", y_test.to_list())
print("Accuracy:", accuracy_score(y_test, pred))
print(classification_report(y_test, pred, zero_division=0))


# 6. 분류 지표
# 정답이 특정 카테고리인 경우 사용
- Accuracy (정확도) : 전체 데이터 중 모델이 올바르게 예측한 비율
                   데이터 클래스가 불균형할 경우 성능을 왜곡할 수 있음
- Precision (정밀도) : 모델이 양성이라고 예측한 것 중 실제 양성 비율
- Recall (재현율) : 실제 양성인것 중 모델이 양성으로 올바르게 예측한 비율
- F1-score : Precision과 Recall의 조화평균
           두 지표의 균형을 볼 때 사용
- Confusion Matrix (오차 행렬) : 실제값과 예측값의 조합을 4가지로 나타낸 표
- ROC-AUC : 거짓 긍정 비율 대비 참 긍정 비율의 변화를 나타낸 곡선 아래의 면적
            1에 가까울수록 성능이 뛰어남


# 7. 회귀 지표
# 정답이 연속적인 숫자인 경우 사용 (낮을수록 좋음)
- MAE(Mean Absolute Error): 실제값과 예측값의 차이의 절댓값 평균
- MSE(Mean Squared Error) : 실제값과 예측값 차이를 제곱해서 평균한 값
                            큰 오차에 더 큰 페널티를 줌
- R² Score (결정계수) : 모델이 데이터의 분산을 얼마나 잘 설명하는지 나타내며 1에 가까울수록 좋음
- RMSE(Root MSE) : MSE에 루트를 씌워 원래 데이터 단위와 일치시킨 값


# 8. Scaling
- 특성마다 값의 범위가 크게 다를 때 범위를 조정하는 작업
- KNN, SVM, Logistic Regression, 신경망 등에서 중요
- Decision Tree, Random Forest는 일반적으로 스케일링이 필요하지 않음

# 8-1. StandardScaler
# 평균을 0, 표준편차를 1로 변환
# 주의 : 훈련 데이터 -> fit_transform() 적용, 테스트 데이터 -> transform()만 적용

- fit() : 데이터의 평균과 표준편차 등을 학습
- transform() : 학습한 기준으로 데이터 변환
- fit_transform() : 학습과 변환을 한 번에 수행

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 8-2. MinMaxScaler
# 데이터를 일반적으로 0 ~ 1 범위로 변환
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# 9. 과적합과 과소적합
- 과적합(Overfitting) : 훈련 데이터를 지나치게 학습해 새로운 데이터의 예측 성능이 떨어지는 현상
- 과소적합(Underfitting) : 데이터의 패턴을 충분히 학습하지 못한 상태
- 일반화(Generalization) : 학습에 사용하지 않은 새로운 데이터에서도 예측을 잘하는 능력

# 과적합 확인하기
from sklearn.metrics import mean_squared_error

train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

print("훈련 MSE:", mean_squared_error(y_train, train_pred))
print("테스트 MSE:", mean_squared_error(y_test, test_pred))

# 회귀 문제에서 MSE가 낮을수록 오차 작음
- 훈련 MSE는 낮고 테스트 MSE는 높음 -> 과적합 의심
- 훈련 MSE와 테스트 MSE 모두 높음 -> 과소적합 가능성

# 과적합을 줄이는 방법
- 모델 복잡도 줄이기
- 학습 데이터 늘리기
- 정규화 적용하기
- 교차 검증으로 성능 확인하기
- 결정 트리의 max_depth 제한하기


# 10. 교차 검증 (Cross-validation)
- 데이터를 여러 부분으로 나누어 모델을 반복 평가하는 방법
- 데이터 분할 1번에 따른 평가 결과의 영향 줄일 수 있음
- 대표적인 방법 : K-Fold Cross-validation

# 5-Fold 교차 검증
# 데이터를 5개로 나누고 매번 하나를 검증용으로 사용하며 나머지 4개로 학습 -> 총 5번 평가한 점수 확인
# 주의 : 교차 검증은 훈련 데이터 안에서 수행하고 테스트 데이터는 최종평가를 위해 남겨 둠

- cv=5 : 5-Fold 교차 검증
- scoring : 사용할 평가 지표
- scores : 각 회차의 평가 점수

from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(random_state=42)

scores = cross_val_score(
    model,
    X_train,
    y_train,
    cv=5,
    scoring="neg_mean_squared_error"  # neg_mean_squared_error -> sklearn의 점수 규칙상 음수로 반환
                                      #                           양수 MSE로 확인하려면 부호 바꿔 줌
)

mse_scores = -scores

print("각 회차 MSE:", mse_scores)
print("평균 MSE:", mse_scores.mean())


# 11. 데이터 누수 (Data Leakage)
- 학습 과정에 예측 시점에는 알 수 없는 정보가 들어가는 문제
- 평가 점수는 높게 나오지만 실제 환경에서는 성능이 떨어질 수 있음

# 잘못된 예시
# 테스트 데이터의 정보끼리 스케일링 기준 계산에 사용했기 때문에 누수위험 O

# 전체 데이터로 스케일링 기준을 학습
X_scaled = scaler.fit_transform(X)
# 그 후에 훈련 데이터와 테스트 데이터 분리

# 올바른 순서
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 데이터 누수의 다른 예시
- 정답값 자체를 입력 특성에 포함함
- 미래의 정보를 이용해 과거를 예측함
- 전체 데이터로 결측값 대체 기준을 계산한 뒤 분리함
- 테스트 데이터의 결과를 반복적으로 확인하면서 모델 조정함

핵심 : 테스트 데이터의 정보를 모델 학습이나 전처리 기준 결정에 사용하지 않는 것


# 12. Pipeline
- 전처리와 모델 학습을 하나로 연결하는 기능
- 전처리 순서를 관리하기 편리함
- 교차 검증에서 각 훈련 부분에 맞춰 전처리를 수행할 수 있어 데이터 누수 위험을 줄이는데 도움 됨

# 예제 코드
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LinearRegression())
])

pipe.fit(X_train, y_train)

pred = pipe.predict(X_test)

# 동작 방식
pipe.fit(X_train, y_train) : 훈련 데이터의 스케일링 기준 학습
                             훈련 데이터 변환
                             변환된 데이터로 모델 학습
pipe.predict(X_test) : 학습한 스케일링 기준으로 테스트 데이터 변환
                       변환된 데이터로 예측

# 교차 검증과 함께 사용하기
# Pipeline을 교차 검증과 함께 사용하면 각 회차에서 훈련용 데이터만으로 전처리 학습할 수 있음
scores = cross_val_score(
    pipe,
    X_train,
    y_train,
    cv=5,
    scoring="r2"
)

print("각 회차 R²:", scores)
print("평균 R²:", scores.mean())