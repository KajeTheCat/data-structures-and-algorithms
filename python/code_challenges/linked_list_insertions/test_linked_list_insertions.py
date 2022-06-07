import pytest
from linked_list_insertions import LinkedList,Node

def test_instantiate_one():
    assert LinkedList()

def test_instantiate_two():
    assert LinkedList([1,2,3,4,5])

