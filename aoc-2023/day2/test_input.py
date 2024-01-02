import pytest
from .solution import Session

def test_input_less():
    file_path = "input-less.txt"
    session = Session.parse(file_path)
    assert sum(session.valid_ids()) == 8
    assert session.sum() == 2286

def test_input():
    file_path = "input.txt"
    session = Session.parse(file_path)
    assert sum(session.valid_ids()) == 2204
    assert session.sum() == 71036
