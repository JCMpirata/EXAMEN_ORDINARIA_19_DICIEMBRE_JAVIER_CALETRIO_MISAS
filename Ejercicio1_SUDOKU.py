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

    def valida_filas(self):
        for fila in self.tablero:
            if len(fila) != 9:
                return False
            for numero in fila:
                if numero != '.':
                    if fila.count(numero) > 1:
                        return False
        return True