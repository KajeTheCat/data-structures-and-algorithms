from merge import mergesort
import pytest

def test_exists():
    assert mergesort

def test_sorted():
    assert mergesort([6,3,9,10,41,30,12]) == [3,6,9,10,12,30,41]

def test_negative():
    assert mergesort([-6,3,-9,10,41,-30,12]) == [-30,-9,-6,3,10,12,41]

def test_empty():
    assert mergesort([]) == []

def test_dupes():
    assert mergesort([1,2,2,2,1]) == [1,1,2,2,2]
