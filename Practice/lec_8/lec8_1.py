def unique_sorted(lst):    # функциия сортировки уник.значений. принимает список
    dict_count = dict()    # создал пустой словарь
    for el in lst:
        dict_count[el] = dict_count.get(el, 0) + 1    # слева - значение элемента словаря с ключом el
        # справа - значение элемента словаря el + 1, или 0 + 1, если ключ el в формирующемся словаре не найден
    sorted_dict = sorted(dict_count.items(), key=lambda num: num[1])    # получили кортежи и отсортировали по 2 эл-ту
    output_list = list()    # создали пустой список
    for elem in sorted_dict:    # для всех кортежей - взять 1й элемент и добавить в список
        output_list.append(elem[0])
    return output_list


my_lst = [1, 2, 1, 3, 1, 4, 4, 5, 4, 6, 4, 7, 4, 7, 5, 5]
new_list = unique_sorted(my_lst)
print(new_list)

