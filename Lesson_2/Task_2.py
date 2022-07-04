import random
import tkinter
from tkinter import messagebox

# Указываем размеры игрового поля
CELL_SIZE = 50
FIELD_SIZE = 10
WIDTH = 500
HEIGHT = 505
GEOM = f'{WIDTH}x{HEIGHT}'

root = tkinter.Tk()  # Создаём окошко в котором будет отрисовываться сама игра
root.geometry(GEOM)
root.title("Игра 'Обратные крестики-нолики!'")
root.resizable(width=False, height=False)  # Блокируем размеры окна


def main():
    window = Window(root)
    window.grid()
    game = Game()

    def position(event):
        x = event.x
        y = event.y
        if game.click_position(x, y, window):  # Передаем ход компьютеру
            game.computer_move(window)

    root.bind("<Button-1>", position)
    root.mainloop()


class Window:
    def __init__(self, rt):
        self.game_window = tkinter.Canvas(rt, width=WIDTH, height=WIDTH, bg='grey')
        self.game_window.pack()

    # Рисуем сетку
    def grid(self):
        self.game_window.create_rectangle(2, 2, WIDTH - 3, WIDTH)
        for i in range(FIELD_SIZE):
            self.game_window.create_line(i * CELL_SIZE, 0, i * CELL_SIZE, WIDTH)
            self.game_window.create_line(0, i * CELL_SIZE, HEIGHT, i * CELL_SIZE)

    # Крестик
    def draw_x(self, x, y, color):
        self.game_window.create_line(CELL_SIZE * x, CELL_SIZE * y, CELL_SIZE * x + CELL_SIZE,
                                     CELL_SIZE * y + CELL_SIZE, width=5, fill=color)
        self.game_window.create_line(CELL_SIZE * x + CELL_SIZE, CELL_SIZE * y, CELL_SIZE * x,
                                     CELL_SIZE * y + CELL_SIZE, width=5, fill=color)

    # Нолик
    def draw_o(self, x, y, color):
        self.game_window.create_oval(CELL_SIZE * x, CELL_SIZE * y, CELL_SIZE * x + CELL_SIZE,
                                     CELL_SIZE * y + CELL_SIZE, width=5, outline=color)


# Логика игры
class Game:
    def __init__(self):
        self.grid_field = [[i * CELL_SIZE, (i + 1) * CELL_SIZE] for i in range(FIELD_SIZE)]
        self.dot_field = [[0 for _ in range(FIELD_SIZE)] for _ in range(FIELD_SIZE)]

    # Проверка проигрыша или победы
    def check_win(self):
        for i in range(FIELD_SIZE):
            for j in range(FIELD_SIZE - 4):
                if self.dot_field[i][j] == self.dot_field[i][j + 1] == self.dot_field[i][j + 2] == \
                        self.dot_field[i][j + 3] == self.dot_field[i][j + 4] != 0:
                    return True
        for i in range(FIELD_SIZE - 4):
            for j in range(FIELD_SIZE):
                if self.dot_field[i][j] == self.dot_field[i + 1][j] == self.dot_field[i + 2][j] == \
                        self.dot_field[i + 3][j] == self.dot_field[i + 4][j] != 0:
                    return True
        for i in range(FIELD_SIZE - 4):
            for j in range(FIELD_SIZE - 4):
                if self.dot_field[i][j] == self.dot_field[i + 1][j + 1] == self.dot_field[i + 2][j + 2] == \
                        self.dot_field[i + 3][j + 3] == self.dot_field[i + 4][j + 4] != 0:
                    return True
        for i in range(FIELD_SIZE - 4):
            for j in range(4, FIELD_SIZE):
                if self.dot_field[i][j] == self.dot_field[i + 1][j - 1] == self.dot_field[i + 2][j - 2] == \
                        self.dot_field[i + 3][j - 3] == self.dot_field[i + 4][j - 4] != 0:
                    return True

    def computer_move(self, window):
        y = random.randint(0, 9)
        x = random.randint(0, 9)
        if self.dot_field[y][x] == 0:
            self.dot_field[y][x] = 2
            color = 'purple'
            window.draw_o(x, y, color)
            if self.check_win():  # Проверка проигрыша или победы компьютера
                messagebox.showinfo("GAMEOVER!!!", "Выиграл компьютер!")
                root.destroy()
        else:
            return self.computer_move(window)

    def click_position(self, x, y, window):
        for i in range(FIELD_SIZE):
            if self.grid_field[i][0] <= x <= self.grid_field[i][1]:
                x = i
            if self.grid_field[i][0] <= y <= self.grid_field[i][1]:
                y = i
        if self.dot_field[y][x] == 0:
            self.dot_field[y][x] = 1
            color = 'black'
            window.draw_x(x, y, color)
            if self.check_win():  # Проверка проигрыша или победы игрока
                messagebox.showinfo("GAMEOVER!!!", "Вы проиграли!")
                root.destroy()
                return False
            return True
        else:
            return False


if __name__ == "__main__":
    main()
