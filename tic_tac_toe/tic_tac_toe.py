import random
class TicTacToe:
    """Класс для управления игровым процессом в крестики-нолики."""
    FREE_CELL = 0   # свободная клетка
    HUMAN_X = 1     # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))  # двумерный кортеж, размером 3x3
        self.__free_coords = [(i, j) for i in range(3) for j in range(3)]  # свободные координаты игрового поля

    def init(self):
        """Метод инициализирует игру (очищает игровое поле)."""
        self.__free_coords = [(i, j) for i in range(3) for j in range(3)]
        for i in range(3):
            for j in range(3):
                self.pole[i][j].value = self.FREE_CELL

    @staticmethod
    def __check_ind(item):
        """Метод проверяет указанные индексы на корректность."""
        i, j = item
        if type(i) != int or type(j) != int or not (0 <= i <= 2) or not (0 <= j <= 2):
            raise IndexError('некорректно указанные индексы')

    @staticmethod
    def __check_coords(coords):
        if len(coords.split(', ')) == 2:
            i, j = coords.split(', ')
            return i.isdigit() and j.isdigit() and 0 <= int(i) <= 2 and 0 <= int(j) <= 2
        return False

    def show(self):
        """Метод отображает текущее состояния игрового поля."""
        d = {0: '#', 1: 'X', 2: '0'}
        for i in range(3):
            for j in range(3):
                print(d[self.pole[i][j].value], end='')
            print()

    def human_go(self):
        """Реализация хода игрока (метод запрашивает координаты свободной клетки и ставит туда крестик)."""
        coords = input('Введите индексы крестика в формате "i, j": ')
        while 1:
            if not self.__check_coords(coords):
                coords = input('Индексы были введены неверно, введите индексы крестика в формате "i, j" повторно: ')
            else:
                i, j = coords.split(', ')
                i, j = int(i), int(j)
                if (i, j) not in self.__free_coords:
                    coords = input('Клетка по данным индексам занята,'
                                   ' введите индексы крестика в формате "i, j" повторно: ')
                else:
                    self.__free_coords.remove((i, j))
                    self.pole[i][j].value = self.HUMAN_X
                    break

    def computer_go(self):
        """Реализация хода компьютера (метод ставит случайным образом нолик в свободную клетку)."""
        i, j = random.choice(self.__free_coords)
        self.__free_coords.remove((i, j))
        self.pole[i][j].value = self.COMPUTER_O

    def __getitem__(self, item):
        """Метод позволяет получать значение из клетки с индексами i, j."""
        self.__check_ind(item)
        i, j = item
        return self.pole[i][j].value

    def __setitem__(self, key, value):
        """Метод позволяет записывать новое значения в клетку с индексами i, j."""
        self.__check_ind(key)
        i, j = key
        self.pole[i][j].value = value

    def __define_winner(self, value):
        pole = [[self.pole[i][j].value for j in range(3)] for i in range(3)]
        if any(all(j == value for j in i) for i in pole):
            return True
        if any(all(j == value for j in i) for i in zip(*pole)):
            return True
        if all(pole[i][i] == value for i in range(3)):
            return True
        if all(pole[2 - i][i] == value for i in range(3)):
            return True
        return False

    @property
    def is_human_win(self):
        """Метод возвращает True, если победил человек, иначе - False."""
        return self.__define_winner(self.HUMAN_X)

    @property
    def is_computer_win(self):
        """Метод возвращает True, если победил компьютер, иначе - False."""
        return self.__define_winner(self.COMPUTER_O)

    @property
    def is_draw(self):
        """Метод возвращает True, если ничья, иначе - False."""
        if self.is_human_win or self.is_computer_win or self.__free_coords:
            return False
        return True

    def __bool__(self):
        """Метод возвращает True, если игра не окончена (никто не победил и есть свободные клетки)
         и False - в противном случае."""
        return not (self.is_computer_win or self.is_human_win) and bool(self.__free_coords)


class Cell:
    """Класс представляет элемент кортежа pole."""
    def __init__(self, value=0):
        self.value = value  # текущее значение в ячейке: 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик

    def __bool__(self):
        """Метод возвращает True если клетка свободна."""
        return self.value == 0


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()
    print()
    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1

game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")
    
