from datetime import timedelta
from fetcher import fetch_weather
from preprocessing import preprocess
import pandas as pd


def update_weather_data():
    # Read existing data
    old_df = pd.read_csv("data/weather_hourly.csv")
    old_df["date"] = pd.to_datetime(old_df["date"])

    # Find the last recorded day
    last_day = old_df["date"].max().date()

    # Download the next day
    download_day = last_day + timedelta(days=1)
    new_date = download_day.strftime("%Y-%m-%d")

    new_df = fetch_weather(new_date, new_date)

    new_df = preprocess(new_df)

    updated_df = pd.concat([old_df, new_df], ignore_index=True)

    
    print(f"Added weather data for {new_date}")