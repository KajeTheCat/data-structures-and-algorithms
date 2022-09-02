import pytest
from .hashtable_left_join import left_join
from .hashtable import Hashtable


def test_exists():
    assert left_join


# @pytest.mark.skip("TODO")
def test_example():
    synonyms = Hashtable()
    synonyms._set("diligent", "employed")
    synonyms._set("fond", "enamored")
    synonyms._set("guide", "usher")
    synonyms._set("outfit", "garb")
    synonyms._set("wrath", "anger")
    # {"diligent": "employed","fond": "enamored","guide": "usher","outfit": "garb","wrath": "anger",}
    antonyms = Hashtable()
    antonyms._set("diligent", "idle")
    antonyms._set("fond", "averse")
    antonyms._set("guide", "follow")
    antonyms._set("flow", "jam")
    antonyms._set("wrath", "delight")
    # {"diligent": "idle", "fond": "averse", "guide": "follow", "flow": "jam","wrath": "delight",}

    expected = [
        ['fond', 'enamored', 'averse'],
        ['outfit', 'garb', None],
        ['guide', 'usher', 'follow'],
        ['diligent', 'employed', 'idle'],
        ['wrath', 'anger', 'delight'],
    ]

    actual = left_join(synonyms, antonyms)

    assert actual == expected

def test_fail():
    synonyms = Hashtable()
    synonyms._set("diligent", "employed")
    synonyms._set("fond", "enamored")
    synonyms._set("guide", "usher")
    synonyms._set("outfit", "garb")
    synonyms._set("wrath", "anger")
    # {"diligent": "employed","fond": "enamored","guide": "usher","outfit": "garb","wrath": "anger",}
    antonyms = Hashtable()
    antonyms._set("diligent", "idle")
    antonyms._set("fond", "averse")
    antonyms._set("guide", "follow")
    antonyms._set("flow", "jam")
    antonyms._set("wrath", "delight")
    # {"diligent": "idle", "fond": "averse", "guide": "follow", "flow": "jam","wrath": "delight",}
    expected = [
        ['outfit', 'garb', None],
        ['fond', 'enamored', 'averse'],
        ['guide', 'usher', 'follow'],
        ['diligent', 'employed', 'idle'],
        ['wrath', 'anger', 'delight'],
    ]
    actual = left_join(synonyms, antonyms)

    assert actual != expected

def test_uneven_buckets():
    synonyms = Hashtable()
    synonyms._set("diligent", "employed")
    synonyms._set("fond", "enamored")
    synonyms._set("guide", "usher")
    synonyms._set("outfit", "garb")
    synonyms._set("wrath", "anger")
    # {"diligent": "employed","fond": "enamored","guide": "usher","outfit": "garb","wrath": "anger",}
    antonyms = Hashtable()
    antonyms._set("diligent", "idle")
    antonyms._set("fond", "averse")
    # {"diligent": "idle", "fond": "averse", "guide": "follow", "flow": "jam","wrath": "delight",}
    expected = [
        ['fond', 'enamored', 'averse'],
        ['outfit', 'garb', None],
        ['guide', 'usher', None],
        ['diligent', 'employed', 'idle'],
        ['wrath', 'anger', None],
    ]
    actual = left_join(synonyms, antonyms)

    assert actual == expected
