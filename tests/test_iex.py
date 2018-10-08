import pytest
import sys

sys.path.insert(0,"../python-iex/iex")

from iex import IEX

iex = IEX()
results = iex.financials("aapl")
print(results)