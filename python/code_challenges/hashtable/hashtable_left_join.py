from .hashtable import Hashtable


def left_join(hash1, hash2):
    join_list = []

    for _bucket in hash1._buckets:
        if _bucket is not None:
            join_list_key = _bucket.key
            join_list_value1 = _bucket.value
            if hash2.contains(_bucket.key):
                join_list_value2 = hash2.get(_bucket.key)
            else:
                join_list_value2 = None
            join_list.append([join_list_key, join_list_value1, join_list_value2])
    return join_list
