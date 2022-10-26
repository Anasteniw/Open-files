
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

dishes = list(cook_book.keys())
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
import os
from pprint import pprint
import fileinput


path = r'C:\Users\anast\Desktop\texts'

rez = sorted(os.listdir(path))
file_name_list = []
for item in rez:
    if item.endswith('.txt'):
        file_name = item
        file_name_list.append(file_name)


str_file_amount =[]
for file in file_name_list:
    with open (file, encoding='utf8') as f:
        str_file = f.readlines()
        str_amount = len(str_file)
        str_file_amount.append(str_amount)


files_dict = {file_name_list[i]: str_file_amount[i] for i in range(len(file_name_list))}


sorted_values = sorted(files_dict.values())
sorted_dict = {}
for i in sorted_values:
    for k in files_dict.keys():
        if files_dict[k] == i:
            sorted_dict[k] = files_dict[k]
            break

with fileinput.FileInput(files=sorted_dict, encoding='utf8') as input:
    for line in input:
        with open('new_file.txt', 'a', encoding='utf-8') as f2:
            f2.writelines(line)
            f2.close()









