"""
Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""

lst = [1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 6, 7, 8, 9, 8]
new_lst = []
for i, el in enumerate(lst):
    if not el in new_lst:
        for el2 in lst[i + 1:]:
            if el == el2:
                new_lst.append(el)
                break
print(new_lst)
