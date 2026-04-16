import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Black Scholes project",
    page_icon="📈",
)

# --- custom styling ---
st.markdown("""
<style>
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
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<div class="sidebar-title">📊 Black-Scholes Model</div>', unsafe_allow_html=True)
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

    asset_price = st.number_input("Current Asset Price", value=99.93)
    strike_price = st.number_input("Strike Price", value=99.88)
    maturity = st.number_input("Time to Maturity (Years)", value=1.00)
    volatility = st.number_input("Volatility (σ)", value=0.20)
    risk_free = st.number_input("Risk-Free Interest Rate", value=0.05)

st.title("Black scholes pricing model")
st.write("Figure out how to do this part later")