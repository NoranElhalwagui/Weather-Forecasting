import joblib
import pandas as pd

from preprocessing import preprocess
from feature_engineering import create_features

def predict():
    model = joblib.load("models/xgboost_temperature.pkl")

    df = pd.read_csv("data/weather_history.csv")

    df = preprocess(df)

    df = create_features(df, horizon=24)


    latest = df.tail(24)

    X = latest.drop(columns=["date", "temperature_target"])

    predictions = model.predict(X)

    # Create output dataframe
    forecast = pd.DataFrame({
        "prediction_time": latest["date"] + pd.Timedelta(hours=24),
        "predicted_temperature": predictions
    })

    print(forecast)
    prediction_date = forecast["prediction_time"].iloc[0].strftime("%Y-%m-%d")

    forecast.to_csv(f"data/forecasts/{prediction_date}.csv",index=False)
if __name__ == "__main__":
    predict()