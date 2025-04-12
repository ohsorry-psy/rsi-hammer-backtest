import pandas as pd
import matplotlib.pyplot as plt
import os
import ta
from data_loader import load_data
from strategy import detect_hammer, detect_rsi_divergence

def generate_combined_chart(symbol, start_date, end_date, commission=0.002):
    df = load_data(symbol, start_date, end_date)
    df['RSI'] = ta.momentum.RSIIndicator(close=df['Close']).rsi()
    df.dropna(inplace=True)

    hammer = detect_hammer(df)
    rsi, _ = detect_rsi_divergence(df)
    combined = sorted(set(hammer) & set(rsi))

    if not os.path.exists("static/charts"):
        os.makedirs("static/charts")

    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Close'], label="Close Price")
    plt.plot(df.index, df['RSI'], label="RSI", alpha=0.4)
    plt.scatter(df.index[combined], df['Close'].iloc[combined], color="green", marker="^", label="Buy Signal")
    plt.title(f"{symbol} - Hammer + RSI Divergence")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    output_path = f"static/charts/{symbol}_combined_strategy.png"
    plt.savefig(output_path)
    plt.close()
    return output_path
