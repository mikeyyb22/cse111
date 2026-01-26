"""Verify that the names.py functions work correctly."""

from names import make_full_name, extract_family_name, extract_given_name
import pytest

"""Test make_full_name"""
def test_make_full_name():
    assert make_full_name("Michael", "McGehee") == "McGehee; Michael"
    assert make_full_name("Anna-Marie", "Jones") == "Jones; Anna-Marie"
    assert make_full_name("Bob", "Dobbs") == "Dobbs; Bob"
    assert make_full_name("Benjamin", "Washington-Smith") == "Washington-Smith; Benjamin"

def test_extract_family_name():
    assert extract_family_name("McGehee; Michael") == "McGehee"
    assert extract_family_name("Jones; Anna-Marie") == "Jones"
    assert extract_family_name("Dobbs; Bob") == "Dobbs"
    assert extract_family_name("Washington-Smith; Benjamin") == "Washington-Smith"

def test_extract_given_name():
    assert extract_given_name("McGehee; Michael") == "Michael"
    assert extract_given_name("Jones; Anna-Marie") == "Anna-Marie"
    assert extract_given_name("Dobbs; Bob") == "Bob"
    assert extract_given_name("Washington-Smith; Benjamin") == "Benjamin"

pytest.main(["-v", "--tb=line", "-rN", __file__])