import os
import types
from datetime import datetime


def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            result = list(old_function(*args, **kwargs))
            with open(path, 'a') as log_file:
                log_file.write(f'{datetime.now()} - {old_function.__name__} - args: {args}, kwargs: {kwargs}, result: {result}\n')
            return (item for item in result)
        return new_function
    return __logger


@logger('flat_generator.log')
def flat_generator(list_of_lists):
    for item in list_of_lists:
        if isinstance(item, list):
            yield from flat_generator(item)
        else:
            yield item


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
