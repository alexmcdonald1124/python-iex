import pytest
import sys

sys.path.insert(0,"../python-iex/iex")

from iex import IEX

iex = IEX()

iex.statistics("aapl")
iex.financials("aapl")
iex.book("aapl")
iex.company("aapl")
iex.delayed_quote("aapl")
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
iex.news("aapl", 1)
iex.ohlc("aapl")
iex.market_ohlc()
iex.peers("aapl")
iex.previous("aapl")
iex.market_previous()
iex.price("aapl")
iex.quote("aapl")
iex.relevant_stocks("aapl")