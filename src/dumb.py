import random
import sys
import re

class DumbCharadesClueGenerator:
    def __init__(self):
        self.clues = []

    def loadData(self, files, title):
        self.clues = []
        for file in files:
            self.addDataFromFile(title, file)
        print('A total of %d clues loaded' % len(self.clues))

    def loadMalayalamData(self, prefix, files):
        self.clues = []
        startYear = input("Start year (1970 - 2010)? : ")
        endYear = input("End year (1970 - 2010)? : ")
        prefixLen = len(prefix)
        for file in files:
            if file[0:prefixLen] == prefix:
                end = prefixLen + 4
                year = file[prefixLen:end]
                if year >= startYear and year <= endYear:
                    self.addDataFromFile(year, file)
            else:
                print ("File name %s doesn't have the prefix %s" % (file, prefix))
        print('A total of %d clues loaded' % len(self.clues))

    def addDataFromFile(self, year, file):
        cnt = 0
        print('%s:' % year, end='')
        with open(file, "r") as input:
            for line in input.readlines():
                if re.match("^\s*#.*$", line):
                    continue
                cnt += 1
                sys.stdout.write('.')
                self.clues.append('%s : %s' % (year, line[:-1]))
        print (' : %d' % cnt)

    def showRandomClue(self):
        while True:
            nClues = len(self.clues)
            x = input("")
            if x == "X":
                break
            i = random.randint(0, nClues - 1)
            clue = self.clues[i]
            print(clue)
            self.clues.remove(clue)

        print("It is over!  Now start over...")


    def doMalayalam(self):
        malMovies = [
            "mal-1970.txt",
            "mal-1971.txt",
            "mal-1972.txt",
            "mal-1973.txt",
            "mal-1974.txt",
            "mal-1975.txt",
            "mal-1976.txt",
            "mal-1977.txt",
            "mal-1978.txt",
            "mal-1979.txt",
            "mal-1980.txt",
            "mal-1981.txt",
            "mal-1982.txt",
            "mal-1983.txt",
            "mal-1984.txt",
            "mal-1985.txt",
            "mal-1986.txt",
            "mal-1987.txt",
            "mal-1988.txt",
            "mal-1989.txt",
            "mal-1990.txt",
            "mal-1991.txt",
            "mal-1992.txt",
            "mal-1993.txt",
            "mal-1994.txt",
            "mal-1995.txt",
            "mal-1996.txt",
            "mal-1997.txt",
            "mal-1998.txt",
            "mal-1999.txt",
            "mal-2000.txt",
            "mal-2001.txt",
            "mal-2002.txt",
            "mal-2003.txt",
            "mal-2004.txt",
            "mal-2005.txt",
            "mal-2006.txt",
            "mal-2007.txt",
            "mal-2008.txt",
            "mal-2009.txt",
            "mal-2010.txt",
        ]

        self.loadMalayalamData("mal-", malMovies)
        self.showRandomClue()

    def doHollywood(self):
        self.loadData(["movies-hits.txt"], "Movie")
        self.showRandomClue()

    def doMahabhrata(self):
        self.loadData(["mahabharata.txt"], "Movie")
        self.showRandomClue()

    def doDisney(self):
        self.loadData(["movies-disney.txt"], "Disney movie")
        self.showRandomClue()

    def doBooks(self):
        # self.loadData(["books-all.txt"], "Book")
        # self.loadData(["books.txt"], "Book")
        # self.loadData(["new-books.txt"], "Book")
        self.loadData(["books-full.txt"], "Book")
        self.showRandomClue()

    def doIdioms(self):
        self.loadData(["idioms-all.txt"], "Idiom")
        self.showRandomClue()


if __name__ == '__main__':
    gen = DumbCharadesClueGenerator()
    choice = "0"
    while choice < "1" or choice > "5":
        print("1 : Malayalam")
        print("2 : Hollywood movies")
        print("3 : Disney movies")
        print("4 : Books")
        print("5 : English idioms")
        print("6 : Mahabharata")
        print("7 : Exit")

        choice = input("\nEnter choice (1-5) : ")

        if choice == "1":
           gen.doMalayalam()
        elif choice == "2":
           gen.doHollywood()
        elif choice == "3":
           gen.doDisney()
        elif choice == "4":
           gen.doBooks()
        elif choice == "5":
           gen.doIdioms()
        elif choice == "6":
           gen.doMahabhrata()
        elif choice == "7":
           break


