class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.current_list_index = 0
        self.current_item_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_list_index >= len(self.list_of_lists):
            raise StopIteration

        if self.current_item_index >= len(self.list_of_lists[self.current_list_index]):
            self.current_list_index += 1
            self.current_item_index = 0
            return self.__next__()

        item = self.list_of_lists[self.current_list_index][self.current_item_index]
        self.current_item_index += 1
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
