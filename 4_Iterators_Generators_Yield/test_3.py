class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.flatten_list = self.flatten(self.list_of_lists)
        self.index = 0

    def flatten(self, lst):
        for item in lst:
            if isinstance(item, list):
                yield from self.flatten(item)
            else:
                yield item

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = next(self.flatten_list)
            return item
        except StopIteration:
            raise StopIteration

def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
