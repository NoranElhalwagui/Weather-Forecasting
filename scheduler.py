import os
import time
import schedule

from datetime import datetime, date

from update_weather import update_weather_data
from predict import predict
from train import train_model


TRAIN_FILE = "models/last_training.txt"


def should_retrain(days=5):
    #Return True if the model should be retrained.

    if not os.path.exists(TRAIN_FILE):
        return True

    with open(TRAIN_FILE, "r") as f:
        last_train = date.fromisoformat(f.read().strip())

    return (date.today() - last_train).days >= days


def update_training_date():
    #Save today's date after training.
    with open(TRAIN_FILE, "w") as f:
        f.write(date.today().isoformat())


def daily_job():

    print(f"\n[{datetime.now()}] Starting daily update...")

    update_weather_data()

    predict()

    if should_retrain():
        print("Retraining model...")
        train_model()
        update_training_date()

    print("Daily job finished.\n")


schedule.every().day.at("01:00").do(daily_job)

print("Scheduler started...")

if __name__ == "__main__":
    daily_job()      

    while True:
        schedule.run_pending()
        time.sleep(60)