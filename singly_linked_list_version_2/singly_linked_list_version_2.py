class Descriptor:
    """Дескриптор для класса StackObj."""
    def __set_name__(self, cls, name):
        self.name = f'_{cls.__name__}__{name}'

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self.name in obj.__dict__:
            return obj.__dict__[self.name]

    def __set__(self, obj, value):
        obj.__dict__[self.name] = value


class StackObj:
    """Класс представляет отдельный объект в односвязном списке."""
    data = Descriptor()
    next = Descriptor()

    def __init__(self, data):
        self.data = data  # ссылка на строку с переданными данными
        self.next = None  # ссылка на следующий объект односвязного списка (если следующего нет, то __next = None)


class Stack:
    """Класс для управления односвязным списком в целом."""
    def __init__(self, top=None):
        self.top = top  # ссылка на первый объект односвязного списка (если объектов нет, то top = None)

    def push_back(self, obj):
        """Метод добавляет объект класса StackObj в конец односвязного списка."""
        if self.top is None:
            self.top = obj
        else:
            prev_obj = self.top
            while prev_obj.next:
                prev_obj = prev_obj.next
            prev_obj.next = obj

    def pop_back(self):
        """Метод удаляет последний объект из односвязного списка."""
        if self.top:
            if self.top.next:
                prev_obj = self.top
                while prev_obj.next.next:
                    prev_obj = prev_obj.next
                prev_obj.next = None
            else:
                self.top = None

    def __add__(self, other):
        if isinstance(other, StackObj):
            self.push_back(other)
            return self
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, list):
            for i in other:
                self.push_back(StackObj(i))
            return self
        return NotImplemented

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
