import random
class GamePole:
    __instance = None

    def __new__(cls, *args, **kwargs):
        """Разрешается создавать только один объект класса GamePole (паттерн Singleton)."""
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, N, M, total_mines):
        self.N = N
        self.M = M
        self.total_mines = total_mines
        self.__pole_cells = [[Cell() for _ in range(M)] for _ in range(N)]

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        """Инициализация начального состояния игрового поля."""
        coords = [(i, j) for i in range(self.N) for j in range(self.M)]
        for k in range(self.total_mines):
            i, j = random.choice(coords)
            self.pole[i][j].is_mine = True
            coords.remove((i, j))
        for i in range(self.N):
            for j in range(self.M):
                mines = 0
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        if 0 <= k <= self.N - 1 and 0 <= l <= self.M - 1:
                            if self.pole[k][l].is_mine:
                                mines += 1
                self.pole[i][j].number = mines

    def open_cell(self, i, j):
        """Метод открывает ячейку с индексами (i, j)."""
        if i > self.N - 1 or j > self.M - 1:
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        self.pole[i][j].is_open = True

    def show_pole(self):
        """Метод отображает игровое поле в консоли."""
        for i in range(self.N):
            for j in range(self.M):
                if self.pole[i][j].is_open:
                    if self.pole[i][j].is_mine:
                        print('*', end='|')
                    else:
                        print(self.pole[i][j].number, end='|')
                else:
                    print('#', end='|')
            print()


class Cell:
    def __init__(self):
        self.is_mine = False  # булево значение True/False; True - в клетке находится мина, False - мина отсутствует
        self.number = 0  # число мин вокруг клетки (целое число от 0 до 8)
        self.is_open = False  # флаг того, открыта клетка или закрыта: True - открыта; False - закрыта

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, is_mine):
        if isinstance(is_mine, bool):
            self.__is_mine = is_mine
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if type(number) == int and 0 <= number <= 8:
            self.__number = number
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, is_open):
        if isinstance(is_open, bool):
            self.__is_open = is_open
        else:
            raise ValueError("недопустимое значение атрибута")

    def __bool__(self):
        if self.is_open:
            return False
        else:
            return True
