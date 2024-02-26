class Rat (object):
    def __init__ (self, name, location = None, haveMemory = False, haveHeuristic = False):
        self.icon = '🐀'
        self.name = name
        self.location = location
        self.foundCheese = False
        self.haveMemory = haveMemory
        self.memory = set( ) if haveMemory else None
        self.haveHeuristic = haveHeuristic
        self.desicionNodes = [] if haveMemory else None

    def __str__ (self):
        return self.name
    
    def getIcon (self):
        return self.icon

    def setLocation (self, location):
        self.location = location

    def getLocation (self):
        return self.location
    
    def heuristic (self, map):
        x, y = self.location
        cheese = None

        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == '2':
                    cheese = (j, i)
                    break

        if cheese:
            return abs(cheese[0] - x) + abs(cheese[1] - y)
        else:
            return 0
    
    def move (self, map):
        if self.haveMemory:
            self.moveWithMemory(map)
        else:
            self.moveBasic(map)

    def moveBasic (self, map):
        x, y = self.location

        if map[y][x] == '2':
            self.foundCheese = True
            return

        moveUp = [x, y - 1]
        moveDown = [x, y + 1]
        moveLeft = [x - 1, y]
        moveRight = [x + 1, y]

        combinations = {
            ('0', '0', '0', '0'): moveRight,
            ('0', '1', '1', '1'): moveUp,
            ('1', '0', '1', '1'): moveDown,
            ('1', '1', '0', '1'): moveLeft,
            ('1', '1', '1', '0'): moveRight,
            ('0', '1', '0', '0'): moveRight,
            ('1', '0', '0', '1'): moveDown,
            ('0', '1', '1', '0'): moveRight,
            ('1', '0', '1', '0'): moveDown,
            ('0', '0', '1', '0'): moveRight,
            ('1', '0', '0', '0'): moveRight,
            ('0', '0', '0', '1'): moveDown,
            ('1', '1', '0', '0'): moveRight,
            ('0', '0', '1', '1'): moveDown,
        }

        up = str(map[y - 1][x]) if 0 <= y - 1 < len(map[x]) else '1'
        down = str(map[y + 1][x]) if 0 <= y + 1 < len(map[x]) else '1'
        left = str(map[y][x - 1]) if 0 <= x - 1 < len(map) else '1'
        right = str(map[y][x + 1]) if 0 <= x + 1 < len(map) else '1'
                    
        for combination, move in combinations.items():
            if up == '2':
                self.location = moveUp
                break
            elif down == '2':
                self.location = moveDown
                break
            elif left == '2':
                self.location = moveLeft
                break
            elif right == '2':
                self.location = moveRight
                break

            if (up, down, left, right) == combination:
                new_x, new_y = move
                if 0 <= new_x < len(map) and 0 <= new_y < len(map[new_x]): 
                    self.location = move
                    break

    def moveWithMemory (self, map):
        x, y = self.location
        self.memory.add((x, y))

        if map[y][x] == '2':
            self.foundCheese = True
            return

        moveUp = [x, y - 1]
        moveDown = [x, y + 1]
        moveLeft = [x - 1, y]
        moveRight = [x + 1, y]

        combinations = {
            ('0', '0', '0', '0'): (moveUp, moveDown, moveLeft, moveRight),
            ('0', '1', '1', '1'): (moveUp, None, None, None),
            ('1', '0', '1', '1'): (None, moveDown, None, None),
            ('1', '1', '0', '1'): (None, None, moveLeft, None),
            ('1', '1', '1', '0'): (None, None, None, moveRight),
            ('0', '1', '0', '0'): (moveUp, None, moveLeft, moveRight),
            ('1', '0', '0', '1'): (None, moveDown, moveLeft, None),
            ('0', '1', '1', '0'): (moveUp, None, None, moveRight),
            ('1', '0', '1', '0'): (None, moveDown, None, moveRight),
            ('0', '0', '1', '0'): (moveUp, moveDown, None, moveRight),
            ('1', '0', '0', '0'): (None, moveDown, moveLeft, moveRight),
            ('0', '0', '0', '1'): (moveUp, moveDown, moveLeft, None),
            ('1', '1', '0', '0'): (None, None, moveLeft, moveRight),
            ('0', '0', '1', '1'): (moveUp, moveDown, None, None),
            ('0', '1', '0', '1'): (moveUp, None, moveLeft, None),
        }

        up = str(map[y - 1][x]) if 0 <= y - 1 < len(map[x]) else '1'
        down = str(map[y + 1][x]) if 0 <= y + 1 < len(map[x]) else '1'
        left = str(map[y][x - 1]) if 0 <= x - 1 < len(map) else '1'
        right = str(map[y][x + 1]) if 0 <= x + 1 < len(map) else '1'

        for combination, moves in combinations.items():
            if up == '2':
                self.location = moveUp
                return
            elif down == '2':
                self.location = moveDown
                return
            elif left == '2':
                self.location = moveLeft
                return
            elif right == '2':
                self.location = moveRight
                return

            if (up, down, left, right) == combination:
                for move in moves:
                    if move:
                        new_x, new_y = move
                        if 0 <= new_x < len(map) and 0 <= new_y < len(map[new_x]): 
                            if self.haveMemory and (new_x, new_y) in self.memory:
                                continue

                            if combination.count('0') != 1 and tuple(self.location) not in self.desicionNodes:
                                self.desicionNodes.append(tuple(self.location))

                            self.location = move
                            self.memory.add((new_x, new_y))
                            return
                    else:
                        continue
                    
                if tuple(self.location) in self.desicionNodes:
                    self.desicionNodes.remove(tuple(self.location))
                    if len(self.desicionNodes) > 0:
                        self.location = list(self.desicionNodes.pop())

                    return
                
                if len(self.desicionNodes) > 0:
                    node = self.desicionNodes.pop()
                    self.desicionNodes.append(node)
                    self.location = list(node)
                    return
    