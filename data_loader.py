import yfinance as yf
import pandas as pd

def load_data(symbol, start_date, end_date):
    df = yf.download(symbol, start=start_date, end=end_date, interval="1d")
    df.dropna(inplace=True)
    return df

