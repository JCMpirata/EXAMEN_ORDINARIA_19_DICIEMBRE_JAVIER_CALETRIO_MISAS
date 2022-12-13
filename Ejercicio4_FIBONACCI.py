
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

        
    