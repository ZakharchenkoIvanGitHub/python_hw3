"""
Задание №8

✔ Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:

✔ Какие вещи взяли все три друга

✔ Какие вещи уникальны, есть только у одного друга

✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует

✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей.
"""
data = {"Вася": ("Палатка", "Котелок", "Спички", "Шашлык"),
        "Витя": ("Палатка", "Котелок", "Топор"),
        "Петя": ("Палатка", "Котелок", "Топор", "Спирт"),
        "Саша": ("Палатка", "Спирт"),
        }

lst = []
for k, v in data.items():
    lst.append(set(v))

res_all = lst[0]
for things in lst[1:]:
    res_all = res_all.intersection(things)
print(f"{res_all} есть у всех")

st = set()
for s in data:
    st = set(data[s])
    for f in data:
        if s != f:
            st = st.difference(set(data[f]))
    if st:
        print(f"Только {s} имеет {st}")

for s in data:
    st = set(data[s])
    st_f = set()
    for f in data:
        if s != f:
            st_f = st_f.intersection(set(data[f])) if st_f else set(data[f])
    if st_f:
        delta = st_f.difference(st)
        if delta:
            print(f"Только {s} не имеет {delta}")
