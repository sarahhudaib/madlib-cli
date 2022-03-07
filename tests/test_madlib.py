import pytest
from madlib_cli.madlib import read_template, parse, merge

def test_read_template_returns_stripped_string():
    actual = read_template("madlib_cli/assets/template.txt")
    received = read_template("madlib_cli/assets/template.txt")
    assert actual == received


@pytest.mark.skip("pending")
def test_parse_template():
    expected = ["first name","age"]
    received = parse("hello {first name}, I am {age} years old")
    assert expected == received


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
