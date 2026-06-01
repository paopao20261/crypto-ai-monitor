import streamlit as st

st.set_page_config(
    page_title="Crypto AI Monitor",
    layout="wide"
)

st.title("🚀 Crypto AI Monitor")
st.subheader("AI Crypto Dashboard")
st.success("部署成功")

st.write("选择币种查看信息")

coin = st.selectbox(
    "选择币种",
    ["BTC","ETH","SOL","BNB"]
)

st.metric(
    label=f"{coin} 最新价格",
    value="$0.00"
)
