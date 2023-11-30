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

        #####
        return self

    def __next__(self):
        #####
        if len(self.list_of_list) == 0:
            print('В списке не осталось вложенных списков')
            raise StopIteration
        else:
            if len(self.list_of_list[0]) > 0:
                item = self.list_of_list[0].pop(0)
            elif len(self.list_of_list[0][0]) == 0:
                print('Во вложенных списках не осталось элементов')
                raise StopIteration
            else:
                item = self.list_of_list[1].pop(0)
                self.list_of_list.pop(0)
        print(self.list_of_list)
        #####
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
        # print(f'flat_iterator_item = {flat_iterator_item}, {type(flat_iterator_item)}')
        # print(f'check_item = {check_item}, {type(check_item)}')
        # print('\n')
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
