import pytest
import sys

from iex.iex import IEX

def financials_search():
    iex = IEX()
    results = iex.financials("aapl")
    assert(results)