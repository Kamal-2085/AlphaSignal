import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# -----------------------------------
# Load ticker
# -----------------------------------

ticker_symbol = "COALINDIA.NS"
ticker = yf.Ticker(ticker_symbol)

info = ticker.info
history = ticker.history(period="1mo")

# -----------------------------------
# Extract Price Data
# -----------------------------------

open_price = history["Open"].iloc[-1]
close_price = history["Close"].iloc[-1]
high_price = history["High"].iloc[-1]
low_price = history["Low"].iloc[-1]

# -----------------------------------
# Extract Market Metrics
# -----------------------------------

market_cap = info.get("marketCap", 0)
pe_ratio = info.get("trailingPE", 0)
pb_ratio = info.get("priceToBook", 0)
dividend_yield = info.get("dividendYield", 0)
beta = info.get("beta", 1)

# -----------------------------------
# Create Feature Vector
# -----------------------------------

features = np.array([
    open_price,
    close_price,
    high_price,
    low_price,
    market_cap,
    pe_ratio,
    pb_ratio,
    dividend_yield,
    beta
]).reshape(1,-1)

# -----------------------------------
# Dummy Training Data
# (In real system you train on many stocks)
# -----------------------------------

X_train = np.random.rand(100,9)

y_train = np.random.uniform(1,10,100)

# -----------------------------------
# Train Model
# -----------------------------------

model = RandomForestRegressor(n_estimators=200)

model.fit(X_train,y_train)

# -----------------------------------
# Predict Market Score
# -----------------------------------

score = model.predict(features)[0]

score = max(1, min(10, score))

print("Price & Market Data Score (1-10):", round(score,2))