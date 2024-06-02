class Board:
    """this class is used for ASCII visualization of the board
    """
    def __init__(self):
        self.board:list[list[str]] = []
        for i in range(8):
            self.board.append([])
            for j in range(16):
                self.board[i].append(' ')

    
    def setBlankBoard(self):
        for i in range(8):
            for j in range(0,16,2):
                self.board[i][j] = '+'
    
    def updateBoard(self,queens):
        self.setBlankBoard()
        
        for col in range(len(queens)):
            # index = column, value at index = row
            self.board[int(queens[col])-1][col*2] = 'Q'
    
    def printBoard(self):
        for row in self.board:
            for e in row:
                print(e,end='')
            print('')
    
    