
personUnkown = ' '
person_x = 'x'
person_0 = '0'

class Cell:
    def __init__(self):
        self.person = personUnkown

    def setPerson(self, person):
         self.person = person
    
    def getPerson(self):
        return self.person  

class Board:
    def __init__(self, r = 3, c = 3):
         self.cells = []
         self.rowsCount = r
         self.columnsCount = c
         for i in range(r*c):
              self.cells.append(Cell())

    def getRowsCount(self):
        return self.rowsCount
    
    def getColumnsCount(self):
        return self.columnsCount

    def isCellAvailible(self, index):
         return self.cells[index-1].getPerson() == personUnkown  

    def getPersonInCell(self, index):
         return self.cells[index-1].getPerson()      

    def setCell(self, index, person):
         self.cells[index-1].setPerson(person)
    
    def getCells(self):
         return self.cells
    
class Player:
    def __init__(self, name, person):
          self.name = name
          self.person = person
    
    def getName(self):
        return self.name
    
    def getPerson(self):
        return self.person

def winCondition(board):
    win_combo = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]        
    
    winPerson = personUnkown
    for combo in win_combo:
        m1 = board.getPersonInCell(combo[0])
        m2 = board.getPersonInCell(combo[1])
        m3 = board.getPersonInCell(combo[2])
        if (m1 == m2 == m3) :
             winPerson = m1
             break
    
    return winPerson

def render(board):
    rc = board.getRowsCount()
    cl = board.getColumnsCount()

    for r in range(rc):
        row = []
        for c in range(cl):
            row.append(board.getPersonInCell(r*cl+c+1))
        print("|".join(row))
        
if __name__ == '__main__':
    #get users
    #swich turns
    #get action
        
 board = Board()
 p1 = Player("1", person_x)
 p2 = Player("2", person_0)

 board.setCell(5, p1.getPerson())
 board.setCell(1, p2.getPerson())
 board.setCell(3, p1.getPerson())
 board.setCell(2, p2.getPerson())

print("win:" + winCondition(board))
render(board)

print("----------------------------------------------------------------")
board.setCell(7, p1.getPerson())
print("win:" + winCondition(board))
render(board)
