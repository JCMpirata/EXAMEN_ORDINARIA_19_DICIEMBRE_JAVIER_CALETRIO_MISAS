
class cifra:
    
        def __init__(self, numero):
            self.numero = numero
    
        def fibonacci(self):
            if self.numero == 0:
                return 0
            elif self.numero == 1:
                return 1
            elif self.numero < 0:
                print("Error: n debe ser mayor o igual a 0")
            else:
                return self.fibonacci(self.numero-1) + self.fibonacci(self.numero-2)

        def Fibonacci(self):
            lista = []
            for i in range(0, self.numero):
                if self.numero <= 2000000:
                    lista.append(self.fibonacci(i))
                else:
                    print("Error: n debe ser menor o igual a 2000000")



if __name__ == '__main__':
    numero = int(input("Ingrese un número: "))
    fibonacci = cifra(numero)
    print(fibonacci.Fibonacci())
    