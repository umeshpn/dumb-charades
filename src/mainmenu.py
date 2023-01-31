from Menu import DumbCharadesMenu


class MalayalaMoviesMenu(DumbCharadesMenu):
    pass


class HollywoodMoviesMenu:
    pass


class DisneyMoviesMenu:
    pass


class BooksMenu:
    pass


class IdiomsMenu:
    pass


class MainMenu(DumbCharadesMenu):
    def __init__(self):
        super().__init__([
            'Malayalam movies',
            'Hollywood movies',
            'Disney movies',
            'Books',
            'Idioms',
            'Exit'
        ])

    def execute(self, option):
        if option == 1:
            MalayalaMoviesMenu().run()
        elif option == 2:
            HollywoodMoviesMenu().run()
        elif option == 3:
            DisneyMoviesMenu().run()
        elif option == 4:
            BooksMenu().run()
        elif option == 5:
            IdiomsMenu().run()
        else:
            print('Good bye!')

if __name__ == '__main__':
    MainMenu().run()
