from hello import add, substract


def test_add():
    assert 2 == add(1, 1)

def test_substract():
    assert 2 == substract(3, 1)
