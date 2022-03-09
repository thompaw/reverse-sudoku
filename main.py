import random


def makeGameBoard():
    boarb = [[], [], [], [], [], [], [], [], []]
    for x in range(9):
        for y in range(9):
            boarb[x][y] = 'X'
    return boarb




class gameBoard:
    def __init__(self, boardin=None):
        if boardin == None:
            self.board = makeGameBoard()
        else:
            self.board = boardin





if __name__ == "__main__":
    pass