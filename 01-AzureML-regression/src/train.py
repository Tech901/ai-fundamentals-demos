import argparse
import os
from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


def _resolve_csv(data_path: str) -> Path:
    p = Path(data_path)
    if p.is_file():
        return p

    # MLTable inputs are typically mounted as a folder; read the known CSV.
    known = p / "car-details-from-car-dehko.cleaned.csv"
    if known.exists():
        return known

    # Fallback: first CSV in the folder.
    csvs = sorted(p.glob("*.csv"))
    if csvs:
        return csvs[0]

    raise FileNotFoundError(f"No CSV found at: {data_path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, help="Path to MLTable folder or CSV file")
    parser.add_argument("--target", default="selling_price")
    args = parser.parse_args()

    csv_path = _resolve_csv(args.data)
    df = pd.read_csv(csv_path)

    # Basic cleanup
    df = df.dropna(subset=[args.target])

    y = df[args.target]

    # Keep the feature set simple and explainable for AI-900.
    feature_cols = ["year", "km_driven", "fuel", "seller_type", "transmission", "owner"]
    X = df[[c for c in feature_cols if c in df.columns]].copy()

    cat_cols = [c for c in ["fuel", "seller_type", "transmission", "owner"] if c in X.columns]
    num_cols = [c for c in ["year", "km_driven"] if c in X.columns]

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols),
        ],
        remainder="passthrough",  # numeric columns pass through
    )

    model = RandomForestRegressor(
        n_estimators=300,
        random_state=42,
        n_jobs=-1,
    )

    pipeline = Pipeline(steps=[("prep", preprocessor), ("model", model)])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    pipeline.fit(X_train, y_train)

    preds = pipeline.predict(X_test)
    rmse = mean_squared_error(y_test, preds, squared=False)
    r2 = r2_score(y_test, preds)

    print(f"CSV: {csv_path}")
    print(f"Rows: {len(df)}  Features: {list(X.columns)}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R2:   {r2:.4f}")

    out_dir = Path("outputs")
    out_dir.mkdir(exist_ok=True)
    joblib.dump(pipeline, out_dir / "model.joblib")


if __name__ == "__main__":
    main()
