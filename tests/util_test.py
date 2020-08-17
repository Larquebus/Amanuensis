import amanuensis.util as u


def test_tuplify():
    assert isinstance(u.tuplify('test'), tuple)
    assert u.tuplify('test') == ('test',)
    assert u.tuplify(None) is None
    assert u.tuplify(None, True) == (None,)
    assert u.tuplify([1, 2, 3]) == (1, 2, 3)
    assert u.tuplify({1, 2, 3}) == (1, 2, 3)
    assert u.tuplify({'a': 1, 'b': 2}) == (('a', 1), ('b', 2))
    assert u.tuplify(1) == (1,)
    assert u.tuplify(1.23) == (1.23,)
