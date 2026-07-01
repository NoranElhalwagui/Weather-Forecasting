# Weather Forecasting Service

A machine learning service that predicts the next 24 hours of temperature using historical weather data from the Open-Meteo API and an XGBoost regression model.

---

## Features

- Fetches historical weather data from Open-Meteo
- Automatically updates the dataset every day
- Preprocesses newly collected data
- Performs feature engineering for time-series forecasting
- Trains an XGBoost model
- Predicts the next 24 hours of temperature
- Saves daily forecasts as CSV files
- Automatically retrains the model every 5 days

---

## Project Structure

```
Weather-Forecasting/
│
├── data/
│   ├── weather_hourly.csv
│   └── forecasts/
│
├── models/
│   └── xgboost_temperature.pkl
│
├── fetcher.py
├── updater.py
├── preprocessing.py
├── feature_engineering.py
├── train.py
├── predict.py
├── scheduler.py
│
└── README.md
```

---

## Dataset

Weather data is collected using the Open-Meteo Historical Forecast API.

Collected features include:

- Temperature
- Relative Humidity
- Precipitation
- Wind Speed
- Wind Direction
- Cloud Cover
- Wind Gusts
- Visibility
- Weather Code
- Apparent Temperature
- Dew Point

Location:
- Latitude: 29.9792
- Longitude: 31.1342

---

## Feature Engineering

The following features are generated before training:

- Hour of day
- Day of week
- Month
- Cyclical encoding (Hour, Month)
- 1-hour lag
- 24-hour lag
- 24-hour rolling mean

Target:

- Temperature 24 hours ahead

---

## Model

Algorithm:

- XGBoost Regressor

Why XGBoost?

- Excellent performance on tabular data
- Fast training
- Handles nonlinear relationships
- Works well with engineered features

---

## Model Performance

| Metric | Value |
|---------|------:|
| Training MAE | 0.716°C |
| Training RMSE | 0.958°C |
| Training R² | 0.985 |
| Test MAE | 1.273°C |
| Test RMSE | 1.782°C |
| Test R² | 0.929 |

---

## Workflow

```
Historical API
      │
      ▼
Fetch weather
      │
      ▼
Update CSV
      │
      ▼
Preprocessing
      │
      ▼
Feature Engineering
      │
      ▼
Train XGBoost
      │
      ▼
Predict next 24 hours
      │
      ▼
Save forecast
```

---

## Installation

```bash
git clone <repository-url>

cd Weather-Forecasting

pip install -r requirements.txt
```

---

## Running

### Download historical data

```bash
python fetcher.py
```

### Train the model

```bash
python train.py
```

### Predict

```bash
python predict.py
```

### Run scheduler

```bash
python scheduler.py
```

---

## Future Improvements

- FastAPI deployment
- Hyperparameter tuning
- Multi-variable forecasting
- Docker support
- CI/CD pipeline
- Visualization dashboard

---

## Technologies

- Python
- Pandas
- XGBoost
- Scikit-learn
- Joblib
- Open-Meteo API
- Schedule
