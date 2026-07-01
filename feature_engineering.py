import pandas as pd

WEATHER_COLUMNS = [
    "temperature_2m",
    "relative_humidity_2m",
    "precipitation",
    "wind_speed_10m",
    "wind_direction_10m",
    "cloud_cover",
    "wind_gusts_10m",
    "visibility",
    "weather_code",
    "apparent_temperature",
    "dew_point_2m",
]


def add_time_features(df):
    df = df.copy()

    df["hour"] = df["date"].dt.hour
    df["day_of_week"] = df["date"].dt.dayofweek
    df["month"] = df["date"].dt.month
    df["day_of_year"] = df["date"].dt.dayofyear

    return df


def add_lag_features(df, lags=[1, 24]):
    df = df.copy()

    for col in WEATHER_COLUMNS:
        for lag in lags:
            df[f"{col}_lag_{lag}"] = df[col].shift(lag)

    return df


def add_rolling_features(df, window=24):
    df = df.copy()

    for col in WEATHER_COLUMNS:
        df[f"{col}_rolling_mean_{window}"] = (
            df[col]
            .rolling(window=window)
            .mean()
        )

    return df


def add_target(df, horizon=24):
    
    df = df.copy()

    df["temperature_target"] = df["temperature_2m"].shift(-horizon)

    return df


def create_features(df, horizon=24):
    df = df.copy()

    df = add_time_features(df)
    df = add_lag_features(df)
    df = add_rolling_features(df)
    df = add_target(df, horizon)
    df.dropna(inplace=True)

    return df