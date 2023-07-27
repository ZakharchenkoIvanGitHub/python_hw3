"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
"""


def possible_combinations(items_dict: dict, max_cap: float) -> list:
    """
    Функция поиска возможных комбинаций
    :param items_dict: словарь с вещами
    :param max_cap: максимальная загрузка рюкзака
    :return: список комбинаций (последний элемент - масса вещей)
    """
    find = True
    keys = list(items_dict.keys())
    possible_list = []
    start = 0

    while find:
        total_massa = 0
        temp_list = []
        temp_key = keys[start:] + keys[0:start]
        for k in temp_key:

            if max_cap >= total_massa + items_dict[k]:
                temp_list.append(k)
                total_massa += items_dict[k]
                if max_cap == total_massa:
                    break
        temp_list.append(round(total_massa,1))
        possible_list.append(temp_list)
        start += 1
        if start == len(keys):
            find = False

    return possible_list


items_dictionary = {
    'Тент': 3.2,
    'Спальник': 1.8,
    'Печь': 2.5,
    'Фонарик': 0.3,
    'Палатка': 4.7,
    'Котелок': 1.1,
    'Кружка': 0.2,
}

# max_capacity = float(input("Введите максимальную грузоподъемность рюкзака"))
max_capacity = 5
print(*possible_combinations(items_dictionary, max_capacity),sep="\n")
