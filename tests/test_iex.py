import pytest
import sys

sys.path.append("..")

from iex.iex import IEX

def financials_search():
    results = iex.financials("aapl")
    assert results