import re
import sys

class DumbCharadesClueLoader:
    def __init__(self):
        self.clues = []

    def clues(self):
        return self.clues

    def load_data(self, title, files):
        self.clues = []
        for file in files:
            self.add_data_from_file(title, file)
        print('Total %d clues loaded' % len(self.clues))

    def load_data_for_years(self, prefix, files, start_year, end_year):
        self.clues = []
        prefix_len = len(prefix)
        for file in files:
            if file[0:prefix_len] == prefix:
                end = prefix_len + 4
                year = file[prefix_len:end]
                if start_year <= year <= end_year:
                    self.add_data_from_file(year, file)
            else:
                print("File name %s doesn't have the prefix %s" % (file, prefix))
        print('Total %d clues loaded' % len(self.clues))

    def add_data_from_file(self, year, file):
        cnt = 0
        with open(file, 'r') as f:
            for line in f.readlines():
                # Ignore comments.
                if re.match('^\s*#.*$', line):
                    continue
                cnt += 1
                sys.stdout.write('.')
                self.clues.append('%s : %s' % (year, line[:-1]))