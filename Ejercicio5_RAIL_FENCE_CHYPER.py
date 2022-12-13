class rail_fence_chyper:
    def __init__(self, cuadricula):
        self.cuadricula = cuadricula
    def codificar(mensaje, clave):
        fila, columna = 0, 0
        i = 1
        tabla1 = [["." for cols in range(len(mensaje))] for rows in range(clave)]
        while columna < len(mensaje):
            if fila + i < 0 or fila + i >= clave:
                i = i*-1
            tabla1[fila][columna]= mensaje[columna]
            fila = fila + i
            columna = columna + 1

        Encripcion = ""
        for j in tabla1:
            Encripcion = Encripcion + "".join(j)
            print(j)
        return Encripcion

    def descodificar (mensaje, valor):
        fila, columna = 0, 0
        i = 1
        tabla2 = [["" for cols in range(len(mensaje))] for rows in range(valor)]
        while columna < len(mensaje):
            if fila + i < 0 or fila + i >= valor:
                i = i*-1
            tabla2[fila][columna] = "*"
            fila = fila + i
            columna = columna + 1
        index = 0
        for fila in range(valor):
            for columna in range(len(mensaje)):
                if tabla2[row][col]== "*":
                    tabla2[row][col] = mensaje[index]
                    index = index+1
        Decripcion = ""
        row = 0
        col = 0
        i=1
        while col < len(mensaje):
            if fila + i < 0 or  + i >= valor:
                i=i*-1
            Decripcion =Decripcion + tabla2[row][col]
            row=row+i
            col=col+1
        return Decripcion
if __name__ == '__main__':
    rail_fence_chyper = rail_fence_chyper()
    mensaje = "Neuschwansstein"
    clave = 3
    print(rail_fence_chyper.codificar(mensaje, clave))
    print(rail_fence_chyper.descodificar(mensaje, clave))