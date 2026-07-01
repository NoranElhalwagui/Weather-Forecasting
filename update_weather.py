from datetime import date, timedelta
from fetcher import fetch_weather
from preprocessing import preprocess
import pandas as pd

TRAIN_FILE = "models/last_training.txt"

def update_weather_data():
    # Read existing data
    old_df = pd.read_csv("data/weather_history.csv")
    old_df["date"] = pd.to_datetime(old_df["date"])

    with open(TRAIN_FILE, "w") as f:
        f.write(date.today().isoformat())
    # Find the last recorded day
    last_day = old_df["date"].max().date()

    # Download the next day
    download_day = last_day + timedelta(days=1)
    new_date = download_day.strftime("%Y-%m-%d")

    new_df = fetch_weather(new_date, new_date)

    new_df = preprocess(new_df)

    updated_df = pd.concat([old_df, new_df], ignore_index=True)

    
    print(f"Added weather data for {new_date}")