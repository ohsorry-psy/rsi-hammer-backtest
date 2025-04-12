import pandas as pd
import matplotlib.pyplot as plt

def detect_hammer(df: pd.DataFrame) -> list:
    signals = []
    for i in range(1, len(df)):
        o, h, l, c = df.iloc[i][['Open', 'High', 'Low', 'Close']]
        body = abs(o - c)
        lower_shadow = min(o, c) - l
        upper_shadow = h - max(o, c)
        if body < (h - l) * 0.3 and lower_shadow > body * 2 and c > o:
            signals.append(i)
    return signals

def detect_rsi_divergence(df: pd.DataFrame, rsi_col='RSI', window=5):
    bullish_signals = []
    bearish_signals = []

    for i in range(window * 2, len(df)):
        price_now = float(df['Close'].iloc[i])
        price_prev = float(df['Close'].iloc[i - window:i].min())
        rsi_now = float(df[rsi_col].iloc[i])
        rsi_prev = float(df[rsi_col].iloc[i - window:i].min())

        if price_now < price_prev and rsi_now > rsi_prev:
            bullish_signals.append(i)

        price_now = float(df['Close'].iloc[i])
        price_prev = float(df['Close'].iloc[i - window:i].max())
        rsi_now = float(df[rsi_col].iloc[i])
        rsi_prev = float(df[rsi_col].iloc[i - window:i].max())

        if price_now > price_prev and rsi_now < rsi_prev:
            bearish_signals.append(i)

    return bullish_signals, bearish_signals

def backtest(df: pd.DataFrame, signals: list, hold_days=5, commission=0.002) -> pd.Series:
    returns = []
    for i in signals:
        if i + hold_days < len(df):
            entry = df['Close'].iloc[i]
            exit_ = df['Close'].iloc[i + hold_days]
            gross_return = (exit_ - entry) / entry
            net_return = gross_return - commission
            returns.append(net_return)
    return pd.Series(returns, dtype='float')

def plot_signals(df, signals, symbol):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Close'], label='Close Price')
    plt.plot(df['RSI'], label='RSI', alpha=0.5)
    plt.scatter(df.index[signals], df['Close'].iloc[signals], color='green', label='Combined Signal', marker='^')
    plt.title(f"{symbol} - Hammer + RSI Divergence")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("static/charts/combined_strategy.png")
    plt.close()
