import pytest
from .hashtable import Hashtable

def test_exists():
    assert Hashtable


# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable._set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected

def test_successful_hash():
    h = Hashtable()
    actual = h.hash("a")
    expected = 237
    assert actual == expected

def test_keys():
    h = Hashtable(10)
    h._set("ape", 1)
    h._set("bow", 2)
    h._set("cat", 3)
    h._set("pea", 4)
    actual = h.keys()
    expected = ['pea', 'ape', 'bow', 'cat']
    assert actual == expected

# @pytest.mark.skip("TODO")
# def test_internals():
#     hashtable = Hashtable(1024)
#     hashtable.set("ahmad", 30)
#     hashtable.set("silent", True)
#     hashtable.set("listen", "to me")

#     actual = []

#     # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
#     for item in hashtable._buckets:
#         if item:
#             actual.append(item.display())

#     expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

#     assert actual == expected
