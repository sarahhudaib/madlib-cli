import pytest
from madlib_cli.madlib import read_template, parse, merge

def test_read_template_returns_stripped_string():
    actual = read_template()
    received = read_template()
    assert actual == received


@pytest.mark.skip("pending")
def test_parse_template():
    actual_stripped, actual_parts = parse(
        "It was a {Adjective} and {Adjective} {Noun}."
    )
    expected_stripped = "It was a {} and {} {}."
    expected_parts = ("Adjective", "Adjective", "Noun")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


@pytest.mark.skip("pending")
def test_merge():
    actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    assert actual == expected


@pytest.mark.skip("pending")
def test_read_template_raises_exception_with_bad_path():

    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        read_template(path)


def testParse():
    expected = ["first name","age"]
    received = parse("hello {first name}, I am {age} years old")
    assert expected == received


## merge takes empty curly braces
def testMerge():
    words = ['smart' , 'boxes', 'hungry' , 'eat']
    text = 'A {} {} had a {} dog so they {} them'
    received = merge(text, words)
    expected = 'A smart boxes had a hungry dog so they eat them'
    assert expected == received
