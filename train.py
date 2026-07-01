import pandas as pd
import joblib
from preprocessing import preprocess
from feature_engineering import create_features
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)
import numpy as np

df = pd.read_csv("data/weather_history.csv")

df = preprocess(df)
df = create_features(df, horizon=24)
X = df.drop(columns=["date", "temperature_target"])
y = df["temperature_target"]

split = int(len(df) * 0.8)

X_train = X.iloc[:split]
X_test = X.iloc[split:]

y_train = y.iloc[:split]
y_test = y.iloc[split:]

from xgboost import XGBRegressor

model = XGBRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_train_pred = model.predict(X_train)
#training error
train_mae = mean_absolute_error(y_train, y_train_pred)
train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
train_r2 = r2_score(y_train, y_train_pred)
#test error
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"Training MAE : {train_mae:.3f} °C")
print(f"Training RMSE: {train_rmse:.3f} °C")
print(f"Training R²  : {train_r2:.4f}")
print(f"-------------------------------")
print(f"Test MAE : {mae:.3f} °C")
print(f"Test RMSE: {rmse:.3f} °C")
print(f"Test R²  : {r2:.4f}")
#joblib.dump(model, "models/xgboost_temperature.pkl")