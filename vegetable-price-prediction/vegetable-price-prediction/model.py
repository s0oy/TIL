from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# 1. 파일 경로 설정
BASE_DIR = Path(__file__).resolve().parent

OUTPUT_DIR = BASE_DIR / "results"
OUTPUT_DIR.mkdir(exist_ok=True)

# 2. 작물별로 두 지역 데이터 불러오기 + 병합
def load_data(crop):
    # crop이 cabbage면 배추 파일, radish면 무 파일 읽음
    daegwallyeong = pd.read_csv(
        BASE_DIR / f"{crop}_daegwallyeong.csv",
        parse_dates=["date"]
    )

    jeju = pd.read_csv(
        BASE_DIR / f"{crop}_jeju.csv",
        parse_dates=["date"]
    )

    # 날짜 중복 확인
    for name, df in [
        ("대관령", daegwallyeong),
        ("제주", jeju)
    ]:
        if df["date"].isna().any():
            raise ValueError(f"{crop} {name}: 날짜에 빈 값이 있습니다.")

        if df["date"].duplicated().any():
            raise ValueError(f"{crop} {name}: 날짜가 중복되어 있습니다.")

    # 지역을 구분할 수 있도록 컬럼 이름 변경
    daegwallyeong = daegwallyeong.rename(
        columns={
            "temp": "temp_daegwallyeong",
            "rain": "rain_daegwallyeong"
        }
    )

    jeju = jeju.rename(
        columns={
            "temp": "temp_jeju",
            "rain": "rain_jeju"
        }
    )

    # 어느 한 지역에만 있는 날짜도 유지
    df = pd.merge(
        daegwallyeong,
        jeju,
        on="date",
        how="outer",
        suffixes=("_d", "_j"),
        validate="one_to_one"
    )

    # 두 파일에 모두 가격이 있는 날짜
    common = df["price_d"].notna() & df["price_j"].notna()

    # 같은 날짜의 가격이 서로 다른지 확인
    if not df.loc[common, "price_d"].eq(
        df.loc[common, "price_j"]
    ).all():
        raise ValueError(f"{crop}: 두 지역 파일의 가격이 다릅니다.")

    # 대관령 파일에 가격이 없으면 제주 파일 가격 사용
    df["price"] = df["price_d"].combine_first(df["price_j"])

    # 중복 가격 컬럼 제거
    df = df.drop(columns=["price_d", "price_j"])

    # 날짜순으로 정렬
    df = df.sort_values("date").reset_index(drop=True)

    return df

# 3. 예측에 사용할 변수와 정답 만들기
def make_features(df):
    df = df.copy()

    # 오늘 정보를 이용해 예측할 다음 관측일과 가격
    # 기상 결측 행을 삭제하기 전에 정답 만들어야 함
    df["target_date"] = df["date"].shift(-1)
    df["target_price"] = df["price"].shift(-1)

    # 직전 관측일 가격
    df["price_previous"] = df["price"].shift(1)

    # 현재 가격을 포함한 최근 3개·7개 관측 가격 평균
    df["price_mean_3obs"] = df["price"].rolling(3).mean()
    df["price_mean_7obs"] = df["price"].rolling(7).mean()

    # 직전 관측 가격 대비 변화율
    df["price_change"] = df["price"].pct_change(fill_method=None)

    return df

# 4. 작물 하나를 학습하고 평가하는 함수
def run_model(crop):
    df = load_data(crop)
    df = make_features(df)

    # 가격 관련 변수
    price_features = [
        "price",
        "price_previous",
        "price_mean_3obs",
        "price_mean_7obs",
        "price_change"
    ]

    # 대관령 날씨
    daegwallyeong_features = [
        "temp_daegwallyeong",
        "rain_daegwallyeong"
    ]

    # 제주 날씨
    jeju_features = [
        "temp_jeju",
        "rain_jeju"
    ]

    all_features = (price_features + daegwallyeong_features + jeju_features)

    # 모든 모델을 같은 날짜로 비교하기 위해
    # 필요한 값이 모두 있는 행만 사용
    df = df.dropna(
        subset=all_features + ["target_date", "target_price"]
    ).reset_index(drop=True)

    # 예측 대상 날짜를 기준으로 학습·시험 구분
    train = df[df["target_date"] < "2026-07-01"].copy()
    test = df[df["target_date"] >= "2026-07-01"].copy()

    if train.empty or test.empty:
        raise ValueError("학습 또는 시험 데이터가 없습니다.")

    y_train = train["target_price"]
    y_test = test["target_price"]

    print(f"\n===== {crop.upper()} =====")
    print(f"학습 데이터: {len(train)}개")
    print(f"시험 데이터: {len(test)}개")

    # 예측 결과 저장용
    predictions = test[["date", "target_date", "target_price"]].copy()

    # 5. 기준 방법 : 다음 가격도 오늘과 같다고 예측
    baseline_pred = test["price"]

    baseline_mae = mean_absolute_error(
        y_test,
        baseline_pred
    )

    predictions["baseline"] = baseline_pred

    scores = [{
        "crop": crop,
        "model": "baseline",
        "mae": baseline_mae
    }]

    # 6. 입력 변수를 달리해서 비교
    feature_sets = {
        "price_only": price_features,
        "price_daegwallyeong": (price_features + daegwallyeong_features),
        "price_jeju": (price_features + jeju_features),
        "price_both_regions": all_features
    }

    for model_name, features in feature_sets.items():
        X_train = train[features]
        X_test = test[features]

        model = RandomForestRegressor(
            n_estimators=100,
            random_state=42,
            n_jobs=-1
        )

        model.fit(X_train, y_train)

        pred = model.predict(X_test)

        mae = mean_absolute_error(y_test, pred)

        scores.append({
            "crop": crop,
            "model": model_name,
            "mae": mae
        })

        predictions[model_name] = pred

        # 두 지역 날씨를 모두 사용한 모델의 중요도 저장
        if model_name == "price_both_regions":
            importance = pd.DataFrame({
                "feature": features,
                "importance": model.feature_importances_
            }).sort_values("importance", ascending=False)

            fig, ax = plt.subplots(figsize=(9, 5))

            ax.barh(
                importance["feature"],
                importance["importance"]
            )

            ax.invert_yaxis()
            ax.set_title(f"{crop.title()}: Feature Importance")
            ax.set_xlabel("Importance")

            fig.tight_layout()

            fig.savefig(
                OUTPUT_DIR / f"{crop}_importance.png",
                dpi=150
            )

            plt.close(fig)

    # 7. 모델별 오차 출력
    scores_df = pd.DataFrame(scores)

    print("\n모델별 평균 절대 오차(MAE)")
    print(
        scores_df[["model", "mae"]].to_string(
            index=False,
            float_format=lambda value: f"{value:,.1f}"
        )
    )

    # 8. 실제값과 예측값 그래프
    fig, ax = plt.subplots(figsize=(12, 5))

    ax.plot(
        test["target_date"],
        y_test,
        label="Actual"
    )

    ax.plot(
        test["target_date"],
        baseline_pred,
        label="Baseline",
        alpha=0.7
    )

    ax.plot(
        test["target_date"],
        predictions["price_both_regions"],
        label="RandomForest: Both Regions"
    )

    ax.set_title(f"{crop.title()}: Next Observed Price")
    ax.set_xlabel("Target Date")
    ax.set_ylabel("Price (source units)")
    ax.legend()
    ax.grid(alpha=0.3)

    fig.tight_layout()

    fig.savefig(
        OUTPUT_DIR / f"{crop}_result.png",
        dpi=150
    )

    plt.close(fig)

    return scores_df

# 10. 배추·무 순서대로 실행
if __name__ == "__main__":

    for crop in ["cabbage", "radish"]:
        run_model(crop)

    print("\n완료! results 폴더를 확인하세요.")