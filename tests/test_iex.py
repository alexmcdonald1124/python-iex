import pytest
from iex.iex import IEX

def financials_search():
    results = iex.financials("aapl")
    assert results