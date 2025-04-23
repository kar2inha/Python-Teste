class Calculadora:
    def __init__(self, n1, n2):
        self.n1 = float(n1)
        self.n2 = float(n2)
        self.result = 0

    def soma(self):
        self.result = self.n1 + self.n2
        return self.result

    def subt(self):
        self.result = self.n1 - self.n2
        return self.result
    
    def mult(self):
        self.result = self.n1 * self.n2
        return self.result
    
    def divi(self):
        self.result = self.n1 / self.n2
        return self.result