from insertion_sort import insertion_sort
import pytest

def test_exists():
    assert insertion_sort

def test_sorted():
    assert insertion_sort([6,3,9,10,41,30,12]) == [3,6,9,10,12,30,41]

def test_negative():
    assert insertion_sort([-6,3,-9,10,41,-30,12]) == [-30,-9,-6,3,10,12,41]

def test_empty():
    assert insertion_sort([]) == []

def test_dupes():
    assert insertion_sort([1,2,2,2,1]) == [1,1,2,2,2]
