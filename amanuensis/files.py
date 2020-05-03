from os import mkdir
from os.path import exists


def hello_world():
    print('Hello world!')


def setup_dirs(dir_map: (list, tuple, dict)):
    """
    Creates a list of directory paths based on dir_map, which must be
    an iterable. Then, makes sure each of those directory paths exists,
    by creating them if necessary.

    :param dir_map: An iterable (list, tuple, or dictionary)
    :return: None
    """
    dir_paths = walk_iter(dir_map)
    for d in dir_paths:
        if not exists(d):
            mkdir(d)


def walk_iter(iterable: (list, tuple, dict), prev='', sep='/'):
    """
    Unpacks a nested dictionary into a list, with each level of the
    dictionary represented, so:
        {'outer': {'innerA': 'A1', 'innerB': ['B1', 'B2']}}
    becomes:
        ['outer', 'outer/innerA', 'outer/innerA/A1', 'outer/innerB',
         'outer/innerB/B1', 'outer/innerB/B2']

    Useful for turning a dictionary mock up of a file structure into
    an iterable set of file paths.

    :param iterable: An iterable of some kind, either a list, tuple, or
        dictionary.
    :param prev: A string, generally only used by walk_iter itself,
        since this function will call itself recursively.
    :param sep: A string, the desired separator between keys and values
        found in the iterable. Default is '/', since it is assumed that
        this function will be used to generate file paths.
    :return: A list.
    """
    result = []
    if isinstance(iterable, list) or isinstance(iterable, tuple):
        for i in iterable:
            result.append(prev + i)
    elif isinstance(iterable, dict):
        for k, v in iterable.items():
            result.append(prev + k)
            if v is not None:
                if isinstance(v, dict) or isinstance(v, list):
                    r = walk_iter(v, prev=prev + k + sep)
                    result += r
                elif isinstance(v, str):
                    result.append(prev + k + sep + v)
                else:
                    raise ValueError(f'Invalid directory structure found at {k}: {v}')
    return result
