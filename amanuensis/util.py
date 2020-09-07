import operator
from functools import reduce
from typing import Iterable


def cascade(*args, into: dict) -> dict:
    """
    Ensures that a passed dictionary has all the arbitrarily-nested
    keys/indices to enter a value at the end point.

    Essentially if you want to make sure your dictionary can do this:

    into[key1][index1][key2] = value

    Then run cascade first.

    **NOTE**: This function WILL change the dictionary you pass via
        into directly! It does not create a copy of into and return it.

    Args:
        *args: An arbitrarily long list of tuples, the first index of
            which must be either a key or an index, and the second value
            of which must be dict or list constructors, depending on
            whether you want to create a dict or list at that position.
        into: A dictionary, which may or may not be empty.

    Returns: The dictionary passed via into, modified to ensure it has
        all the keys and values passed in args.

    """
    for i, a in enumerate(args):
        key = a[0]
        func = a[1]
        if i == 0:
            parent = into
        else:
            prev_args = [arg[0] for arg in args[:i]]
            parent = reduce(operator.getitem, prev_args, into)
        if isinstance(parent, dict):
            if parent.get(key) is None:
                parent[key] = func()
        elif isinstance(parent, list):
            if len(parent) <= key:
                parent.append(func())
    return into


def tuplify(value, do_none: bool = False) -> (tuple, None):
    """
    Simple function that puts the passed object value into a tuple, if
    it is not already.

    Args:
        value: Any object.
        do_none: If True, tells tuplify to tuplify Nones. By default,
            Nones are returned untouched.

    Returns: A tuple, or None.

    """
    if not isinstance(value, tuple) and (value is not None or do_none):
        if isinstance(value, dict):
            value = [(k, v) for k, v in value.items()]
        elif not isinstance(value, Iterable) or isinstance(value, str):
            value = [value]
        return tuple(value)
    else:
        return value
