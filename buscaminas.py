from random import randint


class Buscaminas:

    def __init__(self, rows, cols, bombs):
        self.rows = rows
        self.cols = cols
        self.bombs = bombs
        self.initial_board = [['-' for x in range(self.rows)] for y in range(self.cols)]
        self.board = self.crear_tablero()

    def crear_tablero(self):
        board = [[randint(1, 4) for x in range(self.rows)] for y in range(self.cols)]
        for i in range(self.bombs):
            board[randint(0,self.rows-1)][randint(0,self.cols-1)] = 'B'
        return board

    def show(self):
        return self.initial_board

    # ['flag', 'uncover']
    def play(self, mov, row, col):
        if mov == 'flag':
            self.initial_board[row][col] = 'F'
        if mov == 'uncover':
            if self.hay_bomba(row, col):
                self.lose()
            else:
                self.initial_board[row][col] = self.board[row][col]


    # mov = ['flag', 'uncover']
    def question(self, movs = ['flag','uncover']):

        while True:
            mov = input("Ingrese el movimiento, flag o uncover: ")
            if mov not in ('flag', 'uncover'):
                raise Exception
            else:
                break
        while True:
            row = input("Elija una fila para su movimiento: ")
            if row > self.rows:
                raise Exception
            else:
                break
        while True:
            col = input("Elija una columna: ")
            if col > self.cols:
                raise Exception
            else:
                break
        return [mov, row, col]


    def hay_bomba(self,row,col):
        if self.board[row][col] == 'B':
            return True

    def win(self):
        contador = 0
        for fil in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[fil][col] == 'B' and self.initial_board[fil][col] == 'F':
                    contador += 1
        if contador == self.bombs:
            return True
        else:
            return False

    def lose(self):
        return True

if __name__ == '__main__':
    b = Buscaminas(8,8,10)
    print(b.show())
    print(b.board)
    b.play('flag',0,2)
    print(b.show())
    b.play('flag',0,1)
    print(b.show())
    b.play('uncover', 2, 2)
    print(b.show())
