from abc import abstractmethod

class DumbCharadesMenu:
    def __init__(self, options):
        self.options = options

    def display_menu(self):
        option_count = 0
        for option in self.options:
            option_count += 1
            print('%d. %s' % (option_count, option))
        result = 0
        while result < 1 or result > len(self.options):
            result= int(input('Enter the choice (1 - %d):  ' % len(self.options)))
        return result

    @abstractmethod
    def execute(self, option):
        '''
        Calls the appropriate routines based on the option given.
        :param option: An integer giving the option
        :return: None
        '''
        pass

    def run(self):
        option = self.display_menu()
        self.execute(option)