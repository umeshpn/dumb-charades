import random

class DumbCharadesEngine:
    def __init__(self, clues):
        self.clues = clues.copy()

    def run(self):
        n_clues = len(self.clues)
        while n_clues > 0:
            dummy = input('Press ENTER to get the next clue, X to exit.')
            if dummy == 'X' or dummy == 'x':
                break
            index = random.randint(0, n_clues - 1)
            clue = self.clues[index]
            print(clue)
            self.clues.remove(clue)
            n_clues -= 1

if __name__ == '__main__':
    eng = DumbCharadesEngine([
        'One',
        'Two',
        'Three',
        'Four',
        'Five',
        'Six',
        'Seven',
        'Eight',
        'Nine',
        'Ten'
    ])
    eng.run()