import pandas as pd

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


def backtest(df: pd.DataFrame, signals: list, hold_days=5, commission=0.002) -> pd.Series:
    returns = []
    for i in signals:
        if i + hold_days < len(df):
            entry = df['Close'].iloc[i]
            exit_ = df['Close'].iloc[i + hold_days]

            # 수익률 계산
            gross_return = (exit_ - entry) / entry
            net_return = gross_return - commission

            # 🛠 float 값만 저장
            returns.append(float(net_return))  # <-- tuple 방지용!

    return pd.Series(returns, dtype='float')

 def detect_rsi_divergence(df: pd.DataFrame, rsi_col='RSI', window=5):
    bullish_signals = []
    bearish_signals = []

    if rsi_col not in df.columns or 'Close' not in df.columns:
        raise ValueError("필요한 컬럼이 누락되었습니다. (RSI 또는 Close)")

    for i in range(window * 2, len(df)):
        price_now = df['Close'].iloc[i]
        price_prev = df['Close'].iloc[i - window:i].min()
        rsi_now = df[rsi_col].iloc[i]
        rsi_prev = df[rsi_col].iloc[i - window:i].min()

        if price_now < price_prev and rsi_now > rsi_prev:
            bullish_signals.append(i)

        price_now = df['Close'].iloc[i]
        price_prev = df['Close'].iloc[i - window:i].max()
        rsi_now = df[rsi_col].iloc[i]
        rsi_prev = df[rsi_col].iloc[i - window:i].max()

        if price_now > price_prev and rsi_now < rsi_prev:
            bearish_signals.append(i)

    return bullish_signals, bearish_signals



import pandas as pd
import numpy as np

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
    bullish = []
    bearish = []
    for i in range(window * 2, len(df)):
        price_now = float(df['Close'].iloc[i])
        price_prev = float(df['Close'].iloc[i - window:i].min())
        rsi_now = float(df[rsi_col].iloc[i])
        rsi_prev = float(df[rsi_col].iloc[i - window:i].min())
        if price_now < price_prev and rsi_now > rsi_prev:
            bullish.append(i)

        price_now = float(df['Close'].iloc[i])
        price_prev = float(df['Close'].iloc[i - window:i].max())
        rsi_now = float(df[rsi_col].iloc[i])
        rsi_prev = float(df[rsi_col].iloc[i - window:i].max())
        if price_now > price_prev and rsi_now < rsi_prev:
            bearish.append(i)
    return bullish, bearish

def backtest(df: pd.DataFrame, signals: list, hold_days=5, commission=0.002):
    returns = []
    for i in signals:
        if i + hold_days < len(df):
            entry = df['Close'].iloc[i]
            exit_ = df['Close'].iloc[i + hold_days]
            gross_return = (exit_ - entry) / entry
            net_return = gross_return - commission
            returns.append(net_return)
    return pd.Series(returns, dtype="float")
