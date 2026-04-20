# Black Scholes
A mini project regarding the black scholes model


## dependencies
streamlit
<br>pandas
<br>numpy
<br>math
<br>scipy
<br>matplotlib

## steps 
python -m vevnv .venv
<br>source .venv/bin/activate
<br>download the dependencies
<br>streamlit run landing.py
<br>to deactivate the env: deactivate

## Black scholes options model images (without pnl)
![Alt text](images/blackScholes_image.png)

## Black scholes option pricing heat map (pnl)
![Alt text](images/pnl2.png)
![Alt text](images/pnl.png)
This heatmap shows the pnl given a range of spot prices and volatilty with a set strike price. In this example, the spot price range is 80 to 120. The volatility range is 0.2 to 0.5. The strike price is 99.88. Let's take the first row and column for the call heatmap, it shows the value -8.12. This means that based on black scholes model, the fair price for the option is 1.88 due to the volatility and spot price, however we paid 10 for the it. This means that we lost 8.12 on this trade.

# Details
## Author
- Harris Ilhan Bin Ahmad Affandi
