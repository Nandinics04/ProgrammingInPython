from hello_4 import hello


def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("Nandini") == "hello, Nandini"

