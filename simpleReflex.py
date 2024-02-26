from Rat import Rat
from Map import Map
from Cheese import Cheese

def main():
    rat = Rat('Remy')
    cheese = Cheese()
    map = Map(rat, cheese, 'map2.txt')

    map.startGame()

main()
