import os
import random
import threading
import time

from alpaca.data.historical import StockHistoricalDataClient
from dotenv import load_dotenv
from pymongo import MongoClient

from config import MONGO_DB_USER, mongo_url
from helper_files.client_helper import dynamic_period_selector, get_latest_price, get_ndaq_tickers, strategies
from strategies.talib_indicators import get_data, simulate_strategy


def test_strategies():

    # Initialize the StockHistoricalDataClient
    mongo_client = MongoClient()
    tickers = get_ndaq_tickers(mongo_url, os.environ.get("FINANCIAL_PREP_API_KEY"))
    mongo_client.close()
    """
   periods = ['1d', '5d','1mo', '3mo', '6mo', '1y', '2y', '5y', 'ytd', 'max']
   account_cash = 50000
   portfolio_qty = 10
   total_portfolio_value = 500000
   # Define test parameters  
   for ticker in tickers: 
      current_price = get_latest_price(ticker)   
      historical_data = get_data(ticker)
      for strategy in strategies: 
         
         
         try:
            decision = simulate_strategy(strategy, ticker, current_price, historical_data, account_cash, portfolio_qty, total_portfolio_value)

            print(f"{strategy.__name__} : {decision} :{ticker}")
         except Exception as e:
            print(f"ERROR processing {ticker} for {strategy.__name__}: {e}")
      time.sleep(5)
   """
    for ticker in tickers:
        print(f"{ticker} : {dynamic_period_selector(ticker)}")


if __name__ == "__main__":
    load_dotenv("./.dev.env")
    print(get_latest_price("VRTX"))
    """
   test_strategies()
   """
