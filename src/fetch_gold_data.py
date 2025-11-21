#We import the yfinance library, which lets us download financial data 
import yfinance as yf
#we import datetime tools - we may use them later for scheduling or date calculations
from datetime import datetime, timedelta


def fetch_gold_data(period="1mo", interval="1d"):
    """
    Fetch gold price data (XAUUSD) from Yahoo Finance.
    
    period = how much historical data to pull (e.g., '1mo', '3mo', '1y')
    interval = how often each data point is taken (e.g., '1d' = daily)
    """
    #This ticker represents Gold Futures on Yahoo Finances
    ticker = "GC=F"  # Gold futures continuous contract

    #Download the gold price data
    #auto_adjust=False means we leep raw OHLC prices
    #progress=False hides unnecssary download progress bars
    data = yf.download(ticker, period=period, interval=interval, auto_adjust=False,
                       progress=False)

    #if no data is returned (internet issue, wrong ticker, etc.)
    if data.empty:
        raise ValueError("No data returned from Yahoo Finance.")

    #By default, yfinance uses the date as the index (not a column)
    #This line converts the index back into a normal column called 'Date'.
    data.reset_index(inplace=True)
    # Now the dataframe has a clean structure with columns like:
    # Date, Open, High, Low, Close, Volume
    return data

#When this file is run directly (not imported), run this test:
if __name__ == "__main__":
    df = fetch_gold_data()
    print(df.head()) # print the first 5 rows to confirm it worked
