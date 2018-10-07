import pytest
import sys

sys.path.append("..")

from iex.iex import IEX

def financials_search():
	iex = IEX()
    results = iex.financials("aapl")
    assert results