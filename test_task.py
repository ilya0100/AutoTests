from cmath import inf

import pytest
import sys


#  SET OPERATIONS

def add_elem_to_set(set, value):
    set.add(value)
    return set

def remove_elem(set, value):
    set.remove(value)
    return set


#   SET CHECK OPERATIONS

@pytest.mark.parametrize("set_before, value, set_after", [({1, 2}, 3, {1, 2, 3}),
                                                          ({11, 22, 33}, 33, {11, 22, 33})])
def test_add_elem(set_before, value, set_after):
    assert add_elem_to_set(set_before, value) == set_after


@pytest.mark.parametrize("set_before, value, set_after", [({1, 2, 3}, 3, {1, 2}) ])
def test_remove_elem(set_before, value, set_after):
    assert remove_elem(set_before, value) == set_after

def test_remove_not_exist():
    s = set('Hello')
    if 'a' not in s:
        with pytest.raises(KeyError):
            remove_elem(s, 'a')


#   FLOAT OPERATIONS

def func(item):
    return float(item)


#   FLOAT OPERATIONS CHECK

@pytest.mark.parametrize("item, answer", [('1.334234', 1.334234),
                                          (0, 0),
                                          (-1, -1)])
def test_simple_numbers(item, answer):
    assert func(item) == answer


@pytest.mark.parametrize("item, answer", [(sys.float_info.max + sys.float_info.max, inf),
                                          (sys.float_info.max, 1.7976931348623157e+308)])
def test_overflow_number(item, answer):
    assert func(item) == answer


@pytest.mark.parametrize("item, answer", [('abc123', ValueError),
                                          ('', ValueError),
                                          ('-5-', ValueError)])
def test_value_error(item, answer):
    try:
        assert func(item) == answer
    except ValueError:
        pass