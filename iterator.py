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
        #####
        self.list_of_list = list_of_list
        #####

    def __iter__(self):
        #####
        self.list_index = 0
        self.element_index = 0
        #####
        return self

    def __next__(self):
        #####
        if len(self.list_of_list) != 0:
            if len(self.list_of_list) < (self.list_index + 1):
                self.list_index = 0
                self.element_index = 0
                raise StopIteration
            elif len(self.list_of_list[self.list_index]) > 0:
                self.item = self.list_of_list[self.list_index][self.element_index]
                if len(self.list_of_list[self.list_index]) > (self.element_index + 1):
                    self.element_index += 1
                else:
                    self.element_index = 0
                    if len(self.list_of_list) >= (self.list_index + 1):
                        self.list_index += 1
        #####
        return self.item


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
