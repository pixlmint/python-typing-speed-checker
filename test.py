import main


def test_get_poem_lines():
    lines = main.get_poem_lines(2)
    assert len(lines) == 2
    assert isinstance(lines, list)
