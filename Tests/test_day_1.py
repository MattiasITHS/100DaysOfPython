import Day_1


def test_MyFirstTest() -> None:
    add = Day_1.add(5, 5)
    assert add == 10


def test_sub() -> None:
    sub = Day_1.sub(5, 5)
    assert sub == 0


def test_multi() -> None:
    multi = Day_1.multi(5, 5)
    assert multi == 25


def test_div() -> None:
    div = Day_1.div(5, 5)
    assert div == 1
