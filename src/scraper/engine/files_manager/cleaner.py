import pandas as pd


def clean_data_frame(df: pd.DataFrame):
    df.dropna(inplace=True)
    df['price'] = df['price'].astype(float)
    df['likes'] = df['likes'].astype(int)
    df['id'] = df['id'].astype(int)
