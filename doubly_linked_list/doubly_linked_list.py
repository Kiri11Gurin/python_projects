class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head  # ссылка на первый объект связного списка (если список пустой, то head = None)
        self.tail = tail  # ссылка на последний объект связного списка (если список пустой, то tail = None)

    def add_obj(self, obj):
        """Метод добавляет новый объект obj класса ObjList в конец связного списка."""
        if self.head is None:
            self.head = obj
            self.tail = obj
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj

    def remove_obj(self):
        """Метод удаляет последний объект из связного списка."""
        if self.tail is not None:
            if self.tail.get_prev() is not None:
                temp_tail = self.tail
                self.tail = self.tail.get_prev()
                temp_tail.set_prev(None)
                self.tail.set_next(None)
            else:
                self.tail = None
                self.head = None

    def get_data(self):
        """Метод получает список из строк локального свойства __data всех объектов связного списка."""
        result = []
        obj = self.head
        while obj is not None:
            result.append(obj.get_data())
            obj = obj.get_next()
        return result


class ObjList:
    def __init__(self, data, next_=None, prev=None):
        self.__data = data  # строка с данными
        self.__next = next_  # ссылка на следующий объект связного списка (если след. объекта нет, то __next = None)
        self.__prev = prev  # ссылка на предыдущий объект связного списка (если пред. объекта нет, то __prev = None)

    def set_next(self, obj):
        """Метод изменяет приватное свойство __next на значение obj."""
        self.__next = obj

    def set_prev(self, obj):
        """Метод изменяет приватное свойство __prev на значение obj."""
        self.__prev = obj

    def get_next(self):
        """Метод получает значение приватного свойства __next."""
        return self.__next

    def get_prev(self):
        """Метод получает значение приватного свойства __prev."""
        return self.__prev

    def set_data(self, data):
        """Метод изменяет приватное свойство __data на значение data."""
        self.__data = data

    def get_data(self):
        """Метод получает значение приватного свойства __data."""
        return self.__data
