from Rat import Rat
from Map import Map
from Cheese import Cheese

def main():
    rat = Rat('Remy', haveMemory = True)
    cheese = Cheese()
    map = Map(rat, cheese, 'map.txt')

    map.startGame()

main()
