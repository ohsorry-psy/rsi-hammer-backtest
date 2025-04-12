from data_loader import load_data
from strategy import detect_hammer, detect_rsi_divergence, backtest
from generate_chart import generate_combined_chart

symbol = input("종목 코드 (예: AAPL): ").strip().upper()
start_date = input("시작 날짜 (예: 2024-04-01): ").strip()
end_date = input("종료 날짜 (예: 2025-04-10): ").strip()
commission_input = input("수수료율 (%) 예: 0.2 → 0.002 로 계산됨 [기본값 0.2]: ").strip()
commission = float(commission_input) / 100 if commission_input else 0.002

df = load_data(symbol, start_date, end_date)
hammer_signals = detect_hammer(df)
rsi_signals, _ = detect_rsi_divergence(df)
combined_signals = list(sorted(set(hammer_signals) & set(rsi_signals)))

returns = backtest(df, combined_signals, commission=commission)
print("✅ 총 거래 수:", len(returns))
print("📊 평균 수익률:", f"{returns.mean() * 100:.2f}%")
print("✅ 승률:", f"{(returns > 0).mean() * 100:.2f}%")
print("⚠️ 최대 손실:", f"{returns.min() * 100:.2f}%")

generate_combined_chart(symbol, start_date, end_date, commission)
