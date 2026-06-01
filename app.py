import streamlit as st
import requests
import plotly.graph_objects as go

st.set_page_config(page_title="Crypto AI Monitor", layout="wide")

st.title("🚀 Crypto AI Monitor - K线版")

coin = st.selectbox("选择币种", ["BTC", "ETH", "SOL", "BNB"])

# ===== 实时价格 =====
def get_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}USDT"
    data = requests.get(url).json()
    return float(data["price"])

price = get_price(coin)

st.metric(label=f"{coin} 最新价格", value=f"${price:,.2f}")

# ===== K线数据 =====
def get_kline(symbol):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}USDT&interval=1h&limit=50"
    data = requests.get(url).json()

    candles = {
        "open": [],
        "high": [],
        "low": [],
        "close": [],
        "time": []
    }

    for i in data:
        candles["open"].append(float(i[1]))
        candles["high"].append(float(i[2]))
        candles["low"].append(float(i[3]))
        candles["close"].append(float(i[4]))
        candles["time"].append(i[0])

    return candles

k = get_kline(coin)

fig = go.Figure(data=[
    go.Candlestick(
        x=k["time"],
        open=k["open"],
        high=k["high"],
        low=k["low"],
        close=k["close"]
    )
])

fig.update_layout(title=f"{coin} 1小时K线", xaxis_rangeslider_visible=False)

st.plotly_chart(fig, use_container_width=True)
