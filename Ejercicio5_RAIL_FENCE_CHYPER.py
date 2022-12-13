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

    