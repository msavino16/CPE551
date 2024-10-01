import pytest
from pyramidArea import calcBaseArea, calcSideArea, prntSurfArea

def test_calcBaseArea1():
    assert calcBaseArea(15) == 225

@pytest.mark.xfail(reason="Input should not be text")
def test_calcBaseArea2():
    assert calcBaseArea("5") == 25

def test_calcSideAreaBetween1():
    assert 270.41 <= calcSideArea(15,5) <= 270.42

def test_calcSideAreaBetween2():
    assert round(calcSideArea(10,3),2) == 116.62


@pytest.mark.skip(reason="This function only prints text to the screen")
def test_prntSurfArea():
    prntSurfArea(5,10)