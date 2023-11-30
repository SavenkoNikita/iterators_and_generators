# Задание 1.
# Доработать класс FlatIterator в коде ниже. Должен получиться итератор, который принимает список списков и
# возвращает их плоское представление, т. е. последовательность, состоящую из вложенных элементов. Функция test в
# коде ниже также должна отработать без ошибок.

class FlatIterator:
    """
    Принимает список списков и возвращает их плоское представление, т. е. последовательность, состоящую из
    вложенных элементов.
    """

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.i = -1
        # self.next_list = self.list_of_list[self.i + 1]
        self.results = []
        # print(self.results)
        return self

    def __next__(self):
        if len(self.list_of_list) == 0:
            raise StopIteration
        else:
            # self.i = -1
            # self.result = []
            for lists in self.list_of_list:
                self.i += 1
                for elem in lists:
                    self.results.append(elem)

            # print(self.next_list)
            # self.next_list = self.list_of_list[self.i + 1]
            # self.list_of_list.pop(self.i)
        print(self.results)
        return self.results


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    print(type(list_of_lists_1))
    iter_list = FlatIterator(list_of_lists_1)
    print(type(iter_list))

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
