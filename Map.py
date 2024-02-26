from colorama import Fore, Style
import os
import time

class Map (object):
    def __init__(self, rat, cheese, file):
        self.rat = rat
        self.cheese = cheese
        self.file = file
        self.map = self.loadMap(file)
        self.initialPositions()

    def loadMap(self, file):
        with open(file, 'r') as f:
            auxMap = f.read().splitlines()
        map = [''.join(fila.split()) for fila in auxMap]
        return map
    
    def initialPositions(self):
        for i, row in enumerate(self.map):
            for j, cell in enumerate(row):
                if cell == '3':
                    listRow = list(row)
                    listRow[j] = '0'
                    self.map[i] = ''.join(listRow)

                    self.rat.setLocation([j, i])
                elif cell == '2':
                    self.cheese.setLocation([j, i])
    
    def printColorCell(self, cell):
        if cell == '0':
            print(Fore.WHITE + cell, end=' ')
        elif cell == '1':
            print(Fore.RED + cell, end=' ')
        elif cell == '2':
            print('🧀', end=' ')
        else:
            print(cell, end=' ')

    def printMap(self):
        ratPosition = self.rat.getLocation()
        ratIcon = self.rat.getIcon()

        os.system('cls' if os.name == 'nt' else 'clear')

        for i, row in enumerate(self.map):
            for j, cell in enumerate(row):
                if [j, i] == ratPosition:
                    print(ratIcon, end=' ')
                else:
                    self.printColorCell(cell)
            print()

    def startGame(self):
        while True:
            self.printMap()
            self.rat.move(self.map)
            time.sleep(0.2)

            if self.rat.foundCheese:
                print('The rat ' + str(self.rat) + ' found the cheese!')
                break