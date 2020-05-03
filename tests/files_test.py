from amanuensis.files import walk_iter


def test_walk_iter():
    d = {'test': {'subdirA': 'A1', 'subdirB': ['B1', 'B2'], 'subdirC': None}}
    expected = [
        'test',
        'test/subdirA',
        'test/subdirA/A1',
        'test/subdirB',
        'test/subdirB/B1',
        'test/subdirB/B2',
        'test/subdirC'
    ]
    assert walk_iter(d) == expected

    d = ['test', 'test1', 'testA']
    expected = ['test', 'test1', 'testA']
    assert walk_iter(d) == expected
