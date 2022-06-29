import pprint


def read_cook_book(file_name):
    book = {}
    with open(file_name, encoding='utf-8') as file:
        for line in file:
            dish_list = []
            for i in range(int(file.readline())):
                ing_list = file.readline().split('|')
                dish_list.append({'ingredient_name': ing_list[0].strip(), 'quantity': float(ing_list[1]), 'measure': ing_list[2].strip()})
            book[line.strip()] = dish_list
            file.readline()
    return book


def get_shoplist_by_dishes(dishes, person_count, _cook_book):
    shoplist = {}
    for dish in dishes:
        if dish in _cook_book:
            for ingredient in _cook_book[dish]:
                if ingredient['ingredient_name'] in shoplist:
                    if shoplist[ingredient['ingredient_name']]['measure'] == ingredient['measure']:
                        shoplist[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
                    else:
                        return 'Ингредиент "' + ingredient['ingredient_name'] + '": ' + shoplist[ingredient['ingredient_name']]['measure'] +\
                               ' и ' + ingredient['measure'] + ' - несоизмеримые величины'
                else:
                    shoplist[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}
        else:
            return dish + ' - неизвестное блюдо'
    return shoplist


cook_book = read_cook_book('recipes.txt')
# pprint.pprint(cook_book, width = 160)

# pprint.pprint(get_shoplist_by_dishes(['Утка по-пекински', 'Еда', 'Питьё'], 1, cook_book))
pprint.pprint(get_shoplist_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book))
