import streamlit as st
import requests

st.title("🚀 Crypto AI Monitor")

coin = st.selectbox("选择币种", ["BTC", "ETH", "SOL", "BNB"])

def get_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}USDT"
    data = requests.get(url).json()
    return float(data["price"])

price = get_price(coin)

st.metric(label=f"{coin} 最新价格", value=f"${price:,.2f}")
