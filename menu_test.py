import pygame_menu
import pygame as pg

pg.init()

class Menu:
    def __init__(self):
        self.surface = pg.display.set_mode((900, 550))
        self.menu = pygame_menu.Menu(
            height=550,
            width=900,
            theme=pygame_menu.themes.THEME_SOLARIZED,
            title="КОРЕЙСКАЯ БИТВА МАГОВ"
        )

        self.menu.add.text_input("Имя:", default="Иван", onchange=self.set_name)
        self.menu.add.selector("Сложность: ", [("Высокая", 2), ("Невероятная", 1), ("Невозможная", 3)], onchange=self.set_difficulty)
        self.menu.add.label(title="Безумству храбрых поём мы песню...")
        self.menu.add.button("Войти в игру", self.start_game)
        self.menu.add.button("Выйти", self.quit_game)

        self.run()

    def start_game(self):
        ...

    def quit_game(self):
        ...

    def run(self):
        self.menu.mainloop(self.surface)

    def set_name(self, value):
        print(f"Ваше имя: {value}")

    def set_difficulty(self, selected, value):
        print(selected, value)



if __name__ == "__main__":
    menu = Menu()

