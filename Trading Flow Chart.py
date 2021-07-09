# This is my first Python project that will help a technical analyst decide if they should buy a stock, sell a stock, or wait for a breakout.

# Trends: Bullish, Bearish, Consolidating. Use "Yes" -or- "No" for at_support_level and at_resistance_level.
trend_of_stock = ""
at_support_level = ""
at_resistance_level = ""

# -----> Code that recommends to buy, sell, or wait for breakout  <-----
if trend_of_stock == "Bullish" and at_support_level == "Yes":
    print("Buy the stock!")
elif trend_of_stock == "Bearish" and at_resistance_level == "Yes":
    print("Sell the stock!")
elif trend_of_stock == "Consolidating":
    print("Wait for breakout!")
else:
    print("Don't trade!")

# I am not a technical analyst, but thought the flow chart would be a great little start to coding.