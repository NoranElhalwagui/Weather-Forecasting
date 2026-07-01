import pandas as pd
def preprocess(df):
    df = df.copy()

    df["date"] = pd.to_datetime(df["date"])

    #df.drop(columns=["precipitation_probability"], inplace=True)

    df.drop_duplicates(subset="date", inplace=True)

    df.sort_values("date", inplace=True)

    return df