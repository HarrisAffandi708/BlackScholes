import streamlit as st
import pandas as pd
import numpy as np
from math import log, sqrt, exp
from scipy.stats import norm

st.set_page_config(
    page_title="Black Scholes project",
    page_icon="📈",
    layout="wide"
)

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
    max-width: 100%;
}


section[data-testid="stSidebar"] {
    background-color: #1e1e2f;
    padding-top: 20px;
}

.sidebar-title {
    color: white;
    font-size: 34px;
    font-weight: 700;
    margin-bottom: 20px;
}

.created-by {
    color: #00c853;
    font-size: 18px;
    font-weight: 700;
    margin-top: 10px;
    margin-bottom: 10px;
}

.linkedin-box {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 30px;
}

.linkedin-name a {
    text-decoration: none;
    color: white !important;
    background-color: #2b2b3d;
    padding: 8px 12px;
    border-radius: 8px;
    font-weight: 600;
}

.linkedin-icon {
    width: 34px;
    height: 34px;
}

.main-title {
    font-size: 3.5rem;
    font-weight: 800;
    margin-top: 3rem;
    margin-bottom: 1rem;
}

.value-box {
    border-radius: 20px;
    overflow: hidden;
    min-height: 100px;
    padding: 14px 20px;
    text-align: center;
    color: black;
    font-family: sans-serif;
    box-sizing: border-box;
    width: 100%;
}

.call-box {
    background-color: #8BE28A;
}

.put-box {
    background-color: #F3C6C6;
}

.value-title {
    font-size: 20px;
    font-weight: 500;
    margin-bottom: 10px;
    color: black;
}

.value-number {
    font-size: 28px;
    font-weight: 800;
    color: black;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<div class="sidebar-title">📈 Black-Scholes Model</div>', unsafe_allow_html=True)
    st.markdown('<div class="created-by">Created by:</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="linkedin-box">
        <img class="linkedin-icon" src="https://cdn-icons-png.flaticon.com/512/174/174857.png">
        <div class="linkedin-name">
            <a href="https://www.linkedin.com/in/harris-affandi/" target="_blank">
                Harris Affandi
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    asset_price = st.number_input("Current Asset Price", value=99.93, format="%.2f")
    strike_price = st.number_input("Strike Price", value=99.88, format="%.2f")
    maturity = st.number_input("Time to Maturity (Years)", value=1.00, format="%.2f")
    volatility = st.number_input("Volatility (σ)", value=0.20, format="%.2f")
    risk_free = st.number_input("Risk-Free Interest Rate", value=0.05, format="%.2f")

    st.divider()
    st.markdown("Heatmap parameters")
    call_price = st.number_input("Call Purchase Price", min_value=0.00, value=10.00)
    put_price = st.number_input("Put Purchase Price", min_value=0.00, value=5.00)
    min_spot_price = st.number_input("Min Spot Price (σ)", min_value=0.00, value=80.00)
    max_spot_price = st.number_input("Max Spot price", min_value=0.00, value=120.00)
    min_volatility = st.slider("Min Volatility for Heatmap", 0.00, 1.00, 0.50)
    max_volatility = st.slider("Max Volatility for Heatmap", 0.00, 1.00, 0.50)

    if min_spot_price >= max_spot_price:
        st.warning("Min Spot Price must be less than Max Spot Price.")
    if min_volatility >= max_volatility:
        st.warning("Min Volatility must be less than Max Volatility.")

st.markdown('<div class="main-title">Black-Scholes Pricing Model</div>', unsafe_allow_html=True)

df = pd.DataFrame([{
    "Current Asset Price": f"{asset_price:.2f}",
    "Strike Price": f"{strike_price:.2f}",
    "Time to Maturity (Years)": f"{maturity:.2f}",
    "Volatility (σ)": f"{volatility:.2f}",
    "Risk-Free Interest Rate": f"{risk_free:.2f}"
}])

st.dataframe(df, use_container_width=True, hide_index=True)

st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)

#put and call logic and display


def callOrPut(bool, asset_price,strike_price, maturity, volatility, risk_free):
    if( len(bool) == 0 or asset_price == 0 or strike_price == 0 or maturity == 0 or volatility == 0):
        return 0.0

    d1 = ( log(asset_price/strike_price) + (risk_free + ((volatility)**2)/2) * maturity)/(volatility * (sqrt(maturity)))
    d2 = d1 - (volatility * sqrt(maturity))

    if(bool == "call"):
        call_price = (asset_price * norm.cdf(d1)) - (strike_price * (exp(-risk_free * maturity)) * norm.cdf(d2))
        return call_price
    elif(bool == "put"):
        put_price = (strike_price * (exp(-risk_free * maturity)) * norm.cdf(-d2)) - (asset_price * norm.cdf(-d1))
        return put_price

    return 0.0

def pnlData(option_type, purchase_price, strike_price, maturity, risk_free, spot_prices, volatilities):
    pnl_matrix = []

    for x in volatilities:
        row = []
        for y in spot_prices:
            price = callOrPut(option_type, y, strike_price, maturity, x, risk_free)
            pnl = price - purchase_price
            row.append(pnl)
        pnl_matrix.append(row)
    df = pd.DataFrame(
        pnl_matrix,
        index=[f"{v:.2f}" for v in volatilities],
        columns=[f"{s:.2f}" for s in spot_prices]
    )
    return df





call_value = callOrPut("call", asset_price,strike_price, maturity, volatility, risk_free)
put_value = callOrPut("put", asset_price,strike_price, maturity, volatility, risk_free)
col1, col2 = st.columns([1, 1], gap="medium")

with col1:
    st.markdown(f"""
    <div class="value-box call-box">
        <div class="value-title">CALL Value</div>
        <div class="value-number">${call_value:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="value-box put-box">
        <div class="value-title">PUT Value</div>
        <div class="value-number">${put_value:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-title">Options pricing heatmap</div>', unsafe_allow_html=True)
st.info("Explore how option prices change due to volatility and spot price with the same strike price")

call_pnl = call_value - call_price
put_pnl = put_value - put_price

call_pnl_class = "call-box" if call_pnl >= 0 else "put-box"
put_pnl_class = "call-box" if put_pnl >= 0 else "put-box"

col3, col4 = st.columns([1, 1], gap="medium")

with col3:
    st.markdown(f"""
    <div class="value-box {call_pnl_class}">
        <div class="value-title">CALL PnL</div>
        <div class="value-number">${call_pnl:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="value-box put-box">
        <div class="value-title">PUT PnL</div>
        <div class="value-number">${put_pnl:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

#heatmap part
if min_spot_price < max_spot_price and min_volatility < max_volatility:
    spot_prices = np.linspace(min_spot_price, max_spot_price, 10)
    volatilities = np.linspace(min_volatility, max_volatility, 10)

    call_pnl_df = pnlData(
        "call",
        call_price,
        strike_price,
        maturity,
        risk_free,
        spot_prices,
        volatilities
    )

    put_pnl_df = pnlData(
        "put",
        put_price,
        strike_price,
        maturity,
        risk_free,
        spot_prices,
        volatilities
    )

    st.subheader("Call PnL Heatmap")
    st.dataframe(
        call_pnl_df.style.format("{:.2f}").background_gradient(cmap="RdYlGn", axis=None),
        use_container_width=True
    )

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

    st.subheader("Put PnL Heatmap")
    st.dataframe(
        put_pnl_df.style.format("{:.2f}").background_gradient(cmap="RdYlGn", axis=None),
        use_container_width=True
    )
else:
    st.error("Please make sure the minimum values are less than the maximum values for the heatmap.")




