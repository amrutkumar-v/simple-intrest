import sys
from simpleintrest import simple_interest

def test_SI():
    assert simple_interest(2000,6,10) == 1200
    
def test_SIZERO():
    assert simple_interest(0,10,1) == 0
