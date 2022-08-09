from insertion_sort import insertion_sort
import pytest

def test_exists():
    assert insertion_sort

def test_sorted():
    arr = [6,3,9,10,41,30,12]

    actual = insertion_sort(arr)
    expected = insertion_sort(arr)

    assert actual == expected
