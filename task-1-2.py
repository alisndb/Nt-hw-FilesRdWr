import os
from pprint import pprint


class CookBook:
    def __init__(self):
        self.cook_book = None
        self.shop_list = None

    def get_cook_book_from_path(self, path):
        self.cook_book = {}
        with open(path, 'r', encoding='utf-8') as file:
            for dish in file:
                counter = int(file.readline().strip())
                temp_data = []
                for item in range(counter):
                    name, quantity, measure = file.readline().split('|')
                    temp_data.append(
                        {'ingredient_name': name.strip(), 'quantity': int(quantity.strip()), 'measure': measure.strip()}
                    )
                self.cook_book[dish.strip()] = temp_data
                file.readline()

    def get_shop_list_by_dishes(self, dishes, person_count):
        if not self.cook_book:
            return 'Сперва создайте кулинарную книгу!'
        self.shop_list = {}
        for dish in dishes:
            if dish not in self.cook_book.keys():
                return 'Данного блюда нет в кулинарной книге!'
            for item in self.cook_book[dish]:
                if item['ingredient_name'] not in self.shop_list.keys():
                    self.shop_list[item['ingredient_name']] = {'measure': item['measure'],
                                                               'quantity': item['quantity'] * person_count}
                else:
                    self.shop_list[item['ingredient_name']]['quantity'] += item['quantity'] * person_count


cook_book_1 = CookBook()

cook_book_1.get_cook_book_from_path(os.path.join(os.getcwd(), 'recipes.txt'))
pprint(cook_book_1.cook_book)

cook_book_1.get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint(cook_book_1.shop_list)
