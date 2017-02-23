import random

class Dir:
    """ direction constants """
    N = 1
    E = 2
    S = 4
    W = 8
    next = {N:E, E:S, S:W, W:N}
    opposite = {N:S, E:W, S:N, W:E}
    all = (N, E, S, W)


def go(pos, dir):
    (x, y) = pos
    if dir == Dir.N: y -= 1
    if dir == Dir.E: x += 1
    if dir == Dir.S: y += 1
    if dir == Dir.W: x -= 1
    newPos = (x, y)
    return newPos


def cellOpen(num, dir):
    return num & dir

class TableMazeModel:
    def __init__(self, rowsNum, colsNum):
        self.rowsNum = rowsNum
        self.colsNum = colsNum
        self._data = []
        self._startingPoints = []
        for y in range(rowsNum):
            row = []
            for x in range(colsNum):
                row.append(0)
            self._data.append(row)
            
    def getCell(self, pos):
        """ get cell on given position (x,y) """
        x, y = pos
        return self._data[y][x]
    
    def setCell(self, pos, value):
        """ set cell on given position (x,y) """
        x, y = pos
        self._data[y][x] = value
        
    def canDigg(self, pos, dir):
        """ test if we can digg in this direction from this position (x,y)"""
        newPos = go(pos, dir)
        # we cannot go out of maze model
        if not self.inModel(newPos): return False
        # we cannot digg via open doors :-)
        if self.getCell(pos) & dir: return False
        # we dont want to digg to already visited rooms (cycles)
        if self.getCell(newPos) > 0: return False
        # otherwise we can digg in this direction        
        return True
    
    def whereCanDigg(self, pos):
        return [dir for dir in Dir.all if self.canDigg(pos, dir)]
    
    def inModel(self, pos):
        """ returns list of directions in which we can digg from this position (x,y) """
        x, y = pos 
        if x < 0: return False
        if x >= self.colsNum: return False
        if y < 0: return False
        if y >= self.rowsNum: return False
        return True

    def digg(self, pos, dir):
        """ digg (open door) from room pos in direction dir. Return new position """
        cell = self.getCell(pos)
        self.setCell(pos, cell | dir) # open door in first cell
        pos = go(pos, dir) # go to new cell
        cell = self.getCell(pos)
        self.setCell(pos, cell | Dir.opposite[dir]) # open door in seconds cell
        return pos
    
    def genPath(self, startPos=(0, 0)):
        """ generate random path in maze """
        pos = startPos
        possibleDirs = self.whereCanDigg(pos)
        count = 1
        while possibleDirs:
            dir = random.choice(possibleDirs)
            if len(possibleDirs) > 1:
                self._startingPoints.append(pos)
                random.shuffle(self._startingPoints)
            pos = self.digg(pos, dir)
            possibleDirs = self.whereCanDigg(pos)
            count += 1
            if count > 5: break
            
    def genMaze(self):
        """ generate maze starting from startPos """
        self._startingPoints.append((0,0))
        while self._startingPoints:
            self.genPath(self._startingPoints.pop())

        return self._data
    

    def __repr__(self):
        theme = ['+---+---+---+---+',
                 '|   |           |',
                 '+   +   +   +   +',
                 '|   |           |',
                 '+   +   +   +   +',
                 '|   |           |',
                 '+---+---+---+---+',
                 '|   |           |',
                 '+---+---+---+---+']

        def dirmap2xy(dirmap):
            magic_map = [ [4, 6, 14, 12],
                          [5, 7, 15, 13],
                          [1, 3, 11, 9],
                          [0, 2, 10, 8]]
            if not dirmap in range(16):
                raise TypeError('dirmap must be in range [0..15]')
            
            for row_index, row in enumerate(magic_map):
                for cell_index, cell in enumerate(row):
                    if cell == dirmap:
                        return cell_index * 4, row_index * 2  

        def box(dirmap):
            x, y = dirmap2xy(dirmap)
            out = []
            for row in range(3): # cell height=3
                # out.append(unicode(theme[y + row])[x:x+5]) # cell width=5
                out.append(str(theme[y + row])[x:x+5]) # cell width=5
            return out 
        
        out = ""
        buf = []
        for row in range(1 + self.rowsNum * 2):
            buf.append([''] * (1 + self.colsNum * 4))
        for y in range(self.rowsNum):
            for x in range(self.colsNum):
                for cy, line in enumerate(box(self._data[y][x])):
                    for cx, char in enumerate(line):
                        buf[y*2+cy][x*4+cx] = char
        for row in buf:
            out += ''.join(row) + "\n"
        return out


if __name__ == "__main__":
    model = TableMazeModel(rowsNum=8, colsNum=8)
    model.genMaze()
    print str(model)

