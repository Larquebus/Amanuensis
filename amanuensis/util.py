from typing import Iterable


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
