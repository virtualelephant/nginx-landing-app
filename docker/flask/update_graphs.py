import yfinance as yf
import matplotlib.pyplot as plt
import os

# Directory for storing images
STATIC_DIR = "static"
STOCK_FILE = "stocks.txt"

# Function to generate stock graph
def generate_stock_graph(ticker, filename):
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="7d")  # Fetch last 7 days of data

        if hist.empty:
            print(f"Warning: No data found for {ticker}")
            return

        plt.figure(figsize=(6, 3))
        plt.plot(hist.index, hist["Close"], marker="o", linestyle="-", label=ticker)
        plt.title(f"{ticker} Stock Price")
        plt.xlabel("Date")
        plt.ylabel("Price (USD)")
        plt.grid(True)
        plt.legend()

        # Save the graph
        filepath = os.path.join(STATIC_DIR, filename)
        plt.savefig(filepath, bbox_inches="tight")
        plt.close()
        print(f"Graph saved: {filename}")
    except Exception as e:
        print(f"Error generating graph for {ticker}: {e}")

# Function to read stock tickers from file
def get_stock_list():
    if not os.path.exists(STOCK_FILE):
        print("Warning: stocks.txt not found. Using default list.")
        return ["AVGO", "NVDA", "TSLA", "SPYI", "JEPQ", "YMAX", "MSFO"]  # Default fallback

    with open(STOCK_FILE, "r") as f:
        stocks = [line.strip() for line in f if line.strip()]
    return stocks

# Function to update all graphs
def update_all_graphs():
    print("Updating stock graphs...")
    
    # Indices
    generate_stock_graph("^GSPC", "sp500.png")  # S&P 500
    generate_stock_graph("^NYA", "nyse.png")    # NYSE
    generate_stock_graph("^IXIC", "nasdaq.png") # NASDAQ

    # Dynamic stocks from file
    stocks = get_stock_list()
    for stock in stocks:
        generate_stock_graph(stock, f"{stock.lower()}.png")
    
    print("Stock graphs updated.")

if __name__ == "__main__":
    update_all_graphs()
