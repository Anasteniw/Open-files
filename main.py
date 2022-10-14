
# Задача №1

cook_book = {}
with open('recipes.txt', 'rt', encoding= "utf8") as file:
    for d in file:
        dish = d.strip()
        ingredients = []
        ingredients_items = file.readline()
        for i in range(int(ingredients_items)):
            index = file.readline()
            ingredient_name, quantity, measure = index.strip().split(' | ')
            ingredients.append({"ingredient_name": ingredient_name, "quantity" : quantity, "measure" : measure})
        blank_dishes = file.readline()
        cook_book.update({dish : ingredients})
print(cook_book)


# Задача №2

dishes = ['Запеченный картофель', 'Омлет']
person_count = int(input('Введите количество персон - '))
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for products in cook_book[dish]:
            amount_products = int(products['quantity']) * person_count
            res = {products['ingredient_name']: {'measure': products['measure'], 'quantity':  amount_products}}
            shop_list.update(res)
    return shop_list
print(get_shop_list_by_dishes(dishes, person_count))
    


# Задача №3

import fileinput
with fileinput.FileInput(files=('1.txt', '2.txt', '3.txt'), encoding='utf8') as input:
    for line in input:
        print(line)
       


# f='1.txt'
# i=0
# with open (f, encoding='utf8') as file:
#     for line in file:
#         i+=1
# print(i)









