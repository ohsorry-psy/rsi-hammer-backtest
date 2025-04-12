# 📊 RSI + Hammer Backtest

RSI 다이버전스 + 해머(Hammer) 캔들 패턴 조합 전략 기반의 백테스트 및 시각화 웹 애플리케이션입니다.

![chart](static/chart/combined_strategy.png)

---

## 🔍 기능 소개

- ✅ 해머(Hammer) 캔들 패턴 탐지  
- ✅ RSI 다이버전스 (가격 하락 + RSI 상승)  
- ✅ 두 조건 조합 신호만 필터링  
- ✅ 백테스트 (수수료 반영, 승률, 최대 손실 등 리포트)  
- ✅ 차트 이미지 생성 (matplotlib)  
- ✅ Flask + Render 배포 대응  

---

## 🛠️ 사용 방법

1. 필수 라이브러리 설치

```bash
pip install -r requirements.txt
