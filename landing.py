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
/* Main page spacing */
.block-container {
    padding-top: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
    max-width: 100%;
}

/* Sidebar */
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

/* Title */
.main-title {
    font-size: 3.5rem;
    font-weight: 800;
    margin-bottom: 1rem;
}

/* Cards */
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

# Title
st.markdown('<div class="main-title">Black-Scholes Pricing Model</div>', unsafe_allow_html=True)

# Table
df = pd.DataFrame([{
    "Current Asset Price": f"{asset_price:.4f}",
    "Strike Price": f"{strike_price:.4f}",
    "Time to Maturity (Years)": f"{maturity:.4f}",
    "Volatility (σ)": f"{volatility:.4f}",
    "Risk-Free Interest Rate": f"{risk_free:.4f}"
}])

st.dataframe(df, use_container_width=True, hide_index=True)

# Space under table
st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)

# Cards
call_value = 10.47
put_value = 5.55

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
