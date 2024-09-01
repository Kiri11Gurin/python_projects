class StackObj:
    def __init__(self, data):
        self.__data = data  # __data - ссылка на строку с данными, указанными при создании объекта
        self.__next = None  # __next - ссылка на след. объект класса StackObj (начальное значение None)

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if isinstance(obj, type(self)) or obj is None:
            self.__next = obj


class Stack:
    def __init__(self, top=None):
        self.top = top  # ссылка на первый добавленный объект односвязного списка (если список пуст, то top = None)

    def push(self, obj):
        """Метод добавляет объект класса StackObj в конец односвязного списка."""
        if self.top is None:
            self.top = obj
        else:
            last_obj = self.top
            while last_obj.next:
                last_obj = last_obj.next
            last_obj.next = obj

    def pop(self):
        """Метод извлекает последний объект с его удалением из односвязного списка."""
        popped_obj = None
        if self.top:
            if self.top.next:
                prev_obj, last_obj = self.top, self.top.next
                while last_obj.next:
                    prev_obj, last_obj = last_obj, last_obj.next
                prev_obj.next = None
                popped_obj = last_obj
            else:
                popped_obj = self.top
                self.top = None
        return popped_obj

    def get_data(self):
        """Метод получает список из объектов односвязного списка
        (список из строк локального атрибута __data каждого объекта
        в порядке их добавления, или пустой список, если объектов нет)."""
        result = []
        last_obj = self.top
        while last_obj:
            result.append(last_obj.data)
            last_obj = last_obj.next
        return result
