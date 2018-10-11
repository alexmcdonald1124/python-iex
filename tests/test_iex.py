import pytest
import sys

sys.path.insert(0,"../python-iex/iex")

from iex import IEX

iex = IEX()

iex.statistics("aapl")
iex.financials("aapl")
iex.book("aapl")
iex.chart("aapl", "5y")
iex.company("aapl")
iex.delayed_quote("aapl")
iex.dividends("aapl", "5y")
iex.earnings("aapl")
iex.threshold_securities()
iex.short_interest_list()
iex.largest_trades("aapl")
iex.most_active()
iex.gainers()
iex.losers()
iex.iexvolume()
iex.iexpercent()
iex.logo("aapl")
iex.news("aapl")
iex.market_news(5)
iex.ohlc("aapl")
iex.market_ohlc()
iex.peers("aapl")
iex.previous("aapl")
iex.market_previous()
iex.price("aapl")
iex.quote("aapl")
iex.relevant_stocks("aapl")
iex.splits("aapl", "10y")
iex.time_series("aapl")
iex.volume_by_venue("aapl")
iex.symbols()
iex.corporate_actions("20181009")
iex.daily_dividends()
iex.next_day_ex_date()
iex.symbol_directory()