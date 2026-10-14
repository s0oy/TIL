# Decision Tree & Random Forest

# 1. 의사결정나무 (Decision Tree)
질문을 반복하면서 데이터를 분류하는 모델

# 예를 들어 합격 여부를 예측한다면 다음처럼 판단할 수 있음
- 공부 시간이 4시간 이상인가?
- 출석률이 80% 이상인가?
- 조건에 따라 합격 또는 불합격 예측

장점
- 구조를 이해하기 쉬움
- 데이터의 비선형적인 패턴도 학습 가능

단점
- 나무가 너무 깊어지면 학습 데이터에 과하게 맞춰지는 과적합 발생할 수 있음


# 2. 분류 코드
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

data = load_breast_cancer()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = DecisionTreeClassifier(     # DecisionTreeClassifier() -> 의사결정나무 분류 모델 생성
    max_depth=3,        # 나무의 최대 깊이를 3으로 제한
    random_state=42
)

model.fit(X_train, y_train)    # fit(X_train, y_train) -> 학습 데이터로 모델 학습

pred = model.predict(X_test)   # predict(X_test) -> 테스트 데이터의 클래스 예측

print("Accuracy:", accuracy_score(y_test, pred))
print(classification_report(y_test, pred))    # classification_report() -> Precision, Recall, F1 등 출력

# max_depth를 제한하면 나무가 지나치게 복잡해지는 것을 막는데 도움 됌
# 다만 너무 낮게 설정하면 중요한 패턴을 충분히 학습하지 못할 수도 있음


# 3. Random Forest
- 여러 개의 의사결정나무를 학습한 뒤, 각 나무의 예측을 모아 최종 결과를 만드는 모델
- 여러 나무의 판단을 종합하므로 단일 의사결정나무보다 안정적인 결과를 얻는 경우가 많음

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

model = RandomForestClassifier(
    n_estimators=100,    # 나무 100개 사용
    max_depth=5,         # 각 나무의 최대 깊이를 5로 제한
    random_state=42      # 실행할 때 결과를 재현하기 쉽게 설정
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred))
print(classification_report(y_test, pred))


# 4. 두 모델을 같은 데이터로 비교
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

models = {
    "Decision Tree": DecisionTreeClassifier(
        max_depth=3, random_state=42
    ),
    "Random Forest": RandomForestClassifier(
        n_estimators=100, max_depth=5, random_state=42
    )
}

for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)

    print(name)
    print("Accuracy:", accuracy_score(y_test, pred))
    print()

# 같은 학습 데이터와 테스트 데이터에서 두 모델의 정확도 비교 가능
# 어느 모델이 더 좋은지는 실행 결과와 데이터에 따라 달라지므로 미리 단정 XX


# 5. 비교
항목	  |       Decision Tree	     |        Random Forest
기본 원리 |	     하나의 나무로 판단	    |      여러 나무의 예측을 종합
해석	  |        비교적 쉬움	      |        상대적으로 어려움
과적합	  |  깊은 나무에서 발생하기 쉬움 |	    완화하는 경우가 많음
주요 설정 |	       max_depth	     |     n_estimators, max_depth
스케일링  |	     일반적으로 불필요	    |       일반적으로 불필요