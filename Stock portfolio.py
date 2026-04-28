# Simple Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "AMZN": 3300,
    "MSFT": 300
}

portfolio = {}
total_investment = 0

print("📊 Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))
print("Type 'done' to finish\n")

# Taking user input
while True:
    stock_name = input("Enter stock name: ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("❌ Stock not available. Try again.")
        continue

    quantity = int(input(f"Enter quantity of {stock_name}: "))

    portfolio[stock_name] = quantity

# Calculate total investment
print("\n📈 Portfolio Summary:")

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(f"{stock} -> {qty} shares × ${price} = ${value}")

print("\n💰 Total Investment Value: $", total_investment)

# Save to file (optional part)
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        file.write(f"{stock}: {qty} shares -> ${value}\n")
    file.write(f"\nTotal Investment: ${total_investment}")

print("\n✅ Portfolio saved to 'portfolio.txt'")
