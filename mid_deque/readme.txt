Реализуйте класс MidDeque, который описывает дек.

Экземпляры класса MidDeque должны поддерживать следующие методы:

push_back(x) – добавляет элемент x в конец дека
push_front(x) – добавляет элемент x в начало дека
push_mid(x) – добавляет элемент x в середину дека
pop_back() – удаляет и возвращает элемент из конца дека
pop_front() – удаляет и возвращает элемент из начала дека
pop_mid() – удаляет и возвращает элемент из середины дека
Все методы должны работать за константное время – O(1).

При добавлении элемента в середину дека или удалении его оттуда может существовать два варианта серединного положения: левый и правый. В таком случае должен выбираться левый вариант. Примеры:

Вставка числа 6 в середину дека [1, 2, 3, 4, 5]: 
[1, 2, 3, 4, 5] ➝ [1, 2, 6, 3, 4, 5]

                  
Удаление числа из середины дека [1, 2, 3, 4, 5, 6]: 
[1, 2, 3, 4, 5, 6] ➝ [1, 2, 4, 5, 6]

                  
Примечание. Гарантируется, что методы pop_back(), pop_front() и pop_mid() будет вызываться только для непустого дека.


# Тесты для проверки:
1)
dq = MidDeque()
dq.push_back(1)          # [1]
dq.push_back(2)          # [1, 2]
dq.push_back(3)          # [1, 2, 3]
print(dq.pop_mid())      # 2

2)
dq = MidDeque()
dq.push_back(1)          # [1]
dq.push_front(2)         # [2, 1]
dq.push_mid(3)           # [2, 3, 1]
print(dq.pop_back())     # 1
print(dq.pop_back())     # 3
print(dq.pop_back())     # 2

3)
dq = MidDeque()
dq.push_back(1)          # [1]
dq.push_mid(2)           # [2, 1]
dq.push_mid(3)           # [2, 3, 1]
dq.push_mid(-1)          # [2, -1, 3, 1]
print(dq.pop_front())    # 2
print(dq.pop_front())    # -1
print(dq.pop_front())    # 3
print(dq.pop_front())    # 1

4)
dq = MidDeque()
dq.push_back(1)          # [1]
dq.push_front(2)         # [2, 1]
dq.push_back(3)          # [2, 1, 3]
dq.push_front(4)         # [4, 2, 1, 3]
print(dq.pop_front())    # 4
print(dq.pop_back())     # 3
print(dq.pop_mid())      # 2
print(dq.pop_front())    # 1

5)
dq = MidDeque()
dq.push_mid(1)           # [1]
dq.push_mid(2)           # [2, 1]
dq.push_mid(3)           # [2, 3, 1]
dq.push_mid(4)           # [2, 4, 3, 1]
print(dq.pop_mid())      # 4
print(dq.pop_mid())      # 3
print(dq.pop_mid())      # 2
print(dq.pop_mid())      # 1
