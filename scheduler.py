import schedule
import time

from update_weather import update_weather_data
from preprocessing import preprocess
import pandas as pd


def daily_job():
    print("Starting daily update...")

    # Update raw weather data
    update_weather_data()
    # Preprocess the updated dataset
    df = pd.read_csv("data/weather_hourly.csv")
    #df = preprocess(df)
    df.to_csv("data/weather_hourly_processed.csv", index=False)

    print("Daily update completed.")


# Run every day at 10:00 AM
schedule.every().day.at("10:00").do(daily_job)

print("Scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(60)