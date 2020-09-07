import amanuensis.util as u


def test_cascade_dict_list():
    data = dict()

    expected = {'animals': {'reptiles': []}}

    u.cascade(('animals', dict), ('reptiles', list), into=data)

    assert data == expected


def test_cascade_dict_list_dict():
    data = dict()

    expected = {'animals': {'reptiles': [{}]}}

    u.cascade(('animals', dict), ('reptiles', list), (0, dict), into=data)

    assert data == expected

    expected = {'animals': {'reptiles': [{}, {}]}}

    u.cascade(('animals', dict), ('reptiles', list), (1, dict), into=data)

    assert data == expected


def test_cascade_dict_list_dict_list():
    data = dict()

    expected = {'animals': {'reptiles': [{'africa': []}]}}

    u.cascade(
        ('animals', dict),
        ('reptiles', list),
        (0, dict),
        ('africa', list),
        into=data
    )

    assert data == expected


def test_cascade_dict_dict_list():
    data = dict()

    expected = {'animals': {'order': {'reptiles': []}}}

    u.cascade(
        ('animals', dict),
        ('order', dict),
        ('reptiles', list),
        into=data
    )

    assert data == expected


def test_cascade_list_list_dict():
    data = dict()

    expected = {'mammals': [[{}]]}

    u.cascade(
        ('mammals', list),
        (0, list),
        (0, dict),
        into=data
    )

    assert data == expected


def test_cascade_into_non_empty_dict():
    data = {'animals': {'reptiles': ['nile crocodile', 'gila monster']}}

    expected = {
        'animals': {
            'reptiles': ['nile crocodile', 'gila monster'],
            'mammals': []
        }
    }

    u.cascade(
        ('animals', dict),
        ('mammals', list),
        into=data
    )

    assert data == expected


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
