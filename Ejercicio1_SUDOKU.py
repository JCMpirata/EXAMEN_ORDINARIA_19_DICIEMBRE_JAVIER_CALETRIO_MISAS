board = [
    ["5", ".", ".", ".", "4", ".", ".", ".", "9"],
    [".", "2", ".", ".", "1", ".", "6", "8", "."],
    [".", ".", "9", "8", "7", ".", "1", ".", "."],
    [".", ".", "6", "7", ".", ".", "2", ".", "."],
    [".", "9", ".", "3", "5", "4", ".", "6", "."],
    ["3", ".", ".", ".", ".", ".", ".", ".", "1"],
    ["9", ".", ".", ".", "6", ".", ".", ".", "2"],
    [".", "1", "4", ".", "3", ".", ".", "5", "7"],
    [".", ".", "5", ".", "8", "7", ".", ".", "."]
]

class valida_sudoku:
    def __init__(self, tablero):
        self.tablero = tablero

    def valida_fila(self):
        for fila in self.tablero:
            if len(fila) != 9:
                return False
            for numero in fila:
                if numero != '.':
                    if fila.count(numero) > 1:
                        return False
        return True
    
    def valida_columna(self):
        for columna in range(9):
            lista = []
            for fila in self.tablero:
                if fila[columna] != '.':
                    lista.append(fila[columna])
            if len(lista) != len(set(lista)):
                return False
        return True

    def valida_subcuadrado(self):
        for fila in range(0, 9, 3):
            for columna in range(0, 9, 3):
                lista = []
                for i in range(3):
                    for j in range(3):
                        if self.tablero[fila + i][columna + j] != '.':
                            lista.append(self.tablero[fila + i][columna + j])
                if len(lista) != len(set(lista)):
                    return False
        return True

if __name__ == '__main__':
    sudoku = valida_sudoku(board)
    print(sudoku.valida_fila())
    print(sudoku.valida_columna())
    print(sudoku.valida_subcuadrado())