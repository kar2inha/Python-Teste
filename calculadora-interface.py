from calculator import Calculadora

print("Informe um valor:")
n1 = input()

print("Informe outro valor:")
n2 = input()

calculadora = Calculadora(n1, n2)
print(calculadora.soma())
print(calculadora.subt())
print(calculadora.mult())
print(calculadora.divi())